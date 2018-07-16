# -*- coding: utf-8 -*-

from model import predefined_spaces
from model.geometry import grid_model as gm
from model.geometry import geom_utils as gut

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

# grid model definition
gridGeom= gm.GridModel(prep,xList,yList,zList)

# Grid geometric entities definition (points, lines, surfaces)
# Points' generation
gridGeom.generatePoints()



#Scale in X with origin xOrig (fixed axis: X=xOrig) to the points in a range
#Only X coordinate of points is modified in the following way:
#       x_scaled=xOrig+scale*(x_inic-xOrig)
#syntax: scaleCoorXPointsRange(ijkRange,xOrig,scale)
#     ijkRange: range for the search.
#     xOrig: origin X to apply scale (point in axis X=xOrig)
#            are not affected by the transformation 
#     scale: scale to apply to X coordinate
scaleX=(xArranqVoladz-xAlig2-ladoCartab)/(xArranqVoladz-xAlig2)
gridGeom.scaleCoorXPointsRange(ijkRange=gm.IJKRange((xList.index(-xArranqVoladz),0,zList.index(zLosInf)),(xList.index(-xAlig2),lastYpos,zList.index(zLosInf))),xOrig=-xAlig2,scale=scaleX)
gridGeom.scaleCoorXPointsRange(ijkRange=gm.IJKRange((xList.index(xAlig2),0,zList.index(zLosInf)),(xList.index(xArranqVoladz),lastYpos,zList.index(zLosInf))),xOrig=xAlig2,scale=scaleX)

scaleX=(xArranqVoladz-xAlig2-2*ladoCartab/3.)/(xArranqVoladz-xAlig2)
gridGeom.scaleCoorXPointsRange(ijkRange=gm.IJKRange((xList.index(-xArranqVoladz),0,zList.index(zinterm1)),(xList.index(-xAlig2),lastYpos,zList.index(zinterm1))),xOrig=-xAlig2,scale=scaleX)
gridGeom.scaleCoorXPointsRange(ijkRange=gm.IJKRange((xList.index(xAlig2),0,zList.index(zinterm1)),(xList.index(xArranqVoladz),lastYpos,zList.index(zinterm1))),xOrig=xAlig2,scale=scaleX)

scaleX=(xArranqVoladz-xAlig2-ladoCartab/3.)/(xArranqVoladz-xAlig2)
gridGeom.scaleCoorXPointsRange(ijkRange=gm.IJKRange((xList.index(-xArranqVoladz),0,zList.index(zriostrEstr)),(xList.index(-xAlig2),lastYpos,zList.index(zriostrEstr))),xOrig=-xAlig2,scale=scaleX)
gridGeom.scaleCoorXPointsRange(ijkRange=gm.IJKRange((xList.index(xAlig2),0,zList.index(zriostrEstr)),(xList.index(xArranqVoladz),lastYpos,zList.index(zriostrEstr))),xOrig=xAlig2,scale=scaleX)



#Slope (in X direction, Y direction or both) the grid points in a range
#syntax: slopePointsRange(ijkRange,slopeX,xZeroSlope,slopeY,yZeroSlope)
#     ijkRange: range for the search.
#     slopeX: slope in X direction, expressed as deltaZ/deltaX 
#                       (defaults to 0 = no slope applied)
#     xZeroSlope: coordinate X of the "rotation axis".
#     slopeY: slope in Y direction, expressed as deltaZ/deltaY)
#                       (defaults to 0 = no slope applied)
#     yZeroSlope: coordinate Y of the "rotation axis".
gridGeom.slopePointsRange(ijkRange=gm.IJKRange((xList.index(-xBordeVoladz),0,zList.index(zArrVoladz)),(xList.index(-xArranqVoladz),lastYpos,zList.index(zArrVoladz))),slopeX=-(maxCantoVoladz/2.-minCantoVoladz/2.)/anchVoladz,xZeroSlope=-xArranqVoladz)

gridGeom.slopePointsRange(ijkRange=gm.IJKRange((xList.index(xArranqVoladz),0,zList.index(zArrVoladz)),(xList.index(xBordeVoladz),lastYpos,zList.index(zArrVoladz))),slopeX=(maxCantoVoladz/2.-minCantoVoladz/2.)/anchVoladz,xZeroSlope=xArranqVoladz)

gridGeom.slopePointsRange(ijkRange=gm.IJKRange((0,0,zList.index(zLosInf)),(lastXpos,lastYpos,zList.index(zLosSup))),slopeX=Xslope,xZeroSlope=0) #peralte

#Displacements of the grid points in a range
#syntax: movePointsRange(ijkRange,vDisp)
#        ijkRange: range for the search
#        vDisp: xc vector displacement
# for i in range(1,len(xList)):
#     r= gm.IJKRange((i,0,lastZpos),(i,lastYpos,lastZpos))
#     gridGeom.movePointsRange(r,xc.Vector([0.0,0.0,-trSlope*xList[i]]))
r=gut.def_rg_cooLim(XYZLists,XLosa,Yvano2,(-hTotPilas,zLosSup))
gridGeom.movePointsRange(r,xc.Vector([-despCurv,0.0,0]))

r=gut.def_rg_cooLim(XYZLists,XLosa,(yminRiostrP1,yminRiostrP1),(-hTotPilas,zLosSup))
gridGeom.movePointsRange(r,xc.Vector([-despCurv/LvanosExtr*yminRiostrP1,0.0,0]))
r=gut.def_rg_cooLim(XYZLists,XLosa,(ymaxRiostrP2,ymaxRiostrP2),(-hTotPilas,zLosSup))
gridGeom.movePointsRange(r,xc.Vector([-despCurv/LvanosExtr*yminRiostrP1,0.0,0]))
