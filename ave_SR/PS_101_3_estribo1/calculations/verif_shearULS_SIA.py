# -*- coding: utf-8 -*-

import os

#Project directory structure
execfile("../project_directories.py")

from postprocess import limit_state_data as lsd
from postprocess import RC_material_distribution

from materials.sia262 import SIA262_limit_state_checking

from solution import predefined_solutions

lsd.LimitStateData.internal_forces_results_directory= '../'+internal_forces_results_directory
lsd.LimitStateData.check_results_directory= '../'+check_results_directory

#Reinforced concrete sections on each element.
reinfConcreteSections= RC_material_distribution.loadRCMaterialDistribution()

#Checking material for shear limit state according to SIA262
from materials.sia262 import SIA262_limit_state_checking
limitStateLabel= lsd.shearResistance.label
lsd.shearResistance.controller= SIA262_limit_state_checking.ShearController(limitStateLabel)
meanFCs= lsd.shearResistance.check(reinfConcreteSections)







