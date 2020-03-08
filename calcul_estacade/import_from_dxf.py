# -*- coding: utf-8 -*-
from __future__ import division
import math
import dxfgrabber
from scipy.spatial.distance import cdist
import numpy as np
import re
from import_export import block_topology_entities as bte
from import_export import neutral_mesh_description as nmd


dxf= dxfgrabber.readfile("3d_estacade_rev01.dxf")
layerstoimport= ['dock.*','deck.*','P.*','T.*','parapet.*','footings','bearings','springs']

def layerToImport(layerName):
  for name in layerstoimport:
    if(re.match(name,layerName)):
      return True
  return False

def getRelativeCoo(pt):
  return [pt[0],pt[1]+725,pt[2]-440.936]
 
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
deckFaces= {}
dockFaces= {}
parapetFaces= {}
labelDict= {}
for obj in dxf.entities:
  type= obj.dxftype
  layerName= obj.layer
  if(layerToImport(layerName)):
    if(type == '3DFACE'):
      vertices= []
      for pt in obj.points:
        p= getRelativeCoo(pt)
        idx= getIndexNearestPoint(p,kPoints)
        vertices.append(idx)
      #print layerName, obj.handle
      labelDict[obj.handle]= [layerName]
      if(re.match('deck.*',layerName)):
        deckFaces[obj.handle]= vertices
      elif(re.match('dock.*',layerName)):
        dockFaces[obj.handle]= vertices
      elif(re.match('parapet.*',layerName)):
        parapetFaces[obj.handle]= vertices

print 'deckFaces= ', len(deckFaces)
print 'dockFaces= ', len(dockFaces)
print 'parapetFaces= ', len(parapetFaces)

#Orientation
supportOrientationVector= np.array([0,0,1])
for key in lines:
  vertices= lines[key]
  v= np.array(kPoints[vertices[1]])-np.array(kPoints[vertices[0]])
  dotProd= np.dot(v,supportOrientationVector)
  if(dotProd<0):
    lines[key]= list(reversed(vertices))
  #print key, vertices, v, dotProd

def checkFacesOrientation(faces,sampleVectors):
  retval= {}
  for key in faces:
    vertices= faces[key]
    #orientation of local Z vector.
    v1= np.array(kPoints[vertices[1]])-np.array(kPoints[vertices[0]])
    v2= np.array(kPoints[vertices[2]])-np.array(kPoints[vertices[0]])
    v= np.cross(v1,v2)
    dotProd= np.dot(v,sampleVectors[1])
    if(dotProd>=0):
      retval[key]= vertices
    else:  
      retval[key]= list(reversed(vertices))
    #orientation of local X vector.
    v1= np.array(kPoints[retval[key][1]])-np.array(kPoints[retval[key][0]])
    cosine= np.dot(v,sampleVectors[0])/np.linalg.norm(v)/np.linalg.norm(sampleVectors[0]) #Cosine of the angle.
    angle= np.arccos(np.clip(cosine, -1, 1))
    if(abs(angle)>math.pi/4.0):
      retval[key]= [retval[key][1],retval[key][2],retval[key][3],retval[key][0]]
  return retval

def printFaces(faces):
  for key in faces:
    vertices= faces[key]
    v1= np.array(kPoints[vertices[1]])-np.array(kPoints[vertices[0]])
    v2= np.array(kPoints[vertices[2]])-np.array(kPoints[vertices[0]])
    v= np.cross(v1,v2)
    print key, vertices, v

  
deckOrientationVectors= [np.array([0,1,0]),np.array([0,0,1])] #[X,Z]
deckFaces= checkFacesOrientation(deckFaces,deckOrientationVectors)
#printFaces(deckFaces)
dockOrientationVectors= [np.array([0,1,0]),np.array([-1,0,0])] #[X,Z]
dockFaces= checkFacesOrientation(dockFaces,dockOrientationVectors)
#printFaces(dockFaces)
parapetOrientationVectors= [np.array([0,1,0]),np.array([1,0,0])] #[X,Z]
parapetFaces= checkFacesOrientation(parapetFaces,parapetOrientationVectors)
#printFaces(parapetFaces)




#Block topology
blocks= bte.BlockData()
blocks.name= 'Gilamont_dock'

counter= 0
for p in kPoints:
  blocks.appendPoint(id= counter,x= p[0],y= p[1],z= p[2])
  counter+= 1
faceGroups= [deckFaces,dockFaces,parapetFaces]

counter= 0
for key in lines:
  line= lines[key]
  block= bte.BlockRecord(counter,'line',line,[key])
  blocks.appendBlock(block)
  counter+= 1

for fg in faceGroups:
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

bearingPositions= []
footingPositions= []
for key in points:
  layerName, vertex= points[key]
  position= kPoints[vertex[0]]
  if(layerName=='bearings'):
    bearingPositions.append(position)
  elif(layerName=='footings'):
    footingPositions.append(position)

    
ieData.outputFile.write('bearingPositions= '+str(bearingPositions)+'\n')
ieData.outputFile.write('footingPositions= '+str(footingPositions)+'\n')

springKeyPoints= set()
for key in polylines:
  if(key=='springs'):
    springKeyPoints= polylines[key]

ieData.outputFile.write('springKeyPoints= '+str(springKeyPoints)+'\n')

ieData.outputFile.close()

