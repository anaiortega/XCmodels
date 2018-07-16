# -*- coding: utf-8 -*-
from postprocess import limit_state_data as lsd
from postprocess import RC_material_distribution
from materials.ehe import EHE_limit_state_checking as lschck  #Checking material for shear limit state according to EHE08
#from materials.sia262 import SIA262_limit_state_checking as lschck  #Checking material for shear limit state according to SIA262

execfile('../env_config.py')

#Reinforced concrete sections on each element.
reinfConcreteSections= RC_material_distribution.loadRCMaterialDistribution()

#meanFCs= lsd.shearResistance.check(reinfConcreteSections)


lsd.shearResistance.controller= lschck.ShearController(limitStateLabel= lsd.shearResistance.label)
#from solution import predefined_solutions
#lsd.shearResistance.controller.analysisToPerform= predefined_solutions.simple_newton_raphson
#(FEcheckedModel,meanFCs)= reinfConcreteSections.runChecking(lsd.shearResistance,outputFileName='/tmp/resVerif', matDiagType="d",threeDim= True)  
meanFCs= lsd.shearResistance.check(reinfConcreteSections)





