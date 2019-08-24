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

#Displacements of the grid points in a range
#syntax: movePointsRange(ijkRange,vDisp)
#        ijkRange: range for the search
#        vDisp: xc vector displacement
if Lvoladzi >0:
    r= gut.def_rg_cooLim(XYZLists,Xaleti,(yVoladz,yVoladz),(zArrVoladz,zArrVoladz))
    gridGeom.movePointsRange(r,xc.Vector([0.0,0.0,(Hmaxvoladzi-Hminvoladzi)]))
    r= gut.def_rg_cooLim(XYZLists,Xaleti,(yVoladz,yVoladz),(zMur,zMur))
    gridGeom.movePointsRange(r,xc.Vector([0.0,0.0,(Hmaxvoladzi-Hminvoladzi)/Hmaxvoladzi*hMuret]))

if Lvoladzd >0:
    r= gut.def_rg_cooLim(XYZLists,Xaletd,(yVoladz,yVoladz),(zArrVoladz,zArrVoladz))
    gridGeom.movePointsRange(r,xc.Vector([0.0,0.0,(Hmaxvoladzd-Hminvoladzd)]))
    r= gut.def_rg_cooLim(XYZLists,Xaletd,(yVoladz,yVoladz),(zMur,zMur))
    gridGeom.movePointsRange(r,xc.Vector([0.0,0.0,(Hmaxvoladzd-Hminvoladzd)/Hmaxvoladzd*hMuret]))




#Slope (in X direction, Y direction or both) the grid points in a range
#syntax: slopePointsRange(ijkRange,slopeX,xZeroSlope,slopeY,yZeroSlope)
#     ijkRange: range for the search.
#     slopeX: slope in X direction, expressed as deltaZ/deltaX 
#                       (defaults to 0 = no slope applied)
#     xZeroSlope: coordinate X of the "rotation axis".
#     slopeY: slope in Y direction, expressed as deltaZ/deltaY)
#                       (defaults to 0 = no slope applied)
#     yZeroSlope: coordinate Y of the "rotation axis".
if Lvoladzi >0:
    r=gut.def_rg_cooLim(XYZLists,Xmurestr,(yPuntera,yVoladz),(zMur,zAlet))
    gridGeom.slopePointsRange(ijkRange=r,slopeX=(hMurd-hMuri)/anchoEstr,xZeroSlope=xAletaI)
else:
    r=gut.def_rg_cooLim(XYZLists,Xmurestr,(yPuntera,yVoladz),(zMur,zAlet))
    gridGeom.slopePointsRange(ijkRange=r,slopeX=(hMuri-hMurd)/anchoEstr,xZeroSlope=xAletaD)
    
if angMuri <>0:
    r=gut.def_rg_cooLim(XYZLists,(xAletaI,xAletaI),(yList[0],yList[-1]),(zList[0],zList[-1]))
    gridGeom.rotPntsZAxis(ijkRange=r,angle=angMuri,xyRotCent=[xAletaI,yMurEstr])

if angMurd <>0:
    print 'angmd=', angMurd
    r=gut.def_rg_cooLim(XYZLists,(xAletaD,xAletaD),(yList[0],yList[-1]),(zList[0],zList[-1]))
    gridGeom.rotPntsZAxis(ijkRange=r,angle=angMurd,xyRotCent=[xAletaD,yMurEstr])

