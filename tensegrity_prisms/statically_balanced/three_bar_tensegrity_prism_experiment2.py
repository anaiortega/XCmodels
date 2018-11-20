# -*- coding: utf-8 -*-
from __future__ import division

__author__= "Ana Ortega (AO_O) and Luis C. Pérez Tato (LCPT)"
__copyright__= "Copyright 2017, AO_O and LCPT"
__license__= "GPL"
__version__= "3.0"
__email__= "ana.ortega@ciccp.es l.pereztato@ciccp.es" 

import os
import xc_base
import geom
import xc
from model.geometry import tensegrity
import math


#FE problem
#Data
#    geometry
nSidPol=3     # number of sides of the regular n-polygon
rBasCirc=1.0 # radius of the base circle circunscribing the n-polygon
rTopCirc=1.0 # radius of the top circle circunscribing the n-polygon
Hprism=2     # height of the prism [m]
#    materials
#struts material stiffness= EA=100 [N]
Estruts=1e5    # elastic modulus [Pa]
strutArea=1e-3 # area [m2]
# Gstruts=79.3e9   # shear modulus [Pa] 
# rhoStruts=7850   # mass density [kg/m3]
# fyStruts=200e6   # yield strength [Pa]
# nuStruts=0.3     # Poisson's coefficient
# strutRint=50e-3-10.95e-3  #internal radius [m]
# strutRext=50e-3           #external radius [m]

#diagonal cables material stiffness= sqrt(3) [N/m]
EdiagCable=1e5      #elastic modulus
diagArea=math.sqrt(3)*1e-5
rhoDiagCable=0.0  # effective self weight (gravity component of weight per
                  #volume transverse to the cable)
sigmaPrestrDiagCable=1e7 #final prestress [N]
sigmaPrestrDiagCableInit=1e7#initial prestress [N]
#saddle cables material tiffness= 1 [N/m]
EsaddCable=1e5  #elastic modulus
saddArea=1e-5
rhoSaddCable=0.0  # effective self weight (gravity component of weight per
                  #volume transverse to the cable)
sigmaPrestrSaddCable=1e7 #final prestress
sigmaPrestrSaddCableInit=1e7#initial prestress

from model import predefined_spaces

test= xc.FEProblem()
prep=test.getPreprocessor   
points= prep.getMultiBlockTopology.getPoints
lines= prep.getMultiBlockTopology.getLines
nodes= prep.getNodeHandler
sets=prep.getSets

# Problem type
modelSpace= predefined_spaces.StructuralMechanics3D(nodes) #Defines the dimension of
                  #the space: nodes by three coordinates (x,y,z) and six
                  #DOF for each node (Ux,Uy,Uz,thetaX,thetaY,thetaZ)

prismGeom=tensegrity.tensegrityPrism(nSidPol=nSidPol,RbaseC=rBasCirc,RtopC=rTopCirc,Hprism=Hprism)
#Joints generation
jointsCCoor=prismGeom.genJointsCoor()
for i in jointsCCoor.index:
    points.newPntIDPos3d(int(float(i[2:])),geom.Pos3d(jointsCCoor.loc[i].X,jointsCCoor.loc[i].Y,jointsCCoor.loc[i].Z))
    
#Lines generation
linsJoints=prismGeom.genLineLinkedJoints()
ljInd=linsJoints.index
#lines to struts
strutSet=prep.getSets.defSet('strutSet')
indStruts=[ljInd[i] for i in range(len(ljInd)) if 'strut' in ljInd[i]]
for i in indStruts:
    l=lines.newLine(linsJoints.loc[i].i_jt,linsJoints.loc[i].j_jt)
    l.nDiv=1   #initialization of number or divisions
    strutSet.getLines.append(l)
#lines to saddle cables
saddSet=prep.getSets.defSet('saddSet')
indSadd=[ljInd[i] for i in range(len(ljInd)) if 'sadd' in ljInd[i]]
for i in indSadd:
    l=lines.newLine(linsJoints.loc[i].i_jt,linsJoints.loc[i].j_jt)
    l.nDiv=1   
    saddSet.getLines.append(l)
#lines to diagonal cables
diagSet=prep.getSets.defSet('diagSet')
indDiag=[ljInd[i] for i in range(len(ljInd)) if 'diag' in ljInd[i]]
for i in indDiag:
    l=lines.newLine(linsJoints.loc[i].i_jt,linsJoints.loc[i].j_jt)
    l.nDiv=1   
    diagSet.getLines.append(l)

# #Sections definition
# from materials.sections import section_properties
# strutSect=section_properties.CircularSection(name='strutSect',Rext=strutRext,Rint=strutRint)

#Materials definition
from materials import typical_materials
from materials import typical_materials
#struts material
strutMat=typical_materials.defElasticMaterial(preprocessor=prep, name="strutMat",E=Estruts)
diagCableMat=typical_materials.defElasticMaterial(preprocessor=prep, name="diagCableMat",E=EdiagCable)
saddCableMat=typical_materials.defElasticMaterial(preprocessor=prep, name="saddCableMat",E=EdiagCable)
#strutMat=typical_materials.defElasticSection3d(preprocessor=prep,name='strutMat',A=strutSect.A(),E=Estruts,G=Gstruts,Iz=strutSect.Iz(),Iy=strutSect.Iy(),J=strutSect.J())
#cables materials
# diagCableMat=typical_materials.defCableMaterial(preprocessor=prep,name='diagCableMat',E=EdiagCable,prestress=sigmaPrestrDiagCableInit,rho=rhoDiagCable)
# saddCableMat=typical_materials.defCableMaterial(preprocessor=prep,name='saddCableMat',E=EdiagCable,prestress=sigmaPrestrSaddCableInit,rho=rhoSaddCable)

# # Plotting of CAD entities
# from postprocess.xcVtk.CAD_model import vtk_CAD_graphic
# defDisplay= vtk_CAD_graphic.RecordDefDisplayCAD()
# totalSet= prep.getSets.getSet('total')
# defDisplay.displayBlocks(xcSet=totalSet,fName= None,caption= 'Model grid')


# Geometric transformations
trfs= prep.getTransfCooHandler
# Coord. trasformation for beam in global X direction
ltStruts= trfs.newLinearCrdTransf3d("ltStruts")
ltStruts.xzVector= xc.Vector([0,-1,0]) #local Z axis of the element
                           # parallel to global -Y 

# Seed element for struts
seedElemHandler= prep.getElementHandler.seedElemHandler
seedElemHandler.defaultMaterial= "strutMat"
#seedElemHandler.defaultTransformation="ltStruts"
seedElemHandler.dimElem= 3
seedElemHandler.defaultTag= 1 
#strutTruss= seedElemHandler.newElement("ElasticBeam3d",xc.ID([0,0]))
strutTruss= seedElemHandler.newElement("Spring",xc.ID([1,2]))
#strutTruss= seedElemHandler.newElement("CorotTruss",xc.ID([1,2]))
strutTruss.area= strutArea
strutSet.genMesh(xc.meshDir.I)
# Seed element for diagonal cables
seedElemHandler= prep.getElementHandler.seedElemHandler
seedElemHandler.defaultMaterial= "diagCableMat"
seedElemHandler.dimElem= 3    # three-dimensional space 
seedElemHandler.defaultTag= 1 
diagTruss= seedElemHandler.newElement("Spring",xc.ID([1,2]))
#diagTruss= seedElemHandler.newElement("CorotTruss",xc.ID([1,2]))
diagTruss.area= diagArea
diagSet.genMesh(xc.meshDir.I)
# Seed element for saddle cables
seedElemHandler= prep.getElementHandler.seedElemHandler
seedElemHandler.defaultMaterial= "saddCableMat"
seedElemHandler.dimElem= 3
seedElemHandler.defaultTag= 1 
saddTruss= seedElemHandler.newElement("Spring",xc.ID([1,2]))
#saddTruss= seedElemHandler.newElement("CorotTruss",xc.ID([1,2]))
saddTruss.area= saddArea
saddSet.genMesh(xc.meshDir.I)


# Constraints
constr= prep.getBoundaryCondHandler
n1=points.get(1).getNode()  #node associated with point 1 
constr.newSPConstraint(n1.tag,0,0.0) # ux=0
constr.newSPConstraint(n1.tag,1,0.0) # uy=0
constr.newSPConstraint(n1.tag,2,0.0) # uz=0
for p in range(2,nSidPol+1):
    n=points.get(p).getNode()
    constr.newSPConstraint(n.tag,2,0.0) # uz=0
# for p in range(2,7):
#     n=points.get(p).getNode()
#     print 'node', n.tag
#     constr.newSPConstraint(n.tag,0,0.0)
#     constr.newSPConstraint(n.tag,1,0.0)
#     constr.newSPConstraint(n.tag,2,0.0) # uz=0

# n1=points.get(nSidPol+1).getNode()  #node associated with point 1 
# constr.newSPConstraint(n1.tag,0,0.0) # ux=0
# constr.newSPConstraint(n1.tag,1,0.0) # uy=0
# constr.newSPConstraint(n1.tag,2,0.0) # uz=0

    
strutSet.fillDownwards()
diagSet.fillDownwards()
saddSet.fillDownwards()

# # Displaying of the mesh
# from postprocess.xcVtk.FE_model import vtk_FE_graphic
# defDisplay= vtk_FE_graphic.RecordDefDisplayEF()
# totalSet= prep.getSets.getSet('total')
# defDisplay.FEmeshGraphic(xcSet=totalSet,caption= 'All elements',cameraParameters= vtk_graphic_base.CameraParameters('XYZPos'))
# defDisplay.FEmeshGraphic(xcSet=strutSet,caption= 'Struts',cameraParameters= vtk_graphic_base.CameraParameters('XYZPos'))
# defDisplay.FEmeshGraphic(xcSet=diagSet,caption= 'Diagonal',cameraParameters= vtk_graphic_base.CameraParameters('XYZPos'))
# defDisplay.FEmeshGraphic(xcSet=saddSet,caption= 'Saddle cables',cameraParameters= vtk_graphic_base.CameraParameters('XYZPos'))
# quit()


from solution import predefined_solutions
# Static solution
analysis= predefined_solutions.simple_static_linear(test)
result= analysis.analyze(1)

# for e in diagSet.getElements:
#     print e.tag
#     e.getMaterial().prestress=sigmaPrestrDiagCable

# for e in saddSet.getElements:
#     print e.tag
#     e.getMaterial().prestress=sigmaPrestrSaddCable

# analisis= predefined_solutions.simple_static_linear(test)
# result= analisis.analyze(1)

#Newton Raphson
# analisis= predefined_solutions.simple_newton_raphson(test)
# result= analisis.analyze(10)

# Nstep= 10  #  apply load in 10 steps
# DInc= 1./Nstep 	#  first load increment


# solu= test.getSoluProc
# solCtrl= solu.getSoluControl
# solModels= solCtrl.getModelWrapperContainer
# sm= solModels.newModelWrapper("sm")
# numberer= sm.newNumberer("default_numberer")
# numberer.useAlgorithm("simple")
# cHandler= sm.newConstraintHandler("plain_handler")
# numberer= sm.newNumberer("default_numberer")
# numberer.useAlgorithm("simple")
# analysisAggregations= solCtrl.getAnalysisAggregationContainer
# analysisAggregation= analysisAggregations.newAnalysisAggregation("analysisAggregation","sm")
# solAlgo= analysisAggregation.newSolutionAlgorithm("newton_raphson_soln_algo")
# ctest= analysisAggregation.newConvergenceTest("norm_unbalance_conv_test")
# ctest.tol= 1e-6
# ctest.maxNumIter= 100
# integ= analysisAggregation.newIntegrator("load_control_integrator",xc.Vector([]))
# integ.dLambda1= DInc
# soe= analysisAggregation.newSystemOfEqn("band_gen_lin_soe")
# solver= soe.newSolver("band_gen_lin_lapack_solver")
# analysis= solu.newAnalysis("static_analysis","analysisAggregation","")
# result= analysis.analyze(Nstep)

nodes.calculateNodalReactions(True,1e-6)

n1=points.get(1).getNode()
n2=points.get(2).getNode()
n3=points.get(3).getNode()
n4=points.get(4).getNode()
n5=points.get(5).getNode()
n6=points.get(6).getNode()
print 'displ. node 1',n1.getDisp[0],n1.getDisp[1],n1.getDisp[2]
print 'displ. node 2',n2.getDisp[0],n2.getDisp[1],n2.getDisp[2]
print 'displ. node 3',n3.getDisp[0],n3.getDisp[1],n3.getDisp[2]
print 'displ. node 4',n4.getDisp[0],n4.getDisp[1],n4.getDisp[2]
print 'displ. node 5',n5.getDisp[0],n5.getDisp[1],n5.getDisp[2]
print 'displ. node 6',n6.getDisp[0],n6.getDisp[1],n6.getDisp[2]


# from postprocess.xcVtk.FE_model import quick_graphics as qg
# lcs=qg.QuickGraphics(test)
# lcs.displayDispRot(itemToDisp='uX')
# quit()

print 'react. node 1',n1.getReaction
print 'react. node 2',n2.getReaction
print 'react. node 3',n3.getReaction
print 'react. node 4',n4.getReaction
print 'react. node 5',n5.getReaction
print 'react. node 6',n6.getReaction

quit()




