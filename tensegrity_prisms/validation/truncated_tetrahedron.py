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
#    materials
#struts material stiffness= EA=100 [N]
Estruts=2.1e5    # elastic modulus [Pa]
strutArea=1 # area [m2]
# Gstruts=79.3e9   # shear modulus [Pa] 
# rhoStruts=7850   # mass density [kg/m3]
# fyStruts=200e6   # yield strength [Pa]
# nuStruts=0.3     # Poisson's coefficient
# strutRint=50e-3-10.95e-3  #internal radius [m]
# strutRext=50e-3           #external radius [m]

#diagonal cables material stiffness= sqrt(3) [N/m]
EdiagCable=2.1e5      #elastic modulus
#diagArea=math.sqrt(3)*1e-5
diagArea=1
rhoDiagCable=0.0  # effective self weight (gravity component of weight per
                  #volume transverse to the cable)
sigmaPrestrDiagCable=2*210 #final prestress [N]


from model import predefined_spaces

FEcase= xc.FEProblem()
prep=FEcase.getPreprocessor   
points= prep.getMultiBlockTopology.getPoints
lines= prep.getMultiBlockTopology.getLines
nodes= prep.getNodeHandler
sets=prep.getSets
elements=prep.getElementHandler

# Problem type
modelSpace= predefined_spaces.gdls_elasticidad3D(nodes) #Defines the dimension of
                  #the space: nodes by three coordinates (x,y,z) and six
                  #DOF for each node (Ux,Uy,Uz,thetaX,thetaY,thetaZ)

# Model definition
nodes.defaultTag= 1 #First node number.
nod1= nodes.newNodeXYZ(+3,+1,+1)
nod2= nodes.newNodeXYZ(+1,+3,+1)
nod3= nodes.newNodeXYZ(+1,+1,+3)

nod4= nodes.newNodeXYZ(-3,-1,+1)
nod5= nodes.newNodeXYZ(-1,-3,+1)
nod6= nodes.newNodeXYZ(-1,-1,+3)

nod7= nodes.newNodeXYZ(-3,+1,-1)
nod8= nodes.newNodeXYZ(-1,+3,-1)
nod9= nodes.newNodeXYZ(-1,+1,-3)

nod10= nodes.newNodeXYZ(+3,-1,-1)
nod11= nodes.newNodeXYZ(+1,-3,-1)
nod12= nodes.newNodeXYZ(+1,-1,-3)


# #Sections definition
# from materials.sections import section_properties
# strutSect=section_properties.CircularSection(name='strutSect',Rext=strutRext,Rint=strutRint)

#Materials definition
from materials import typical_materials
from materials import typical_materials
#struts material
strutMat=typical_materials.defElasticMaterial(preprocessor=prep, name="strutMat",E=Estruts)
#cables materials
diagCableMat=typical_materials.defCableMaterial(preprocessor=prep,name='diagCableMat',E=EdiagCable,prestress=sigmaPrestrDiagCable,rho=rhoDiagCable)

# Elements definition
elements.defaultMaterial='diagCableMat'
elements.defaultTag= 1
elements.dimElem= 3

diag1= elements.newElement("CorotTruss",xc.ID([1,2]))
diag1.area= diagArea
diag2= elements.newElement("CorotTruss",xc.ID([2,3]))
diag2.area= diagArea
diag3= elements.newElement("CorotTruss",xc.ID([1,3]))
diag3.area= diagArea

diag4= elements.newElement("CorotTruss",xc.ID([4,5]))
diag4.area= diagArea
diag5= elements.newElement("CorotTruss",xc.ID([5,6]))
diag5.area= diagArea
diag6= elements.newElement("CorotTruss",xc.ID([4,6]))
diag6.area= diagArea

diag7= elements.newElement("CorotTruss",xc.ID([7,8]))
diag7.area= diagArea
diag8= elements.newElement("CorotTruss",xc.ID([8,9]))
diag8.area= diagArea
diag9= elements.newElement("CorotTruss",xc.ID([7,9]))
diag9.area= diagArea

diag10= elements.newElement("CorotTruss",xc.ID([10,11]))
diag10.area= diagArea
diag11= elements.newElement("CorotTruss",xc.ID([11,12]))
diag11.area= diagArea
diag12= elements.newElement("CorotTruss",xc.ID([10,12]))
diag12.area= diagArea

diag13= elements.newElement("CorotTruss",xc.ID([1,7]))
diag13.area= diagArea


# Displaying of the mesh
from postprocess.xcVtk.FE_model import vtk_FE_graphic
from postprocess.xcVtk import vtk_graphic_base
defDisplay= vtk_FE_graphic.RecordDefDisplayEF()
totalSet= prep.getSets.getSet('total')
defDisplay.FEmeshGraphic(xcSet=totalSet,caption= 'All elements',cameraParameters= vtk_graphic_base.CameraParameters('XYZPos'))

quit()

# Plotting of CAD entities
# from postprocess.xcVtk.CAD_model import vtk_CAD_graphic
# defDisplay= vtk_CAD_graphic.RecordDefDisplayCAD()
# totalSet= prep.getSets.getSet('total')
# defDisplay.displayBlocks(setToDisplay=totalSet,caption= 'Model grid')

# Seed element for struts
seedElemHandler= prep.getElementHandler.seedElemHandler
seedElemHandler.defaultMaterial= "strutMat"
seedElemHandler.dimElem= 3
seedElemHandler.defaultTag= 1 
strutTruss= seedElemHandler.newElement("CorotTruss",xc.ID([0,0]))
strutTruss.area= strutArea
strutSet.genMesh(xc.meshDir.I)
# Seed element for diagonal cables
seedElemHandler= prep.getElementHandler.seedElemHandler
seedElemHandler.defaultMaterial= "diagCableMat"
seedElemHandler.dimElem= 3    # three-dimensional space 
seedElemHandler.defaultTag= 1 
diagTruss= seedElemHandler.newElement("CorotTruss",xc.ID([0,0]))
diagTruss.area= diagArea
diagSet.genMesh(xc.meshDir.I)
# Seed element for saddle cables
seedElemHandler= prep.getElementHandler.seedElemHandler
seedElemHandler.defaultMaterial= "saddCableMat"
seedElemHandler.dimElem= 3
seedElemHandler.defaultTag= 1 
saddTruss= seedElemHandler.newElement("CorotTruss",xc.ID([0,0]))
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

    
strutSet.fillDownwards()
diagSet.fillDownwards()
saddSet.fillDownwards()

# Displaying of the mesh
# from postprocess.xcVtk.FE_model import vtk_FE_graphic
# defDisplay= vtk_FE_graphic.RecordDefDisplayEF()
# totalSet= prep.getSets.getSet('total')
# defDisplay.FEmeshGraphic(xcSet=totalSet,caption= 'All elements',cameraParameters= vtk_graphic_base.CameraParameters('XYZPos'))
# defDisplay.FEmeshGraphic(xcSet=strutSet,caption= 'Struts',cameraParameters= vtk_graphic_base.CameraParameters('XYZPos'))
# defDisplay.FEmeshGraphic(xcSet=diagSet,caption= 'Diagonal',cameraParameters= vtk_graphic_base.CameraParameters('XYZPos'))
# defDisplay.FEmeshGraphic(xcSet=saddSet,caption= 'Saddle cables',cameraParameters= vtk_graphic_base.CameraParameters('XYZPos'))
# quit()




# Loads definition
cargas= prep.getLoadHandler
casos= cargas.getLoadPatterns
#Load modulation.
ts= casos.newTimeSeries("constant_ts","ts")
casos.currentTimeSeries= "ts"
lPattern= "0"
lp0= casos.newLoadPattern("default",lPattern)
# imposed displacements
# lp0.newSPConstraint(2,0,0.001) #(node, DOF, value)
# lp0.newSPConstraint(2,0,0.001) #(node, DOF, value)
# lp0.newSPConstraint(3,1,0.001) 
# lp0.newSPConstraint(4,0,0.001)
# lp0.newSPConstraint(4,1,0.001) 
#Loads
#lp0.newNodalLoad(2,xc.Vector([210,0,0]))
#lp0.newNodalLoad(4,xc.Vector([210,210,0]))
casos.addToDomain(lPattern) # Add load case to domain

# Solution procedure
solu= FEcase.getSoluProc
solCtrl= solu.getSoluControl
solModels= solCtrl.getModelWrapperContainer
sm= solModels.newModelWrapper("sm")
numberer= sm.newNumberer("default_numberer")
numberer.useAlgorithm("rcm")   # graph algorithm: reverse Cuthill-Macgee.
cHandler= sm.newConstraintHandler("penalty_constraint_handler")
cHandler.alphaSP= 1.0e15  #Factor applied with single-freedom constraints
cHandler.alphaMP= 1.0e15  #Factor applied with multi-freedom constraints
analysisAggregations= solCtrl.getAnalysisAggregationContainer
analysisAggregation= analysisAggregations.newAnalysisAggregation("analysisAggregation","sm") # newAnalysisAggregation(nameAnalysisAggregation,nameWrapper)
solAlgo= analysisAggregation.newSolutionAlgorithm("newton_raphson_soln_algo")
ctest= analysisAggregation.newConvergenceTest("norm_unbalance_conv_test")
ctest.tol= 1e-3
ctest.maxNumIter= 100
ctest.printFlag= 1 #flag used to print information on convergence (optional)
integ= analysisAggregation.newIntegrator("load_control_integrator",xc.Vector([]))
integ.dLambda1= 0.1
soe= analysisAggregation.newSystemOfEqn("band_gen_lin_soe")
solver= soe.newSolver("band_gen_lin_lapack_solver")
analysis= solu.newAnalysis("static_analysis","analysisAggregation","")
result= analysis.analyze(1)


nodes.calculateNodalReactions(True,1e-6)


n1=points.get(1).getNode()
n2=points.get(2).getNode()
n3=points.get(3).getNode()
n4=points.get(4).getNode()
n5=points.get(5).getNode()
n6=points.get(6).getNode()
print n1.getDisp[0],n1.getDisp[1],n1.getDisp[2]
print n4.getDisp[0],n4.getDisp[1],n4.getDisp[2]

strut1=elements.getElement(1)
strut2=elements.getElement(2)
strut3=elements.getElement(3)
diag1=elements.getElement(5)
diag2=elements.getElement(6)
diag3=elements.getElement(7)
saddTop1=elements.getElement(9)
saddTop2=elements.getElement(10)
saddTop3=elements.getElement(11)
saddBot1=elements.getElement(12)
saddBot2=elements.getElement(13)
saddBot3=elements.getElement(14)

F_strut1=strut1.getN()
F_strut2=strut2.getN()
F_strut3=strut3.getN()
F_diag1=diag1.getN()
F_diag2=diag2.getN()
F_diag3=diag3.getN()
F_saddTop1=saddTop1.getN()
F_saddTop2=saddTop2.getN()
F_saddTop3=saddTop3.getN()
F_saddBot1=saddBot1.getN()
F_saddBot2=saddBot2.getN()
F_saddBot3=saddBot3.getN()

print "F_strut1", F_strut1
print "F_strut2", F_strut2
print "F_strut3", F_strut3
print "F_diag1", F_diag1
print "F_diag2", F_diag2
print "F_diag3", F_diag3
print "F_saddTop1", F_saddTop1
print "F_saddTop2", F_saddTop2
print "F_saddTop3", F_saddTop3
print "F_saddBot1", F_saddBot1
print "F_saddBot2", F_saddBot2
print "F_saddBot3", F_saddBot3

print "Linic_strut1", strut1.getLineSegment(True).getLength()
print "Linic_strut2", strut2.getLineSegment(True).getLength()
print "Linic_strut3", strut3.getLineSegment(True).getLength()
print "Linic_diag1", diag1.getLineSegment(True).getLength()
print "Linic_diag2", diag2.getLineSegment(True).getLength()
print "Linic_diag3", diag3.getLineSegment(True).getLength()
print "Linic_saddTop1", saddTop1.getLineSegment(True).getLength()
print "Linic_saddTop2", saddTop2.getLineSegment(True).getLength()
print "Linic_saddTop3", saddTop3.getLineSegment(True).getLength()
print "Linic_saddBot1", saddBot1.getLineSegment(True).getLength()
print "Linic_saddBot2", saddBot2.getLineSegment(True).getLength()
print "Linic_saddBot3", saddBot3.getLineSegment(True).getLength()

deltaL_strut1= strut1.getLineSegment(True).getLength()-strut1.getLineSegment(False).getLength()
deltaL_strut2= strut2.getLineSegment(True).getLength()-strut2.getLineSegment(False).getLength()
deltaL_strut3= strut3.getLineSegment(True).getLength()-strut3.getLineSegment(False).getLength()
deltaL_diag1= diag1.getLineSegment(True).getLength()-diag1.getLineSegment(False).getLength()
deltaL_diag2= diag2.getLineSegment(True).getLength()-diag2.getLineSegment(False).getLength()
deltaL_diag3= diag3.getLineSegment(True).getLength()-diag3.getLineSegment(False).getLength()
deltaL_saddTop1= saddTop1.getLineSegment(True).getLength()-saddTop1.getLineSegment(False).getLength()
deltaL_saddTop2= saddTop2.getLineSegment(True).getLength()-saddTop2.getLineSegment(False).getLength()
deltaL_saddTop3= saddTop3.getLineSegment(True).getLength()-saddTop3.getLineSegment(False).getLength()
deltaL_saddBot1= saddBot1.getLineSegment(True).getLength()-saddBot1.getLineSegment(False).getLength()
deltaL_saddBot2= saddBot2.getLineSegment(True).getLength()-saddBot2.getLineSegment(False).getLength()
deltaL_saddBot3= saddBot3.getLineSegment(True).getLength()-saddBot3.getLineSegment(False).getLength()

print "deltaL_strut1", deltaL_strut1
print "deltaL_strut2", deltaL_strut2
print "deltaL_strut3", deltaL_strut3
print "deltaL_diag1", deltaL_diag1
print "deltaL_diag2", deltaL_diag2
print "deltaL_diag3", deltaL_diag3
print "deltaL_saddTop1", deltaL_saddTop1
print "deltaL_saddTop2", deltaL_saddTop2
print "deltaL_saddTop3", deltaL_saddTop3
print "deltaL_saddBot1", deltaL_saddBot1
print "deltaL_saddBot2", deltaL_saddBot2
print "deltaL_saddBot3", deltaL_saddBot3

from postprocess.xcVtk.FE_model import quick_graphics as qg
lcs=qg.LoadCaseResults(FEcase)
lcs.displayDispRot(itemToDisp='uZ')
quit()

