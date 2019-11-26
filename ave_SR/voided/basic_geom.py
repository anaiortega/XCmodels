# -*- coding: utf-8 -*-

from model import predefined_spaces
from model.geometry import grid_model as gm
from postprocess import output_styles as outSty
from postprocess import output_handler as outHndl

#             *** GEOMETRIC model (points, lines, surfaces) - SETS***
FEcase= xc.FEProblem()
preprocessor=FEcase.getPreprocessor
prep=preprocessor   #short name
nodes= prep.getNodeHandler
elements= prep.getElementHandler
elements.dimElem= 3
# Problem type
modelSpace= predefined_spaces.StructuralMechanics3D(nodes) #Defines the
# dimension of the space: nodes by three coordinates (x,y,z) and 
# six DOF for each node (Ux,Uy,Uz,thetaX,thetaY,thetaZ)
sty=outSty.OutputStyle()
out=outHndl.OutputHandler(modelSpace,sty)
cam=out.getCameraParameters()

sty.language=('sp','UTF-8')
# grid model definition (tablero)
gridTabl= gm.GridModel(prep,xListTabl,yListTabl,zListTabl)
# grid model definition (pilas)
gridPil= gm.GridModel(prep,xListPil,yListPil,zListPil)

# Grid geometric entities definition (points, lines, surfaces)
# Points' generation
gridTabl.generatePoints()
gridPil.generatePoints()

#Displacements of the grid points in a range
#syntax: movePointsRange(ijkRange,vDisp)
#        ijkRange: range for the search
#        vDisp: xc vector displacement
# for i in range(1,len(xList)):
#     r= gm.IJKRange((i,0,lastZpos),(i,lastYpos,lastZpos))
#     gridGeom.movePointsRange(r,xc.Vector([0.0,0.0,-trSlope*xList[i]]))


#Scale in X with origin xOrig (fixed axis: X=xOrig) to the points in a range
#Only X coordinate of points is modified in the following way:
#       x_scaled=xOrig+scale*(x_inic-xOrig)
#syntax: scaleCoorXPointsRange(ijkRange,xOrig,scale)
#     ijkRange: range for the search.
#     xOrig: origin X to apply scale (point in axis X=xOrig)
#            are not affected by the transformation 
#     scale: scale to apply to X coordinate
scaleX=(xArranqVoladz-xAlmasAlig[1]-ladoCartab)/(xArranqVoladz-xAlmasAlig[1])
gridTabl.scaleCoorXPointsRange(ijkRange=gm.IJKRange((xListTabl.index(-xArranqVoladz),0,zListTabl.index(zLosInf)),(xListTabl.index(-xAlmasAlig[1]),len(yListTabl)-1,zListTabl.index(zLosInf))),xOrig=-xAlmasAlig[1],scale=scaleX)
gridTabl.scaleCoorXPointsRange(ijkRange=gm.IJKRange((xListTabl.index(xAlmasAlig[1]),0,zListTabl.index(zLosInf)),(xListTabl.index(xArranqVoladz),len(yListTabl)-1,zListTabl.index(zLosInf))),xOrig=xAlmasAlig[1],scale=scaleX)

scaleX=(xArranqVoladz-xAlmasAlig[1]-2*ladoCartab/3.)/(xArranqVoladz-xAlmasAlig[1])
gridTabl.scaleCoorXPointsRange(ijkRange=gm.IJKRange((xListTabl.index(-xArranqVoladz),0,zListTabl.index(zinterm1)),(xListTabl.index(-xAlmasAlig[1]),len(yListTabl)-1,zListTabl.index(zinterm1))),xOrig=-xAlmasAlig[1],scale=scaleX)
gridTabl.scaleCoorXPointsRange(ijkRange=gm.IJKRange((xListTabl.index(xAlmasAlig[1]),0,zListTabl.index(zinterm1)),(xListTabl.index(xArranqVoladz),len(yListTabl)-1,zListTabl.index(zinterm1))),xOrig=xAlmasAlig[1],scale=scaleX)

scaleX=(xArranqVoladz-xAlmasAlig[1]-ladoCartab/3.)/(xArranqVoladz-xAlmasAlig[1])
gridTabl.scaleCoorXPointsRange(ijkRange=gm.IJKRange((xListTabl.index(-xArranqVoladz),0,zListTabl.index(zriostrEstr)),(xListTabl.index(-xAlmasAlig[1]),len(yListTabl)-1,zListTabl.index(zriostrEstr))),xOrig=-xAlmasAlig[1],scale=scaleX)
gridTabl.scaleCoorXPointsRange(ijkRange=gm.IJKRange((xListTabl.index(xAlmasAlig[1]),0,zListTabl.index(zriostrEstr)),(xListTabl.index(xArranqVoladz),len(yListTabl)-1,zListTabl.index(zriostrEstr))),xOrig=xAlmasAlig[1],scale=scaleX)



#Slope (in X direction, Y direction or both) the grid points in a range
#syntax: slopePointsRange(ijkRange,slopeX,xZeroSlope,slopeY,yZeroSlope)
#     ijkRange: range for the search.
#     slopeX: slope in X direction, expressed as deltaZ/deltaX 
#                       (defaults to 0 = no slope applied)
#     xZeroSlope: coordinate X of the "rotation axis".
#     slopeY: slope in Y direction, expressed as deltaZ/deltaY)
#                       (defaults to 0 = no slope applied)
#     yZeroSlope: coordinate Y of the "rotation axis".
gridTabl.slopePointsRange(ijkRange=gm.IJKRange((xListTabl.index(-xBordeVoladz),0,zListTabl.index(zArrVoladz)),(xListTabl.index(-xArranqVoladz),len(yListTabl)-1,zListTabl.index(zArrVoladz))),slopeX=-(maxCantoVoladz/2.-minCantoVoladz/2.)/anchVoladz,xZeroSlope=-xArranqVoladz)

gridTabl.slopePointsRange(ijkRange=gm.IJKRange((xListTabl.index(xArranqVoladz),0,zListTabl.index(zArrVoladz)),(xListTabl.index(xBordeVoladz),len(yListTabl)-1,zListTabl.index(zArrVoladz))),slopeX=(maxCantoVoladz/2.-minCantoVoladz/2.)/anchVoladz,xZeroSlope=xArranqVoladz)
