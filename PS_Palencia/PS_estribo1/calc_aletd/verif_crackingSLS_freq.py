# -*- coding: utf-8 -*-

import os

#Project directory structure
execfile("../project_directories.py")

from postprocess import limit_state_data as lsd
from postprocess import RC_material_distribution
from materials.sia262 import SIA262_limit_state_checking
execfile('./directs.py')

lsd.LimitStateData.internal_forces_results_directory= dir_int_forces
lsd.LimitStateData.check_results_directory= dir_checks

#Reinforced concrete sections on each element.
reinfConcreteSections= RC_material_distribution.loadRCMaterialDistribution()

#Checking material for limit state.
limitStress= 350e6 #XXX
limitStateLabel= lsd.freqLoadsCrackControl.label
lsd.freqLoadsCrackControl.controller= SIA262_limit_state_checking.CrackControlSIA262PlanB(limitStateLabel,limitStress)
lsd.freqLoadsCrackControl.check(reinfConcreteSections)



