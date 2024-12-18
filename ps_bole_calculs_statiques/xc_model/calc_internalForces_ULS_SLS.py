# -*- coding: utf-8 -*-
import os
from postprocess import limit_state_data as lsd
from model.sets import sets_mng as sUtils

model_path="./"
#Project directory structure
exec(open(model_path+'env_config.py').read())
lsd.LimitStateData.envConfig= cfg

modelDataInputFile=model_path+"fe_model.py" #data for FE model generation
exec(open(modelDataInputFile).read())

#RC sections definition.
exec(open(model_path+'sectionsDef.py').read())

#Define section for each element (spatial distribution of RC sections).
reinfConcreteSectionDistribution.assign(elemSet= deckSet.elements, setRCSects= deckSlabRCSect)
reinfConcreteSectionDistribution.assign(elemSet= parapetSet.elements, setRCSects= parapetRCSect)
# reinfConcreteSectionDistribution.assign(elemSet= setDock.elements, setRCSects= dockRCSect)
# reinfConcreteSectionDistribution.assign(elemSet= setParapet.elements, setRCSects= parapetRCSect)
# reinfConcreteSectionDistribution.assign(elemSet= setColumns.elements, setRCSects= columnRCSect)
# reinfConcreteSectionDistribution.assign(elemSet= setTransverseReinforcements.elements, setRCSects= transverseReinfRCSect)


reinfConcreteSectionDistribution.dump()

#Elements with an assigned section.
elementsWithSection= reinfConcreteSectionDistribution.getElementSet(preprocessor)

loadCombinations= preprocessor.getLoadHandler.getLoadCombinations

#Limit states to calculate internal forces for.
limitStates= [lsd.normalStressesResistance, # Normal stresses resistance.
lsd.shearResistance, # Shear stresses resistance (IS THE SAME AS NORMAL STRESSES, THIS IS WHY IT'S COMMENTED OUT).
lsd.freqLoadsCrackControl, # RC crack control under frequent loads
lsd.quasiPermanentLoadsCrackControl, # RC crack control under quasi-permanent loads
lsd.fatigueResistance # Fatigue resistance.
] 

for ls in limitStates:
  ls.saveAll(combContainer=combContainer, setCalc= elementsWithSection)
  print 'combinations for ', ls.label, ': ', loadCombinations.getKeys()

