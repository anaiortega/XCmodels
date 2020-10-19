# -*- coding: utf-8 -*-


from postprocess import limit_state_data as lsd
from postprocess import RC_material_distribution
#from materials.ehe import EHE_limit_state_checking
from materials.ec2 import EC2_limit_state_checking
from solution import predefined_solutions

lsd.LimitStateData.envConfig= cfg

#Reinforced concrete sections on each element.
#reinfConcreteSections=RC_material_distribution.RCMaterialDistribution()
reinfConcreteSections=RC_material_distribution.loadRCMaterialDistribution()
reinfConcreteSections.mapSectionsFileName='./mapSectionsReinforcementTenStiff.pkl'
#Checking material for limit state.
limitStateLabel= lsd.freqLoadsCrackControl.label
lsd.freqLoadsCrackControl.controller= EC2_limit_state_checking.CrackStraightController(limitStateLabel= lsd.freqLoadsCrackControl.label)
lsd.freqLoadsCrackControl.controller.solutionProcedureType= predefined_solutions.PlainStaticModifiedNewton
lsd.freqLoadsCrackControl.check(reinfConcreteSections)



