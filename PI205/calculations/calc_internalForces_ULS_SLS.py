# -*- coding: utf-8 -*-
import os
from postprocess import limit_state_data as lsd

model_path="../"
#Project directory structure
exec(open(model_path+'env_config.py').read())
lsd.LimitStateData.envConfig= cfg

modelDataInputFile=model_path+"model_data.py" #data for FE model generation
exec(open(modelDataInputFile).read())

#RC sections definition.
exec(open(model_path+'sectionsDef.py').read())

#Define section for each element (spatial distribution of RC sections).
preprocessor= prep
reinfConcreteSectionDistribution.assign(elemSet=preprocessor.getSets.getSet('foundExtSlab').elements,setRCSects=FoundExtSlabRCSect)
reinfConcreteSectionDistribution.assign(elemSet=preprocessor.getSets.getSet('foundIntSlab').elements,setRCSects=FoundIntSlabRCSect)
reinfConcreteSectionDistribution.assign(elemSet=preprocessor.getSets.getSet('leftWall').elements,setRCSects=LeftWallRCSect)
reinfConcreteSectionDistribution.assign(elemSet=preprocessor.getSets.getSet('rightWall').elements,setRCSects=RightWallRCSect)
reinfConcreteSectionDistribution.assign(elemSet=preprocessor.getSets.getSet('deckExtSlab').elements,setRCSects=DeckExtSlabRCSect)
reinfConcreteSectionDistribution.assign(elemSet=preprocessor.getSets.getSet('deckIntSlab').elements,setRCSects=DeckIntSlabRCSect)

reinfConcreteSectionDistribution.dump()

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
  ls.saveAll(combContainer=combContainer,setCalc=setCalc)
  print 'combinations for ', ls.label, ': ', loadCombinations.getKeys()

