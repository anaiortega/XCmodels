# -*- coding: utf-8 -*-

#Reproduction of an X tensegrity model, from the document «Desarrollo de una metodología basada en el método de los elementos finitos para la proyección de estructuras tenségridas», by Puigoriol Forcada et al.


import xc_base
import geom
import xc
from solution import predefined_solutions
from model import predefined_spaces
from materials import typical_materials
import math

E=2.1e5  #Young modulus [MPa]
l=1      #lenght
area=1   #area
#sigmaPret=1e-5  #must be >0
sigmaPret=500

# Model definition
FEcase= xc.FEProblem()
preprocessor=  FEcase.getPreprocessor
nodes= preprocessor.getNodeHandler
elements= preprocessor.getElementHandler

# Problem type
modelSpace= predefined_spaces.gdls_elasticidad3D(nodes) #Defines the dimension of
                  #the space: nodes by three coordinates (x,y,z) and 
                  #three DOF for each node (Ux,Uy,Uz)
                  #IMPORTANT NOT TO PASS BY

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
ctruss1.area= area
ctruss2= elements.newElement("CorotTruss",xc.ID([1,3]))
ctruss2.area= area
ctruss3= elements.newElement("CorotTruss",xc.ID([2,4]))
ctruss3.area= area
ctruss4= elements.newElement("CorotTruss",xc.ID([3,4]))
ctruss4.area= area
elements.defaultMaterial= "strutMat"
ctruss5= elements.newElement("CorotTruss",xc.ID([1,4]))
ctruss5.area= area
ctruss6= elements.newElement("CorotTruss",xc.ID([2,3]))
ctruss6.area= area


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

R1X= nod1.getReaction[0]
R1Y= nod1.getReaction[1] 
R2Y= nod2.getReaction[1] 
deltaX_n2= nod2.getDisp[0]
deltaY_n2= nod2.getDisp[1]  
deltaX_n3= nod3.getDisp[0]
deltaY_n3= nod3.getDisp[1]  
deltaX_n4= nod4.getDisp[0]
deltaY_n4= nod4.getDisp[1]  

stress_el1= ctruss1.getN()
stress_el2= ctruss2.getN()
stress_el3= ctruss3.getN()
stress_el4= ctruss4.getN()
stress_el5= ctruss5.getN()
stress_el6= ctruss6.getN()

length_el1=ctruss1.getLineSegment(False).getLength()
length_el2=ctruss2.getLineSegment(False).getLength()
length_el3=ctruss3.getLineSegment(False).getLength()
length_el4=ctruss4.getLineSegment(False).getLength()
length_el5=ctruss5.getLineSegment(False).getLength()
length_el6=ctruss6.getLineSegment(False).getLength()

lengthIncr_el1=length_el1-ctruss1.getLineSegment(True).getLength()
lengthIncr_el2=length_el2-ctruss2.getLineSegment(True).getLength()
lengthIncr_el3=length_el3-ctruss3.getLineSegment(True).getLength()
lengthIncr_el4=length_el4-ctruss4.getLineSegment(True).getLength()
lengthIncr_el5=length_el5-ctruss5.getLineSegment(True).getLength()
lengthIncr_el6=length_el6-ctruss6.getLineSegment(True).getLength()

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
print 'stress_el1= ',stress_el1
print 'stress_el2= ',stress_el2
print 'stress_el3= ',stress_el3
print 'stress_el4= ',stress_el4
print 'stress_el5= ',stress_el5
print 'stress_el6= ',stress_el6
print
print 'length_el1= ',length_el1
print 'length_el2= ',length_el2
print 'length_el3= ',length_el3
print 'length_el4= ',length_el4
print 'length_el5= ',length_el5
print 'length_el6= ',length_el6
print
print 'lengthIncr_el1= ',lengthIncr_el1
print 'lengthIncr_el2= ',lengthIncr_el2
print 'lengthIncr_el3= ',lengthIncr_el3
print 'lengthIncr_el4= ',lengthIncr_el4
print 'lengthIncr_el5= ',lengthIncr_el5
print 'lengthIncr_el6= ',lengthIncr_el6
