# -*- coding: utf-8 -*-
from postprocess import limit_state_data as lsd
from postprocess.config import default_config

workingDirectory= default_config.findWorkingDirectory()+'/'
exec(open(workingDirectory+'model_gen.py').read()) #FE model generation
lsd.LimitStateData.envConfig= cfg

#Reinforced concrete sections on each element.
#reinfConcreteSections= RC_material_distribution.loadRCMaterialDistribution()

#Steel beams definition
exec(open(workingDirectory+'steel_beams_def.py').read())

#Set of entities for which checking is going to be performed.
setCalc= overallSet

loadCombinations= prep.getLoadHandler.getLoadCombinations

#Limit states to calculate internal forces for.
limitStates= [lsd.steelNormalStressesResistance, # Normal stresses resistance.
lsd.steelShearResistance, # Shear stresses resistance (IS THE SAME AS NORMAL STRESSES, THIS IS WHY IT'S COMMENTED OUT).
lsd.freqLoadsCrackControl, # RC crack control under frequent loads
lsd.quasiPermanentLoadsCrackControl, # RC crack control under quasi-permanent loads
lsd.fatigueResistance # Fatigue resistance.
] 

#limitStates= [lsd.freqLoadsCrackControl]

for ls in limitStates:
  ls.saveAll(combContainer,setCalc,bucklingMembers= [col01a,col01b,col02a,col02b,col03,beam01])
  print('combinations for ', ls.label, ': ', loadCombinations.getKeys())


