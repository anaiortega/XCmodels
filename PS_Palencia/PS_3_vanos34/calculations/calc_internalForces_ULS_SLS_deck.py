# -*- coding: utf-8 -*-
from postprocess import limit_state_data as lsd
execfile("../model_gen.py") #FE model generation
execfile("../env_config_deck.py")

#Chose combination file (keyComb contains the determining combinations)
execfile(path_loads_def+"keyComb_deck.py")
#execfile(path_loads_def+"loadComb_deck.py")

#Reinforced concrete sections on each element.
#reinfConcreteSections= RC_material_distribution.loadRCMaterialDistribution()

#Steel beams definition

#Set of entities for which checking is going to be performed.
#setCalc=setArmPil
setCalc=setArmados
loadCombinations= preprocessor.getLoadHandler.getLoadCombinations

#Limit states to calculate internal forces for.
limitStates= [lsd.normalStressesResistance, # Normal stresses resistance.
#lsd.shearResistance, # Shear stresses resistance (IS THE SAME AS NORMAL STRESSES, THIS IS WHY IT'S COMMENTED OUT).
#lsd.freqLoadsCrackControl, # RC crack control under frequent loads
#lsd.quasiPermanentLoadsCrackControl, # RC crack control under quasi-permanent loads
#lsd.fatigueResistance # Fatigue resistance.
] 

#limitStates= [lsd.freqLoadsCrackControl]

for ls in limitStates:
    ls.saveAll(combContainer,setCalc,lstSteelBeams=None)
    print 'combinations for ', ls.label, ': ', loadCombinations.getKeys()


