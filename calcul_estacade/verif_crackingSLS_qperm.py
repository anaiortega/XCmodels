# -*- coding: utf-8 -*-

import os

#Project directory structure
execfile("./env_config.py")

from postprocess import limit_state_data as lsd
from postprocess import RC_material_distribution
from materials.sia262 import SIA262_limit_state_checking

lsd.LimitStateData.internal_forces_results_directory= cfg.projectDirTree.intForcPath
lsd.LimitStateData.check_results_directory= cfg.projectDirTree.verifPath

#Reinforced concrete sections on each element.
reinfConcreteSections= RC_material_distribution.loadRCMaterialDistribution()

#Checking material for limit state.
limitStress= 230e6 #XXX 
limitStateLabel= lsd.quasiPermanentLoadsCrackControl.label
lsd.quasiPermanentLoadsCrackControl.controller= SIA262_limit_state_checking.CrackControlSIA262PlanB(limitStateLabel,limitStress)
lsd.quasiPermanentLoadsCrackControl.check(reinfConcreteSections)

