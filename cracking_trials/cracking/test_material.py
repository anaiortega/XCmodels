import xc_base
import geom
import xc
import math
from materials.ec2 import EC2_materials
from materials import concrete_base
from materials import typical_materials
import matplotlib.pyplot as plt
import numpy as np

f_ck=33e6      #concrete characteristic strength [Pa] (concrete C30-37 adopted)
f_ct=3.086*1e6   # concrete tensile strength
               # (in the test the calculated fctm=2896468.15 is used)
ro_s_eff=0.04740833      #effective ratio of reinforcement

# Model definition
problem=xc.FEProblem()              #necesary to create this instance of
                                     #the class xc.FEProblem()
preprocessor=problem.getPreprocessor

# Materials definition
concrete= EC2_materials.EC2Concrete("C33",-33e6,1.5) #concrete according to EC2 fck=33 MPa      

#Reinforcing steel.
rfSteel= EC2_materials.S450C #reinforcing steel according to EC2 fyk=450 MPa
steelDiagram= rfSteel.defDiagK(preprocessor) #Definition of steel stress-strain diagram in XC. 

#Parameters for tension stiffening of concrete
paramTS=concrete_base.paramTensStiffness(concrMat=concrete,reinfMat=rfSteel,reinfRatio=ro_s_eff,diagType='K')
concrete.tensionStiffparam=paramTS           #parameters for tension stiffening are assigned to concrete
concrDiagram=concrete.defDiagK(preprocessor) #Definition of concrete stress-strain diagram in XC.


epsMin=concrDiagram.epscu
epsMax=concrDiagram.epsctu
nmbPoints=100
interval=(epsMax-epsMin)/nmbPoints
epsLst=[epsMin+i*interval for i in range(nmbPoints)]+[epsMax-i*interval for i in range(nmbPoints)]
sigmaLst=list()
print 'concrDiagram \n'
for eps in epsLst:
  concrDiagram.setTrialStrain(eps, 0.0)
  concrDiagram.commitState()
  sigmaLst.append([eps,concrDiagram.getStress()*1e-6])
  print eps,'   ',concrDiagram.getStress()*1e-6
concrDiagram.revertToStart()  
