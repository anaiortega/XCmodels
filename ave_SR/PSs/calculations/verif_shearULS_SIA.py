# -*- coding: utf-8 -*-

import os

#Project directory structure
execfile("../env_config.py")

from postprocess import limit_state_data as lsd
from postprocess import RC_material_distribution

from materials.sia262 import SIA262_limit_state_checking

from solution import predefined_solutions

lsd.LimitStateData.envConfig= cfg

#Reinforced concrete sections on each element.
reinfConcreteSections= RC_material_distribution.loadRCMaterialDistribution()

#Checking material for shear limit state according to SIA262
from materials.sia262 import SIA262_limit_state_checking
limitStateLabel= lsd.shearResistance.label
lsd.shearResistance.controller= SIA262_limit_state_checking.ShearController(limitStateLabel)
lsd.shearResistance.check(reinfConcreteSections)







