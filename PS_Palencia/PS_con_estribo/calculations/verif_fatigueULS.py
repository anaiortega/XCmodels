# -*- coding: utf-8 -*-
from materials.sia262 import SIA262_limit_state_checking

execfile("../model_gen.py") #FE model generation

#choose env_config file:
execfile("../env_config_deck.py")
execfile("../env_config_abutment.py")
#
# variables that control the output of the checking (setCalc,
# appendToResFile .py [defaults to 'N'], listFile .tex [defaults to 'N']
outCfg= lsd.VerifOutVars(setCalc=beamX,appendToResFile='N',listFile='N')

#Reinforced concrete sections on each element.
reinfConcreteSections= RC_material_distribution.loadRCMaterialDistribution()

limitStateLabel= lsd.fatigueResistance.label
lsd.fatigueResistance.controller= SIA262_limit_state_checking.FatigueController(limitStateLabel)
lsd.fatigueResistance.check(reinfConcreteSections,outCfg)


