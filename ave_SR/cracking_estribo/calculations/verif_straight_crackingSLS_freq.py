# -*- coding: utf-8 -*-
from solution import predefined_solutions
from postprocess import limit_state_data as lsd
from postprocess import RC_material_distribution
from materials.ehe import EHE_limit_state_checking as lschck
#from materials.ec2 import EC2_limit_state_checking

execfile('../env_config.py')
lsd.LimitStateData.envConfig= cfg

#Reinforced concrete sections on each element.
#reinfConcreteSections=RC_material_distribution.RCMaterialDistribution()
reinfConcreteSections=RC_material_distribution.loadRCMaterialDistribution()
reinfConcreteSections.mapSectionsFileName='./mapSectionsReinforcementTenStiff.pkl'
#Checking material for limit state.
limitStateLabel= lsd.freqLoadsCrackControl.label
lsd.freqLoadsCrackControl.controller= lschck.CrackStraightController(limitStateLabel= lsd.freqLoadsCrackControl.label)
lsd.freqLoadsCrackControl.controller.analysisToPerform=predefined_solutions.plain_static_modified_newton
lsd.freqLoadsCrackControl.check(reinfConcreteSections)



