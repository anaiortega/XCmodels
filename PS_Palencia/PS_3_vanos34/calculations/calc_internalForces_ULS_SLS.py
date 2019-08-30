# -*- coding: utf-8 -*-
from postprocess import limit_state_data as lsd
execfile("../env_config.py")
execfile("../model_gen.py") #FE model generation
if pile_found.lower()[0]=='y':
    execfile(path_loads_def+"loadComb_deck_and_abutment.py")
else:
    execfile(path_loads_def+"loadComb_deck.py")
#Reinforced concrete sections on each element.
#reinfConcreteSections= RC_material_distribution.loadRCMaterialDistribution()

#Steel beams definition

#Set of entities for which checking is going to be performed.
setCalc=setArmados+setArmadosEstr
#setCalc=struts
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
    ls.saveAll(FEcase,combContainer,setCalc,lstSteelBeams=None)
    print 'combinations for ', ls.label, ': ', loadCombinations.getKeys()

