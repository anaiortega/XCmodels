# -*- coding: utf-8 -*-

import os

#Project directory structure

from postprocess import limit_state_data as lsd
from postprocess import RC_material_distribution
from materials.ehe import EHE_limit_state_checking
#from materials.ec2 import EC2_limit_state_checking
from solution import predefined_solutions

lsd.LimitStateData.envConfig= cfg

#Reinforced concrete sections on each element.
reinfConcreteSections=RC_material_distribution.RCMaterialDistribution()
reinfConcreteSections.mapSectionsFileName='./mapSectionsReinforcementTenStiff.pkl'
reinfConcreteSections=RC_material_distribution.loadRCMaterialDistribution()
#Checking material for limit state.
limitStateLabel= lsd.freqLoadsCrackControl.label
lsd.freqLoadsCrackControl.controller= EHE_limit_state_checking.CrackStraightController(limitStateLabel= lsd.freqLoadsCrackControl.label)
lsd.freqLoadsCrackControl.controller.analysisToPerform=predefined_solutions.simple_static_modified_newton
lsd.freqLoadsCrackControl.check(reinfConcreteSections)



