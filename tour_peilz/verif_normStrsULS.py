# -*- coding: utf-8 -*-


import os
from postprocess import limit_state_data as lsd
from postprocess import RC_material_distribution
from materials.sia262 import SIA262_limit_state_checking

lsd.LimitStateData.internal_forces_results_directory= './results/internalForces/'
lsd.LimitStateData.check_results_directory= './results/verifications/'

#Reinforced concrete sections on each element.
reinfConcreteSections= RC_material_distribution.loadRCMaterialDistribution()

limitStateLabel= lsd.normalStressesResistance.label
lsd.normalStressesResistance.controller= SIA262_limit_state_checking.BiaxialBendingNormalStressController(limitStateLabel)
lsd.normalStressesResistance.check(reinfConcreteSections)



