# -*- coding: utf-8 -*-
from __future__ import division
import math
from scipy.spatial.distance import cdist
import numpy as np
from import_export import NeutralMeshDescription as nmd
from miscUtils import LogMessages as lmsg
from import_export import DxfReader
import re

layerNamesToImport= ['floor.*','middle.*','bulkhead.*','roof.*','parapet.*','side.*']

def getRelativeCoo(pt):
  return [pt[0],pt[1],pt[2]] #No modification.

dxfImport= DxfReader.DXFImport("rampe_quai_2.dxf",layerNamesToImport,getRelativeCoo, threshold= 0.1,importLines= False)
#dxfImport= DxfReader.DXFImport("rr.dxf",layerNamesToImport,getRelativeCoo, threshold= 0.1)

print dxfImport.layersToImport
'''
print 'kPoints= ', len(dxfImport.kPoints)
print 'points= ', len(dxfImport.points)
print 'lines= ', len(dxfImport.lines)
print 'polylines= ', len(dxfImport.polylines)
#Get faces
for name in dxfImport.layersToImport:
  print name
  print dxfImport.facesByLayer[name]
'''

#Orientation
# supportOrientationVector= np.array([0,0,1])
# for key in dxfImport.lines:
#   vertices= dxfImport.lines[key]
#   v= np.array(kPoints[vertices[1]])-np.array(kPoints[vertices[0]])
#   dotProd= np.dot(v,supportOrientationVector)
#   if(dotProd<0):
#     lines[key]= list(reversed(vertices))
#   #print key, vertices, v, dotProd

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
  kPoints= dxfImport.kPoints
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
      lmsg.warning('angle: '+ str(math.degrees(angle)) + ' greater than 45 degrees after three rotations.')
  return retval

def printFaces(faces):
  for key in faces:
    vertices= faces[key]
    v1= np.array(kPoints[vertices[1]])-np.array(kPoints[vertices[0]])
    v2= np.array(kPoints[vertices[2]])-np.array(kPoints[vertices[0]])
    v= np.cross(v1,v2)
    print key, vertices, v

for name in dxfImport.layersToImport:
  faceGroup= dxfImport.facesByLayer[name]
  deckOrientationVectors= [np.array([1,0,0]),np.array([0,1,0])]
  if(re.match("floor.*",name) or re.match("roof.*",name)):
    deckOrientationVectors= [np.array([1,0,0]),np.array([0,0,1])]
  elif(re.match("parapet.*",name) or re.match("bulkhead.*",name)):
    deckOrientationVectors= [np.array([0,0,1]),np.array([1,0,0])]
  elif(re.match("side.*",name) or re.match("middle.*",name)):
    deckOrientationVectors= [np.array([0,0,1]),np.array([0,1,0])]
  dxfImport.facesByLayer[name]= checkFacesOrientation(faceGroup,deckOrientationVectors)




#Block topology
blocks= dxfImport.exportBlockTopology('Tour_ramps')

fileName= 'xc_model_blocks'
ieData= nmd.XCImportExportData()
ieData.outputFileName= fileName
ieData.problemName= 'tourRamps'
ieData.blockData= blocks

ieData.writeToXCFile()

