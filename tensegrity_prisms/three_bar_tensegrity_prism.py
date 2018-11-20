# -*- coding: utf-8 -*-
from __future__ import division

__author__= "Ana Ortega (AO_O) and Luis C. Pérez Tato (LCPT)"
__copyright__= "Copyright 2017, AO_O and LCPT"
__license__= "GPL"
__version__= "3.0"
__email__= "ana.Ortega@ciccp.es l.pereztato@ciccp.es" 

import os
import xc_base
import geom
import xc
import math
import pandas as pd
import numpy as np

def genJointsCoor(n,r0,rh,b):
    ''':returns: the cart. coord. of the joinst of a rotationally symetric  
    tensegrity prism with n-polygons on two parallel planes, twisted over angle 
    alfa with respect to each other. The twist angle is obtained by the 
    theorem of Tobie and Kenner as: alfa=pi/2-pi/n.
    The origin of the cartesian coordinate system is placed at the center of 
    the base circle, with the z-axis in the axis of the cylinder and joint 
    n+1.
    'jt' corresponds to joints in the top circle
    'jb' corresponds to joints in the base circle

    :param n: number of sides of the regular n-polygon 
    :param r0: radius of the base circle circunscribing the n-polygon
    :param rh: radius of the top circle circunscribing the n-polygon
    :param b: length of the struts
    '''
    #Twist angle
    alfa=math.pi*(1/2-1/n)
    #height of the prism
    h=math.sqrt(b**2-rh**2-r0**2+2*rh*r0*math.cos(2*math.pi/n+alfa))
    angPoly=2*math.pi/n
    retval=pd.DataFrame(columns=("X","Y","Z"))
    #joints in top circle (jt):
    for i in range(1,n+1):
        ang=alfa+i*angPoly
        retval.loc['jt'+str(i)]=rh*math.cos(ang),rh*math.sin(ang),h
    #joints in base circle (jb):
    for i in range(1,n+1):
        ang=(i-1)*angPoly
        retval.loc['jb'+str(i+n)]=r0*math.cos(ang),r0*math.sin(ang),0
    return retval



def genLineLinkedJoints(n):
    '''Return the joints id linked by each line (strut or cable)
    'strut' corresponds to compression bars
    'sadd' corresponds to saddle strings (cables forming the n-polygons)
    'diag' corresponds to diagonal strings 

    :param n: number of sides of the regular n-polygon  
    '''
    retval=pd.DataFrame(columns=("i_jt","j_jt"))
    for i in range(1,n+1):
        retval.loc['strut'+str(i)]=i+n,i
    for i in range(1,n):
        retval.loc['sadd'+str(i)]=n+i,n+i+1
    retval.loc['sadd'+str(n)]=2*n,n+1
    for i in range(1,n):
        retval.loc['sadd'+str(n+i)]=i,i+1
    retval.loc['sadd'+str(2*n)]=n,1
    for i in range(1,n):
        retval.loc['diag'+str(i)]=n+1+i,i
    retval.loc['diag'+str(n)]=n+1,n
    return retval.astype(int)
    

# a= genJointsCoor(5,0.33,0.33,1)
# print a

# b=genLineLinkedJoints(n)
# print b


# import matplotlib.pyplot as plt
# plt.figure()
# plt.plot(a.X[0:n],a.Y[0:n],'ro')
# plt.plot(a.X[n:2*n],a.Y[n:2*n],'bo')
# plt.show()


#FE problem
#Data
#    geometry
nSidPol=8     # number of sides of the regular n-polygon
rBasCirc=0.33 # radius of the base circle circunscribing the n-polygon
rTopCirc=0.33 # radius of the top circle circunscribing the n-polygon
lStruts=1.414   # length of the struts [m]
#    materials
#struts material
Estruts=210e9    # elastic modulus [Pa]
Gstruts=79.3e9   # shear modulus [Pa] 
rhoStruts=7850   # mass density [kg/m3]
fyStruts=200e6   # yield strength [Pa]
nuStruts=0.3     # Poisson's coefficient
strutRint=50e-3-10.95e-3  #internal radius [m]
strutRext=50e-3           #external radius [m]
strutArea=1

#diagonal cables material
EdiagCable=210e9      #elastic modulus
rhoDiagCable=0.0  # effective self weight (gravity component of weight per
                  #volume transverse to the cable)
sigmaPrestrDiagCable=1 #prestress
diagArea=1
#saddle cables material
EsaddCable=210e9  #elastic modulus
rhoSaddCable=0.0  # effective self weight (gravity component of weight per
                  #volume transverse to the cable)
sigmaPrestrSaddCable=1 #prestress
saddArea=1                  

from model import predefined_spaces

test= xc.FEProblem()
prep=test.getPreprocessor   
points= prep.getMultiBlockTopology.getPoints
lines= prep.getMultiBlockTopology.getLines
nodes= prep.getNodeHandler
sets=prep.getSets

# Problem type
modelSpace= predefined_spaces.SolidMechanics3D(nodes) #Defines the dimension of
                  #the space: nodes by three coordinates (x,y,z) and 
                  #three DOF for each node (Ux,Uy,Uz)
#Joints generation
jointsCCoor=genJointsCoor(n=nSidPol,r0=rBasCirc,rh=rTopCirc,b=lStruts)
for i in jointsCCoor.index:
    points.newPntIDPos3d(int(float(i[2:])),geom.Pos3d(jointsCCoor.loc[i].X,jointsCCoor.loc[i].Y,jointsCCoor.loc[i].Z))
    
#Lines generation
linsJoints=genLineLinkedJoints(n=nSidPol)
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

#Sections definition
from materials.sections import section_properties
strutSect=section_properties.CircularSection(name='strutSect',Rext=strutRext,Rint=strutRint)

#Materials definition
from materials import typical_materials
from materials import typical_materials
#struts material
strutMat=typical_materials.defElasticMaterial(preprocessor=prep, name="strutMat",E=Estruts)
#strutMat=typical_materials.defElasticSection3d(preprocessor=prep,name='strutMat',A=strutSect.A(),E=Estruts,G=Gstruts,Iz=strutSect.Iz(),Iy=strutSect.Iy(),J=strutSect.J())
#cables materials
diagCableMat=typical_materials.defCableMaterial(preprocessor=prep,name='diagCableMat',E=EdiagCable,prestress=sigmaPrestrDiagCable,rho=rhoDiagCable)
saddCableMat=typical_materials.defCableMaterial(preprocessor=prep,name='saddCableMat',E=EdiagCable,prestress=sigmaPrestrSaddCable,rho=rhoSaddCable)

# Plotting of CAD entities
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
seedElemHandler.defaultTransformation="ltStruts"
seedElemHandler.dimElem= 3
seedElemHandler.defaultTag= 1 
#strutTruss= seedElemHandler.newElement("ElasticBeam3d",xc.ID([0,0]))
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
# # Static solution
# analysis= predefined_solutions.simple_static_linear(test)
# result= analysis.analyze(1)

#Newton Raphson
Nstep= 100       #  apply load in 10 steps
DInc= 1./Nstep 	#  first load increment
solu= test.getSoluProc
solCtrl= solu.getSoluControl
solModels= solCtrl.getModelWrapperContainer
sm= solModels.newModelWrapper("sm")
cHandler= sm.newConstraintHandler("plain_handler")
numberer= sm.newNumberer("default_numberer")
numberer.useAlgorithm("simple")
analysisAggregations= solCtrl.getAnalysisAggregationContainer
analysisAggregation= analysisAggregations.newAnalysisAggregation("analysisAggregation","sm")
solAlgo= analysisAggregation.newSolutionAlgorithm("newton_raphson_soln_algo")
ctest= analysisAggregation.newConvergenceTest("norm_unbalance_conv_test")
ctest.tol= 1e-8
ctest.maxNumIter= 100
integ= analysisAggregation.newIntegrator("load_control_integrator",xc.Vector([]))
integ.dLambda1= DInc
soe= analysisAggregation.newSystemOfEqn("band_gen_lin_soe")
solver= soe.newSolver("band_gen_lin_lapack_solver")
analysis= solu.newAnalysis("static_analysis","analysisAggregation","")
result= analysis.analyze(Nstep)

quit()


nodes.calculateNodalReactions(True,1e-6)
R1= nodes.getNode(2).getReaction[0] 
R2= nodes.getNode(1).getReaction[0] 

print R1
print R2
quit()








# Loads definition
cargas= prep.getLoadHandler
casos= cargas.getLoadPatterns
#Load modulation.
ts= casos.newTimeSeries("constant_ts","ts")
casos.currentTimeSeries= "ts"
lPattern= "0"
lp0= casos.newLoadPattern("default",lPattern)
casos.currentLoadPattern= lPattern
casos.addToDomain(lPattern)


Nstep= 10  #  apply load in 10 steps
DInc= 1./Nstep 	#  first load increment


solu= test.getSoluProc
solCtrl= solu.getSoluControl
solModels= solCtrl.getModelWrapperContainer
sm= solModels.newModelWrapper("sm")
numberer= sm.newNumberer("default_numberer")
numberer.useAlgorithm("simple")
cHandler= sm.newConstraintHandler("plain_handler")
analysisAggregations= solCtrl.getAnalysisAggregationContainer
analysisAggregation= analysisAggregations.newAnalysisAggregation("analysisAggregation","sm")
solAlgo= analysisAggregation.newSolutionAlgorithm("newton_raphson_soln_algo")
ctest= analysisAggregation.newConvergenceTest("norm_unbalance_conv_test")
ctest.tol= 1e-6
ctest.maxNumIter= 100
integ= analysisAggregation.newIntegrator("load_control_integrator",xc.Vector([]))
integ.dLambda1= DInc
soe= analysisAggregation.newSystemOfEqn("band_gen_lin_soe")
solver= soe.newSolver("band_gen_lin_lapack_solver")
analysis= solu.newAnalysis("static_analysis","analysisAggregation","")
result= analysis.analyze(Nstep)
