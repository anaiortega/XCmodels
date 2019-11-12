# -*- coding: utf-8 -*-


import os

model_path="./"
#Project directory structure
execfile("env_config.py")

from postprocess import limit_state_data as lsd
from postprocess import RC_material_distribution
from materials.aci import ACI_limit_state_checking

lsd.LimitStateData.internal_forces_results_directory= cfg.projectDirTree.intForcPath
lsd.LimitStateData.check_results_directory= cfg.projectDirTree.verifPath

#Reinforced concrete sections on each element.
reinfConcreteSections= RC_material_distribution.loadRCMaterialDistribution()

#Checking material for limit state.
limitStateLabel= lsd.shearResistance.label
lsd.shearResistance.controller= ACI_limit_state_checking.ShearController(limitStateLabel)
lsd.shearResistance.check(reinfConcreteSections)



