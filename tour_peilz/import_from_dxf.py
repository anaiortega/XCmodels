# -*- coding: utf-8 -*-
from __future__ import division
import math
import dxfgrabber
from scipy.spatial.distance import cdist
import numpy as np
import re
from import_export import BlockTopologyEntities as bte
from import_export import NeutralMeshDescription as nmd
from miscUtils import LogMessages as lmsg


dxf= dxfgrabber.readfile("rampe_quai_2.dxf")
layerstoimport= ['floor.*','bulkhead.*','roof.*','parapet.*','middle.*','side.*']

def layerToImport(layerName):
  for regExp in layerstoimport:
    if(re.match(regExp,layerName)):
      return True
  return False

def getRelativeCoo(pt):
  return [pt[0],pt[1],pt[2]] #No modification.

layerNames= []
for layer in dxf.layers:
  layerName= layer.name
  if(layerToImport(layer.name)):
    layerNames.append(layer.name)

print layerNames
 
points= []
for obj in dxf.entities:
  type= obj.dxftype
  if(layerToImport(obj.layer)):
    if(type == '3DFACE'):
      for pt in obj.points:
        points.append(getRelativeCoo(pt))
    elif(type == 'LINE'):
      for pt in [obj.start,obj.end]:
        points.append(getRelativeCoo(pt))
    elif(type == 'POINT'):
      points.append(getRelativeCoo(obj.point))

def getIndexNearestPoint(pt, kPts):
  return cdist([pt], kPts).argmin()

def getNearestPoint(pt, kPts):
  return kPts[getIndexNearestPoint(pt, kPts)]

#Get k-points.
threshold= 0.01
kPoints= [points[0]]
for p in points:
  nearestPoint= getNearestPoint(p,kPoints)
  dist= cdist([p],[nearestPoint])[0][0]
  if(dist>threshold):
    kPoints.append(p)

print 'points= ', len(points)
print 'kPoints= ', len(kPoints)

#Get points
points= {}
for obj in dxf.entities:
  type= obj.dxftype
  layerName= obj.layer
  if(layerToImport(layerName)):
    if(type == 'POINT'):
      vertices= [-1]
      p= getRelativeCoo(obj.point)
      vertices[0]= getIndexNearestPoint(p,kPoints)
      points[obj.handle]= (layerName, vertices)

print 'points= ', len(points)


#Get lines
lines= {}
polylines= {}
for obj in dxf.entities:
  type= obj.dxftype
  lineName= obj.layer
  if(layerToImport(lineName)):
    if(type == 'LINE'):
      vertices= [-1,-1]
      p1= getRelativeCoo(obj.start)
      p2= getRelativeCoo(obj.end)
      length= cdist([p1],[p2])[0][0]
      vertices[0]= getIndexNearestPoint(p1,kPoints)
      vertices[1]= getIndexNearestPoint(p2,kPoints)
      if(vertices[0]==vertices[1]):
        print 'Error in line ', lineName, ' vertices are equal: ', vertices
      if(length>threshold):
        lines[lineName]= vertices
      else:
        print 'line too short: ', p1, p2, length
    elif(type == 'POLYLINE'):
      vertices= set()
      for p in obj.points:
        rCoo= getRelativeCoo(p)
        vertices.add(getIndexNearestPoint(rCoo,kPoints))
        polylines[lineName]= vertices

print 'lines= ', len(lines)
print 'polylines= ', len(polylines)

#Get faces
facesByLayer= {}
for name in layerNames:
  facesByLayer[name]= dict()

labelDict= {}
for obj in dxf.entities:
  type= obj.dxftype
  layerName= obj.layer
  if(layerToImport(layerName)):
    facesDict= facesByLayer[layerName]
    if(type == '3DFACE'):
      vertices= []
      for pt in obj.points:
        p= getRelativeCoo(pt)
        idx= getIndexNearestPoint(p,kPoints)
        vertices.append(idx)
      #print layerName, obj.handle
      labelDict[obj.handle]= [layerName]
      facesDict[obj.handle]= vertices

for name in layerNames:
  print name
  print facesByLayer[name]

#Orientation
supportOrientationVector= np.array([0,0,1])
for key in lines:
  vertices= lines[key]
  v= np.array(kPoints[vertices[1]])-np.array(kPoints[vertices[0]])
  dotProd= np.dot(v,supportOrientationVector)
  if(dotProd<0):
    lines[key]= list(reversed(vertices))
  #print key, vertices, v, dotProd

def getAverageOrientationFaces(faces):
  retval= [[0.0,0.0,0.0],[0.0,0.0,0.0]]
  for key in faces:
    vertices= faces[key]
    #orientation of local Z vector.
    v0= np.array(kPoints[vertices[1]])-np.array(kPoints[vertices[0]])
    retval[0][0]+=v0[0]; retval[0][1]+=v0[1]; retval[0][2]+=v0[2];
    v1= np.array(kPoints[vertices[2]])-np.array(kPoints[vertices[0]])
    retval[1][0]+=v1[0]; retval[1][1]+=v1[1]; retval[1][2]+=v1[2];
  n= len(faces)
  retval[0][0]/=n; retval[0][1]/=n; retval[0][2]/=n;
  retval[1][0]/=n; retval[1][1]/=n; retval[1][2]/=n;
  return retval

def getAngle(sampleVector, v1):
    cosine= np.dot(v1,sampleVector)/np.linalg.norm(v1)/np.linalg.norm(sampleVector) #Cosine of the angle.
    return np.arccos(np.clip(cosine, -1, 1))
  
def checkFacesOrientation(faces,sampleVectors):
  retval= {}
  for key in faces:
    vertices= faces[key]
    #orientation of local Z vector.
    v1= np.array(kPoints[vertices[1]])-np.array(kPoints[vertices[0]])
    v2= np.array(kPoints[vertices[3]])-np.array(kPoints[vertices[0]])
    v= np.cross(v1,v2)
    dotProd= np.dot(v,sampleVectors[1])
    if(dotProd>=0):
      retval[key]= vertices
    else:  
      retval[key]= list(reversed(vertices))
    #orientation of local X vector.
    v1= np.array(kPoints[retval[key][1]])-np.array(kPoints[retval[key][0]])
    angle= getAngle(sampleVectors[0],v1)
    if(abs(angle)>(math.pi/4.0)):
      retval[key]= [retval[key][1],retval[key][2],retval[key][3],retval[key][0]]
    v1= np.array(kPoints[retval[key][1]])-np.array(kPoints[retval[key][0]])
    angle= getAngle(sampleVectors[0],v1)
    if(abs(angle)>(math.pi/4.0)):
      retval[key]= [retval[key][1],retval[key][2],retval[key][3],retval[key][0]]
    v1= np.array(kPoints[retval[key][1]])-np.array(kPoints[retval[key][0]])
    angle= getAngle(sampleVectors[0],v1)
    if(abs(angle)>(math.pi/4.0)):
      retval[key]= [retval[key][1],retval[key][2],retval[key][3],retval[key][0]]
    v1= np.array(kPoints[retval[key][1]])-np.array(kPoints[retval[key][0]])
    angle= getAngle(sampleVectors[0],v1)
    if(abs(angle)>(math.pi/4.0)):
      lmsg.error('angle: '+ str(math.degrees(angle)) + ' greater than 45 degrees after three girations.')
  return retval

def printFaces(faces):
  for key in faces:
    vertices= faces[key]
    v1= np.array(kPoints[vertices[1]])-np.array(kPoints[vertices[0]])
    v2= np.array(kPoints[vertices[2]])-np.array(kPoints[vertices[0]])
    v= np.cross(v1,v2)
    print key, vertices, v

for name in layerNames:
  faceGroup= facesByLayer[name]
  deckOrientationVectors= [np.array([1,0,0]),np.array([0,1,0])]
  if(re.match("floor.*",name) or re.match("roof.*",name)):
    deckOrientationVectors= [np.array([1,0,0]),np.array([0,0,1])]
  elif(re.match("parapet.*",name) or re.match("bulkhead.*",name)):
    deckOrientationVectors= [np.array([0,0,1]),np.array([1,0,0])]
  elif(re.match("side.*",name) or re.match("middle.*",name)):
    deckOrientationVectors= [np.array([0,0,1]),np.array([0,1,0])]
  facesByLayer[name]= checkFacesOrientation(faceGroup,deckOrientationVectors)




#Block topology
blocks= bte.BlockData()
blocks.name= 'Tour_rampes'

counter= 0
for p in kPoints:
  blocks.appendPoint(id= counter,x= p[0],y= p[1],z= p[2])
  counter+= 1

counter= 0
for key in lines:
  line= lines[key]
  block= bte.BlockRecord(counter,'line',line,[key])
  blocks.appendBlock(block)
  counter+= 1

for name in layerNames:
  fg= facesByLayer[name]
  for key in fg:
    face= fg[key]
    block= bte.BlockRecord(counter,'face',face,labelDict[key])
    blocks.appendBlock(block)
    counter+= 1

fileName= 'xc_model_blocks'
ieData= nmd.XCImportExportData()
ieData.outputFileName= fileName
ieData.problemName= 'gilamontDock'
ieData.blockData= blocks

ieData.writeToXCFile()

