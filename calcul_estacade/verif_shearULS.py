# -*- coding: utf-8 -*-

import os

#Project directory structure
exec(open("./env_config.py").read())
from postprocess import limit_state_data as lsd
from postprocess import RC_material_distribution
from materials.sia262 import SIA262_limit_state_checking

lsd.LimitStateData.envConfig= cfg

#Reinforced concrete sections on each element.
reinfConcreteSections= RC_material_distribution.loadRCMaterialDistribution()

#Checking material for limit state.
limitStateLabel= lsd.shearResistance.label
outCfg.controller= SIA262_limit_state_checking.ShearController(limitStateLabel)
lsd.shearResistance.check(reinfConcreteSections)




