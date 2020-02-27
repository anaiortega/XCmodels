# -*- coding: utf-8 -*-
from postprocess import limit_state_data as lsd
from postprocess.config import default_config

workingDirectory= default_config.findWorkingDirectory()+'/'
execfile(workingDirectory+'model_gen.py') #FE model generation
lsd.LimitStateData.envConfig= cfg

#Reinforced concrete sections on each element.
#reinfConcreteSections= RC_material_distribution.loadRCMaterialDistribution()

#Steel beams definition
execfile(workingDirectory+'steel_beams_def.py')

#Set of entities for which checking is going to be performed.
setCalc= overallSet

loadCombinations= prep.getLoadHandler.getLoadCombinations

#Limit states to calculate internal forces for.
limitStates= [lsd.normalStressesResistance, # Normal stresses resistance.
lsd.shearResistance, # Shear stresses resistance (IS THE SAME AS NORMAL STRESSES, THIS IS WHY IT'S COMMENTED OUT).
lsd.freqLoadsCrackControl, # RC crack control under frequent loads
lsd.quasiPermanentLoadsCrackControl, # RC crack control under quasi-permanent loads
lsd.fatigueResistance # Fatigue resistance.
] 

#limitStates= [lsd.freqLoadsCrackControl]

for ls in limitStates:
  ls.saveAll(FEcase,combContainer,setCalc,lstSteelBeams=[col01a,col01b,col02a,col02b,col03,beam01])
  print 'combinations for ', ls.label, ': ', loadCombinations.getKeys()


