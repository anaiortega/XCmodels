# -*- coding: utf-8 -*-
import os
from postprocess import limit_state_data as lsd
from postprocess import element_section_map

model_path="../"
#Project directory structure
exec(open(model_path+'env_config.py').read())
lsd.LimitStateData.envConfig= cfg

modelDataInputFile=model_path+"model_data.py" #data for FE model generation
exec(open(modelDataInputFile).read())


#Define section names for each element.
mapSectionsForEveryElement= ElementSectionMap.ShellElementSectionMap()
preprocessor= model.getPreprocessor()
mapSectionsForEveryElement.assign(preprocessor.getSets.getSet('foundExtSlab').elements,'foundExtSlab')
mapSectionsForEveryElement.assign(preprocessor.getSets.getSet('foundIntSlab').elements,'foundIntSlab')
mapSectionsForEveryElement.assign(preprocessor.getSets.getSet('leftWall').elements,'leftWall')
mapSectionsForEveryElement.assign(preprocessor.getSets.getSet('rightWall').elements,'rightWall')
mapSectionsForEveryElement.assign(preprocessor.getSets.getSet('deckExtSlab').elements,'deckExtSlab')
mapSectionsForEveryElement.assign(preprocessor.getSets.getSet('deckIntSlab').elements,'deckIntSlab')

mapSectionsForEveryElement.dump()

#Set of entities for which analysis is going to be performed.
setCalc= shellElements

loadCombinations= preprocessor.getLoadHandler.getLoadCombinations

#Limit states to calculate internal forces for.
limitStates= [lsd.normalStressesResistance, # Normal stresses resistance.
lsd.shearResistance, # Shear stresses resistance (IS THE SAME AS NORMAL STRESSES, THIS IS WHY IT'S COMMENTED OUT).
lsd.freqLoadsCrackControl, # RC crack control under frequent loads
lsd.quasiPermanentLoadsCrackControl, # RC crack control under quasi-permanent loads
lsd.fatigueResistance # Fatigue resistance.
] 

for ls in limitStates:
  ls.saveAll(combContainer,setCalc)
  print 'combinations for ', ls.label, ': ', loadCombinations.getKeys()

