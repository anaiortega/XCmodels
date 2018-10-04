# -*- coding: utf-8 -*-
from solution import predefined_solutions
from postprocess import limit_state_data as lsd
from postprocess import RC_material_distribution
from materials.ehe import EHE_limit_state_checking as lschck
#from materials.ec2 import EC2_limit_state_checking

execfile("../model_gen.py") #FE model generation

setCalc=decks  #set of elements for which to perform the checking

#Reinforced concrete sections on each element.
#reinfConcreteSections=RC_material_distribution.RCMaterialDistribution()
reinfConcreteSections=RC_material_distribution.loadRCMaterialDistribution()
reinfConcreteSections.mapSectionsFileName='./mapSectionsReinforcementTenStiff.pkl'
#Checking material for limit state.
limitStateLabel= lsd.freqLoadsCrackControl.label
lsd.freqLoadsCrackControl.controller= lschck.CrackStraightController(limitStateLabel= lsd.quasiPermanentLoadsCrackControl.label)
lsd.freqLoadsCrackControl.controller.analysisToPerform=predefined_solutions.simple_static_modified_newton
meanFCs= lsd.quasiPermanentLoadsCrackControl.check(reinfConcreteSections,setCalc=setCalc)



