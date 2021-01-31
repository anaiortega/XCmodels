# -*- coding: utf-8 -*-
import os
from postprocess import limit_state_data as lsd


model_path="../"
#Project directory structure
exec(open(model_path+'env_config.py').read()))
lsd.LimitStateData.envConfig= cfg

modelDataInputFile=model_path+"model_data.py" #data for FE model generation
exec(open(modelDataInputFile).read()))

#RC sections definition.
exec(open("../sectionsDef.py").read()))

#Define section names for each element.

preprocessor= FEcase.getPreprocessor
reinfConcreteSectionDistribution.assign(elemSet=deck.elements,setRCSects=deckRCSects)
reinfConcreteSectionDistribution.assign(elemSet=found.elements,setRCSects=foundRCSects)
reinfConcreteSectionDistribution.assign(elemSet=wall.elements,setRCSects=wallRCSects)
reinfConcreteSectionDistribution.assign(elemSet=beamX.elements,setRCSects=beamXRCsect)
reinfConcreteSectionDistribution.assign(elemSet=beamY.elements,setRCSects=beamYRCsect)
reinfConcreteSectionDistribution.assign(elemSet=columnZ.elements,setRCSects=columnZRCsect)

reinfConcreteSectionDistribution.dump()

#Set of entities for which checking is going to be performed.
setCalc= overallSet
#setCalc= deck

loadCombinations= preprocessor.getLoadHandler.getLoadCombinations

#Limit states to calculate internal forces for.
limitStates= [lsd.normalStressesResistance, # Normal stresses resistance.
lsd.shearResistance, # Shear stresses resistance (IS THE SAME AS NORMAL STRESSES, THIS IS WHY IT'S COMMENTED OUT).
lsd.freqLoadsCrackControl, # RC crack control under frequent loads
lsd.quasiPermanentLoadsCrackControl, # RC crack control under quasi-permanent loads
lsd.fatigueResistance # Fatigue resistance.
] 

#limitStates= [lsd.freqLoadsCrackControl]

for ls in limitStates:
  ls.saveAll(combContainer,setCalc)
  print 'combinations for ', ls.label, ': ', loadCombinations.getKeys()
quit()

