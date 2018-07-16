# -*- coding: utf-8 -*-
from materials.sia262 import SIA262_limit_state_checking

execfile('../env_config.py')

#Reinforced concrete sections on each element.
reinfConcreteSections= RC_material_distribution.loadRCMaterialDistribution()

limitStateLabel= lsd.fatigueResistance.label
lsd.fatigueResistance.controller= SIA262_limit_state_checking.FatigueController(limitStateLabel)
meanFCs= lsd.fatigueResistance.check(reinfConcreteSections)


