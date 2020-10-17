# -*- coding: utf-8 -*-

import xc_base
import geom
import xc
from solution import predefined_solutions
from model import predefined_spaces
from materials import typical_materials
import math

E=2.1e11  #Young modulus [Pa]
l=1      #length of cables [m]
areaStrut=1e-4   #cros-section area of struts [m2]
areaCable=1e-4   #cros-section area of cables [m2]
#sigmaPret=1e-5  #must be >0
sigmaPret=420e6  #prestressing stress in cables [Pa]


# Model definition
FEcase= xc.FEProblem()
preprocessor=  FEcase.getPreprocessor
nodes= preprocessor.getNodeHandler
elements= preprocessor.getElementHandler

# Problem type
modelSpace= predefined_spaces.SolidMechanics3D(nodes) #Defines the dimension of
                  #the space: nodes by three coordinates (x,y,z) and 
                  #three DOF for each node (Ux,Uy,Uz)

# Model definition
nodes.defaultTag= 1 #First node number.
nod1= nodes.newNodeXYZ(0,0,0)    #node 1
nod2= nodes.newNodeXYZ(l,0,0)    #node 2
nod3= nodes.newNodeXYZ(0,l,0)  
nod4= nodes.newNodeXYZ(l,l,0)  

# Materials definition
cable=typical_materials.defCableMaterial(preprocessor, name="cable",E=E,prestress=sigmaPret,rho=0.0)
              #uniaxial bilinear prestressed material. The stress strain ranges
              #from slack (large strain at zero stress) to taught
              #(linear with modulus E).
              #rho= effective self weight (gravity component of weight per 
              #     volume transverse to the cable)
strutMat=typical_materials.defElasticMaterial(preprocessor, name="strutMat",E=E) #elastic uniaxial material

# Elements definition
elements.defaultMaterial= "cable"
elements.defaultTag= 1 #First element number.
elements.dimElem= 3
ctruss1= elements.newElement("CorotTruss",xc.ID([1,2]))
ctruss1.sectionArea= areaCable
ctruss2= elements.newElement("CorotTruss",xc.ID([1,3]))
ctruss2.sectionArea= areaCable
ctruss3= elements.newElement("CorotTruss",xc.ID([2,4]))
ctruss3.sectionArea= areaCable
ctruss4= elements.newElement("CorotTruss",xc.ID([3,4]))
ctruss4.sectionArea= areaCable
elements.defaultMaterial= "strutMat"
ctruss5= elements.newElement("CorotTruss",xc.ID([1,4]))
ctruss5.sectionArea= areaStrut
ctruss6= elements.newElement("CorotTruss",xc.ID([2,3]))
ctruss6.sectionArea= areaStrut


# Constraints
modelSpace.fixNode000(1)
constraints= modelSpace.constraints
constraints.newSPConstraint(2,1,0.0) # newSPConstraint(tag_nod,id_gdl,valor)
                                    # Create a single-point boundary constraint
constraints.newSPConstraint(2,2,0.0)
constraints.newSPConstraint(3,2,0.0)
constraints.newSPConstraint(4,2,0.0)

# Loads definition
cargas= preprocessor.getLoadHandler
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
solutionStrategies= solCtrl.getSolutionStrategyContainer
solutionStrategy= solutionStrategies.newSolutionStrategy("solutionStrategy","sm") # newSolutionStrategy(nameSolutionStrategy,nameWrapper)
solAlgo= solutionStrategy.newSolutionAlgorithm("newton_raphson_soln_algo")
ctest= solutionStrategy.newConvergenceTest("norm_unbalance_conv_test")
ctest.tol= 1e-3
ctest.maxNumIter= 100
ctest.printFlag= 1 #flag used to print information on convergence (optional)
integ= solutionStrategy.newIntegrator("load_control_integrator",xc.Vector([]))
integ.dLambda1= 0.1
soe= solutionStrategy.newSystemOfEqn("band_gen_lin_soe")
solver= soe.newSolver("band_gen_lin_lapack_solver")
analysis= solu.newAnalysis("static_analysis","solutionStrategy","")
result= analysis.analyze(1)


nodes.calculateNodalReactions(True,1e-6)

R1X= nod1.getReaction[0]
R1Y= nod1.getReaction[1] 
R2Y= nod2.getReaction[1] 
deltaX_n2= nod2.getDisp[0]
deltaY_n2= nod2.getDisp[1]  
deltaX_n3= nod3.getDisp[0]
deltaY_n3= nod3.getDisp[1]  
deltaX_n4= nod4.getDisp[0]
deltaY_n4= nod4.getDisp[1]  

F_el1= ctruss1.getN()
F_el2= ctruss2.getN()
F_el3= ctruss3.getN()
F_el4= ctruss4.getN()
F_el5= ctruss5.getN()
F_el6= ctruss6.getN()

#deformed length
length_el1=ctruss1.getLineSegment(False).getLength()
length_el2=ctruss2.getLineSegment(False).getLength()
length_el3=ctruss3.getLineSegment(False).getLength()
length_el4=ctruss4.getLineSegment(False).getLength()
length_el5=ctruss5.getLineSegment(False).getLength()
length_el6=ctruss6.getLineSegment(False).getLength()

print 'R1X= ', R1X
print 'R1Y= ', R1Y
print 'R2Y= ', R2Y
print
print 'deltaX_n2= ', deltaX_n2
print 'deltaX_n3= ', deltaX_n3
print 'deltaY_n3= ', deltaY_n3
print 'deltaX_n4= ', deltaX_n4
print 'deltaY_n4= ', deltaY_n4
print
print 'F_el1= ',F_el1
print 'F_el2= ',F_el2
print 'F_el3= ',F_el3
print 'F_el4= ',F_el4
print 'F_el5= ',F_el5
print 'F_el6= ',F_el6
# print
# print 'length_el1= ',length_el1
# print 'length_el2= ',length_el2
# print 'length_el3= ',length_el3
# print 'length_el4= ',length_el4
# print 'length_el5= ',length_el5
# print 'length_el6= ',length_el6
print
print 'delta_length_el1= ',length_el1-l
print 'delta_length_el2= ',length_el2-l
print 'delta_length_el3= ',length_el3-l
print 'delta_length_el4= ',length_el4-l
print 'delta_length_el5= ',length_el5-l*math.sqrt(2)
print 'delta_length_el6= ',length_el6-l*math.sqrt(2)
print
print "Analytical solution (for areaStrut=areaCable"
F_cable=sigmaPret*areaCable/(1+math.sqrt(2))
F_strut=-F_cable*math.sqrt(2)
deltL_cable=(F_cable/areaCable-sigmaPret)/E*l
deltL_strut=F_strut/areaStrut/E*(l*math.sqrt(2))

print 'F_cable=', F_cable
print 'F_strut=', F_strut
print 'delta_L_cable=',deltL_cable
print 'delta_L_strut=',deltL_strut


from postprocess import utils_display
from postprocess.xcVtk.FE_model import quick_graphics as QGrph
from postprocess.xcVtk import vtk_graphic_base
xcTotalSet=utils_display.setToDisplay(elSet=preprocessor.getSets.getSet('total'),genDescr='',sectDescr=[])

lcs=QGrph.LoadCaseResults(FEcase)
#lcs.displayDispRot(itemToDisp='uX',setToDisplay=xcTotalSet.elSet,fConvUnits=1000,unitDescription='mm', vtk_graphic_base.CameraParameters('XYZPos',1),fileName=None,defFScale=0.0)

# lcs.displayDispRot(itemToDisp='uZ',defFScale=1e2)
# lcs.displayDispRot(itemToDisp='uY')

lcs.loadCaseName='Prestressing stress= 420 Mpa                                                   '
xcTotalSet.elSet.name=''

lcs.displayIntForcDiag(itemToDisp='N',setToDisplay=xcTotalSet.elSet,fConvUnits= 1.0e-3,scaleFactor=1,unitDescription=': Axial forces (kN)',  viewDef=vtk_graphic_base.CameraParameters('ZPos',1),fileName='val_quad01.jpg',defFScale=25.0)



