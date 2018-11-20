# -*- coding: utf-8 -*-
from __future__ import division

'''Verification test to check the losses of prestress force due to
elastic shortening of concrete.
The test calculates the loss of stress in a tendon due to elastic 
shortening of concrete caused by the post-tensioning of the subsequent 
tendon. Some data are taken from example 4-1 of Baderul course
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
from scipy.spatial import distance
import math
import xc_base
import geom
import xc
from materials import typical_materials as tm
from materials.prestressing import prestressed_concrete as presconc
from rough_calculations import ng_prestressed_concrete as ng_presconc
from model import predefined_spaces
from solution import predefined_solutions

#Geometry
span=20      #span of the beam [m]
hBeam=1.6295 #height of the cross-section [m]
wBeam=0.2596 #width of the cross-section [m]
Abeam=hBeam*wBeam   #cross-section area of the beam[m2]
Iybeam=1/12.*wBeam*hBeam**3 #moment of inertia of the beam cross-section [m4]
Izbeam=1/12.*hBeam*wBeam**3 #moment of inertia of the beam cross-section [m4]

Abeam=0.423  #cross-section area of the beam[m2]
Ibeam=9.36e-2 #moment of inertia of the beam cross-section [m4]


#Parabola
eEnds=0           #eccentricity of cables at both ends of the beam
eMidspan=-0.558   #eccentricity of cables at midspan [m]

#Material properties
Ec=2.6e10      #modulus of elasticity of concrete [Pa]
Ep=Ec*7.5    #modulus of elasticity of prestressing steel
nuc=0.2      #coefficient of Poisson of concrete
densc= 2500   #specific mass of concrete (kg/m3)

fy= 1171e6 # Yield stress of the steel expressed in Pa.
Aps=2.85e-3/2.0  #area of tendon cross-section [m2]
#Prestress
fpi=1239e6/2.0       #initial stress in the tendon [Pa]
mu=0.20               #friction coefficient
k=0.0020              #wobble coefficient [1/m]
anc_slip=6e-3         #anchorage slip [m]
#Loads
Wsw=Abeam*densc*9.81        #uniform load on beam [N/m]


#Approximation of the loss of prestress due to shortening of concrete
#  at midspan
Mi_midsp=Wsw*span**2/8. #Moment in the midspan section [Nm]
rg_loss_midsp=ng_presconc.loss_elastic_shortening_concr(Abeam,Ibeam,Ec,Ep,Aps,abs(eMidspan),fpi,Mi_midsp)
# at the ends
Mi_ends=0.0
rg_loss_ends=ng_presconc.loss_elastic_shortening_concr(Abeam,Ibeam,Ec,Ep,Aps,abs(eEnds),fpi,Mi_ends)

# Loss of prestress: the bending moment and the tendon eccentricity varie along the span; an average stress in concrete is used

rg_loss_avg=(rg_loss_midsp+rg_loss_ends)/2.0  #[Pa]

print 'rough loss average F=', rg_loss_avg*Aps*1e-3

# XC model of the beam
# Problem type
FEcase= xc.FEProblem()
preprocessor=  FEcase.getPreprocessor
nodes= preprocessor.getNodeHandler
modelSpace= predefined_spaces.StructuralMechanics3D(nodes)
nodes.defaultTag= 1 #First node number.

# BEAM
beamSet=preprocessor.getSets.defSet('beamSet')
#Nodes
nnodesBeam=91   #number of nodes to create the beam elements
XdistNod=span/(nnodesBeam-1)
for i in range(nnodesBeam):
    n=nodes.newNodeXYZ(i*XdistNod,0,0)
    beamSet.getNodes.append(n)

#Geometric sections
from materials.sections import section_properties as sectpr
geomSectBeam=sectpr.RectangularSection(name='geomSectBeam',b=wBeam,h=hBeam)

# Material definition
concrete=tm.MaterialData(name='concrete',E=Ec,nu=nuc,rho=densc)
beamMat=tm.BeamMaterialData(name= 'beamMat', section=geomSectBeam, material=concrete)
beamMat.setupElasticShear3DSection(preprocessor)

#Beam elements
linCooTr=modelSpace.newLinearCrdTransf(trfName='linCooTr',xzVector=xc.Vector([0,-1,0])) 

elements= preprocessor.getElementHandler
elements.defaultTransformation= 'linCooTr'
elements.dimElem=preprocessor.getNodeHandler.dimSpace
elements.defaultMaterial='beamMat'
elements.defaultTag= 1
for nn in range(1,nnodesBeam):
    elem= elements.newElement("ElasticBeam3d",xc.ID([nn,nn+1]))
    beamSet.getElements.append(elem)

#Boundary conditions
modelSpace.fixNode000_FFF(1)
#modelSpace.fixNode(DOFpattern='F00_FFF',nodeTag=nnodesBeam)
modelSpace.fixNode000_FFF(nnodesBeam)

#TENDONS
#Material
prestressingSteel= tm.defSteel02(preprocessor=preprocessor, name="prestressingSteel",E=Ep,fy=fy,b=0.001,initialStress=fpi)

#Geometry
n_points_rough=5    #number of points provided to the interpolation algorithm
n_points_fine=91   #number of points interpolated

#Exact parabola
from model.geometry import geom_utils
a,b,c=geom_utils.fit_parabola(np.array([0,span/2.0,span]), np.array([eEnds,eMidspan,eEnds]))
x_parab_rough,y_parab_rough,z_parab_rough=geom_utils.eq_points_parabola(0,span,n_points_rough,a,b,c,0)
#Tendon1 definition, layout
tendon1=presconc.PrestressTendon([])
tendon1.roughCoordMtr=np.array([x_parab_rough,y_parab_rough,z_parab_rough])
#Interpolated 3D spline 
tendon1.pntsInterpTendon(n_points_fine,1)
#Plot
#tendon1.plot2D(XaxisValues='X',fileName='plot.png',symbolRougPoints='r*',symbolFinePoints='g+',symbolTendon='g-')

corCooTr=modelSpace.newLinearCrdTransf(trfName='corCooTr',xzVector=xc.Vector([0,-1,0]))
nodes.defaultTag= 101
tendon1Set=tendon1.creaTendonElements(preprocessor=preprocessor,materialName='prestressingSteel',elemTypeName='Truss',crdTransfName='corCooT',areaTendon=Aps,setName='tendon1Set')

#Tendon2 definition, layout
tendon2=presconc.PrestressTendon([])
tendon2.roughCoordMtr=np.array([x_parab_rough,y_parab_rough,z_parab_rough])
#Interpolated 3D spline 
tendon2.pntsInterpTendon(n_points_fine,1)
#Plot
#tendon2.plot2D(XaxisValues='X',fileName='plot.png',symbolRougPoints='r*',symbolFinePoints='g+',symbolTendon='g-')


nodes.defaultTag= 201
tendon2Set=tendon2.creaTendonElements(preprocessor=preprocessor,materialName='prestressingSteel',elemTypeName='Truss',crdTransfName='corCooT',areaTendon=Aps,setName='tendon2Set')

overallSet=preprocessor.getSets.getSet('total')

#Plot elements
# from postprocess.xcVtk.FE_model import vtk_FE_graphic
# defDisplay= vtk_FE_graphic.RecordDefDisplayEF()
# defDisplay.FEmeshGraphic(xcSet=tendonSet,caption='Prestressing tendon',cameraParameters= vtk_graphic_base.CameraParameters('YPos'),defFScale=1.0)
# defDisplay.FEmeshGraphic(xcSet=beamSet,caption='Beam',cameraParameters= vtk_graphic_base.CameraParameters('YPos'),defFScale=1.0)

# Connection between cable and beam
# gluedDOFs= [0,1,2,3,4,5]
# tendonSet_nod=tendonSet.getNodes
# for n in tendonSet_nod:
#     print 'node',n.tag,'x=',n.getInitialPos3d.x
#     nearElem=beamSet.getElements.getNearestElement(n.getCurrentPos3d(0.0))
#     modelSpace.constraints.newGlueNodeToElement(n,nearElem,xc.ID(gluedDOFs))

# Connection between tendon 1 and beam
gluedDOFs= [0,1,2,3,4,5]
for nn in range(nnodesBeam):
    modelSpace.constraints.newEqualDOF(nn+1,nn+101,xc.ID(gluedDOFs))

# Connection between tendon 2and beam
gluedDOFs= [0,1,2,3,4,5]
for nn in range(nnodesBeam):
    modelSpace.constraints.newEqualDOF(nn+1,nn+201,xc.ID(gluedDOFs))

# losses in tendon 1
tendon1.calcLossFriction(coefFric=mu,k=k,sigmaP0_extr1=fpi,sigmaP0_extr2=0.0)
tendon1.calcLossAnchor(Ep=Ep,anc_slip_extr1=anc_slip, anc_slip_extr2=0.0)
# initialize stress in tendon 1 elements with the stresses calculated after
# friction and anchorage slip losses:
tendon1.applyStressToElems(stressMtr=tendon1.stressAfterLossAnch)

# losses in tendon 2
tendon2.calcLossFriction(coefFric=mu,k=k,sigmaP0_extr1=fpi,sigmaP0_extr2=0.0)
tendon2.calcLossAnchor(Ep=Ep,anc_slip_extr1=anc_slip, anc_slip_extr2=0.0)
# initialize stress in tendon 1 elements with the stresses calculated after
# friction and anchorage slip losses:
tendon2.applyStressToElems(stressMtr=tendon2.stressAfterLossAnch)


# Turn off tendon 1 
tendon1Set.killElements()
mesh=FEcase.getDomain.getMesh
mesh.setDeadSRF(0.0)  #Assigns Stress Reduction Factor for element deactivation.
mesh.freezeDeadNodes("block1") # Restrain movement of inactive nodes.

# Turn off tendon 2 
tendon2Set.killElements()
mesh=FEcase.getDomain.getMesh
mesh.setDeadSRF(0.0)  #Assigns Stress Reduction Factor for element deactivation.
mesh.freezeDeadNodes("block2") # Restrain movement of inactive nodes.

# Loads definition
cargas= preprocessor.getLoadHandler

casos= cargas.getLoadPatterns

#Load modulation.
ts= casos.newTimeSeries("constant_ts","ts")
casos.currentTimeSeries= "ts"
#Load case definition
lp0= casos.newLoadPattern("default","0")
casos.currentLoadPattern='0'
#We add the load case to domain.
casos.addToDomain('0')


# Phase 1: prestressing of tendon 1
# Solution procedure
analisis= predefined_solutions.simple_static_linear(FEcase)
analOk= analisis.analyze(1)

tendon1Set.aliveElements()
mesh.meltAliveNodes("block1") # Reactivate inactive nodes.
loadVector=xc.Vector([0,0,-1])
for e in beamSet.getElements:
    e.vector3dUniformLoadGlobal(loadVector)

analOk= analisis.analyze(1)

from postprocess.xcVtk.FE_model import quick_graphics as QGrph
lcs=QGrph.QuickGraphics(FEcase)
lcs.displayDispRot(itemToDisp='uZ',setToDisplay=beamSet,fConvUnits=1e3,unitDescription='beam [mm]. Phase 1: prestressing of tendon 1',vtk_graphic_base.CameraParameters("YNeg",1),fileName='twoTendonsUz01.png',defFScale=2e2)

lcs.displayIntForcDiag(itemToDisp='Mz',setToDisplay=beamSet,fConvUnits=1e-3,scaleFactor=-2e-2,unitDescription='beam [kNm]. Phase 1: prestressing of tendon 1',vtk_graphic_base.CameraParameters("YNeg",1),fileName='twoTendonsMz01.png',defFScale=1)

lcs.displayIntForcDiag(itemToDisp='N',setToDisplay=tendon1Set,fConvUnits=1e-3,scaleFactor=1e-2,unitDescription='tendon 1 [kN]. Phase 1: prestressing of tendon 1', vtk_graphic_base.CameraParameters('XYZNeg',1),fileName='twoTendons_t1_N01.png',defFScale=1)

# Phase 2: self-weight
#Add uniform load on beam elems to current load pattern
loadVector=xc.Vector([0,0,-Wsw])
for e in beamSet.getElements:
    e.vector3dUniformLoadGlobal(loadVector)
analOk= analisis.analyze(1)



lcs.displayDispRot(itemToDisp='uZ',setToDisplay=beamSet,fConvUnits=1e3,unitDescription='beam [mm]. Phase 2: self-weight',vtk_graphic_base.CameraParameters("YNeg",1),fileName='twoTendonsUz02.png',defFScale=2e2)

lcs.displayIntForcDiag(itemToDisp='Mz',setToDisplay=beamSet,fConvUnits=1e-3,scaleFactor=-0.05,unitDescription='beam [kNm]. Phase 2: self-weight',vtk_graphic_base.CameraParameters("YNeg",1),fileName='twoTendonsMz02.png',defFScale=1)

lcs.displayIntForcDiag(itemToDisp='N',setToDisplay=tendon1Set,fConvUnits=1e-3,scaleFactor=1e-2,unitDescription='tendon 1 [kN]. Phase 2: self-weight', vtk_graphic_base.CameraParameters('XYZNeg',1),fileName='twoTendons_t1_N02.png',defFScale=1)

# Phase 3: revive tendon 2
tendon2Set.aliveElements()
mesh.meltAliveNodes("block2") # Reactivate inactive nodes.
analOk= analisis.analyze(1)

lcs.displayDispRot(itemToDisp='uZ',setToDisplay=beamSet,fConvUnits=1e3,unitDescription='beam [mm]. Phase 3: prestressing of tendon 2',vtk_graphic_base.CameraParameters("YNeg",1),fileName='twoTendonsUz03.png',defFScale=2e2)

#lcs.displayIntForcDiag(itemToDisp='N',setToDisplay=beamSet,fConvUnits= 1e-2,scaleFactor=1e-3,unitDescription='', vtk_graphic_base.CameraParameters('ZPos',1),fileName=None,defFScale=1)
lcs.displayIntForcDiag(itemToDisp='Mz',setToDisplay=beamSet,fConvUnits=1e-3,scaleFactor=-2e-2,unitDescription='beam [kNm]. Phase 3: prestressing of tendon 2 ',vtk_graphic_base.CameraParameters("YNeg",1),fileName='twoTendonsMz03.png',defFScale=1)

lcs.displayIntForcDiag(itemToDisp='N',setToDisplay=tendon1Set,fConvUnits=1e-3,scaleFactor=1e-2,unitDescription='tendon 1 [kN]. Phase 3: prestressing of tendon 2', vtk_graphic_base.CameraParameters('XYZNeg',1),fileName='twoTendons_t1_N03.png',defFScale=1)
lcs.displayIntForcDiag(itemToDisp='N',setToDisplay=tendon2Set,fConvUnits=1e-3,scaleFactor=1e-2,unitDescription='tendon 2 [kN]. Phase 3: prestressing of tendon 2', vtk_graphic_base.CameraParameters('XYZNeg',1),fileName='twoTendons_t2_N03.png',defFScale=1)


#delta= nodes.getNode(nnodesBeam).getDisp[0]

'''
for nn in range(nnodesBeam):
    print 'displacement X', nodes.getNode(nn+1).getDisp[0],',',nodes.getNode(nn+101).getDisp[0]

print 'loss_aprox=',rg_loss_avg*1e-6
print 'delta=', delta
for e in tendonSet.getElements:
    print (fpi-e.getN()/Aps)*1e-6
for e in beamSet.getElements:
    # print e.getN*1e-3
    print e.getMy1*1e-3
    # print e.getMz1*1e-6
    # print e.getMy2*1e-6
    # print e.getMz2*1e-6
'''
# nodes.calculateNodalReactions(True,1e-6)
# R1= nodes.getNode(1).getReaction[1]
# R2= nodes.getNode(nnodesBeam).getReaction[1]

# print R1
# print R2
