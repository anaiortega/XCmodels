# -*- coding: utf-8 -*-
from postprocess import limit_state_data as lsd

execfile("../model_gen.py") #FE model generation
execfile("../env_config_deck.py")
setCalc=ties

intForcCombFileName=cfg.intForcPath+'intForce_ULS_normalStressesResistance.csv'
outputFileName=cfg.intForcPath+'maxN.py'
lsd.calc_max_tension_axial_forces(setCalc=setCalc,intForcCombFileName=intForcCombFileName,outputFileName=outputFileName)

#lsd.calc_max_compression_axial_forces(setCalc=setCalc,intForcCombFileName=intForcCombFileName,outputFileName='./pp.py')

