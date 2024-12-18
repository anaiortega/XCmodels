# -*- coding: utf-8 -*-


import os
from postprocess import limit_state_data as lsd
from postprocess import RC_material_distribution
from materials.sia262 import SIA262_limit_state_checking

exec(open("../projectDirs.py").read())
lsd.LimitStateData.envConfig= cfg

lsd.LimitStateData.internal_forces_results_directory= projectDirs.getInternalForcesResultsDirectory()
lsd.LimitStateData.check_results_directory= projectDirs.getCheckResultsDirectory()

#Reinforced concrete sections on each element.
reinfConcreteSections= RC_material_distribution.loadRCMaterialDistribution()

limitStateLabel= lsd.normalStressesResistance.label
outCfg.controller= SIA262_limit_state_checking.BiaxialBendingNormalStressController(limitStateLabel)
lsd.normalStressesResistance.check(reinfConcreteSections)



