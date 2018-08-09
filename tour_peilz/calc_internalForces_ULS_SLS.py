# -*- coding: utf-8 -*-
import os
from postprocess import limit_state_data as lsd
from model.sets import sets_mng as sUtils

execfile("xc_model_data.py")
lsd.LimitStateData.internal_forces_results_directory= './results/internalForces/'

#RC sections definition.
execfile('sectionsDef.py')

#Define section for each element (spatial distribution of RC sections).
reinfConcreteSectionDistribution.assign(elemSet= floor30_elements.getElements, setRCSects= slab30RCSect)
reinfConcreteSectionDistribution.assign(elemSet= floor40_elements.getElements, setRCSects= slab40RCSect)
reinfConcreteSectionDistribution.assign(elemSet= lateral30_elements.getElements, setRCSects= wall30RCSect)
reinfConcreteSectionDistribution.assign(elemSet= lateral40_elements.getElements, setRCSects= wall40RCSect)
reinfConcreteSectionDistribution.assign(elemSet= roof_elements.getElements, setRCSects= deckRCSect)

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
  ls.saveAll(feProblem=tourRamps,combContainer=combContainer,setCalc= elementsWithSection,fConvIntForc= 1.0)
  print 'combinations for ', ls.label, ': ', loadCombinations.getKeys()

