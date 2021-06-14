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
limitStress= 355e6 #XXX
limitStateLabel= lsd.freqLoadsCrackControl.label
outCfg.controller= SIA262_limit_state_checking.CrackControlSIA262PlanB(limitStateLabel,limitStress)
lsd.freqLoadsCrackControl.check(reinfConcreteSections)



