# -*- coding: utf-8 -*-

import os
from postprocess import limit_state_data as lsd
from postprocess import RC_material_distribution
from materials.sia262 import SIA262_limit_state_checking

#Project directory structure
exec(open("../env_config.py").read())

lsd.LimitStateData.envConfig= cfg

#Reinforced concrete sections on each element.
reinfConcreteSections= RC_material_distribution.loadRCMaterialDistribution()

limitStateLabel= lsd.fatigueResistance.label
outCfg.controller= SIA262_limit_state_checking.FatigueController(limitStateLabel)
lsd.fatigueResistance.check(reinfConcreteSections)


