# -*- coding: utf-8 -*-

from materials.sia262 import SIA262_limit_state_checking
from solution import predefined_solutions

#Results directories
execfile('./calculs_config.py')

#Reinforced concrete sections on each element.
reinfConcreteSections= RC_material_distribution.loadRCMaterialDistribution()

#Checking material for shear limit state according to SIA262
from materials.sia262 import SIA262_limit_state_checking
limitStateLabel= lsd.shearResistance.label
lsd.shearResistance.controller= SIA262_limit_state_checking.ShearController(limitStateLabel)
meanFCs= lsd.shearResistance.check(reinfConcreteSections)







