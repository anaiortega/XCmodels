# -*- coding: utf-8 -*-
import os
from postprocess import limit_state_data as lsd
from solution import predefined_solutions


execfile("model_data.py")

#RC sections definition.
execfile("sectionsDef.py")
lsd.LimitStateData.envConfig= cfg

#Define section names for each element.

preprocessor= FEcase.getPreprocessor
reinfConcreteSectionDistribution.assign(elemSet=deckSet.elements,setRCSects=deckRCSects)
reinfConcreteSectionDistribution.assign(elemSet=parapetBodySet.elements,setRCSects=parapetBodyRCSects)
reinfConcreteSectionDistribution.assign(elemSet=parapetHeadSet.elements,setRCSects=parapetHeadRCSects)

reinfConcreteSectionDistribution.dump()

#Set of entities for which checking is going to be performed.
#setCalc= shellElements.elSet
setCalc= shells

loadCombinations= preprocessor.getLoadHandler.getLoadCombinations

#Limit states to calculate internal forces for.
limitStates= [lsd.normalStressesResistance, # Normal stresses resistance.
lsd.shearResistance, # Shear stresses resistance (IS THE SAME AS NORMAL STRESSES, THIS IS WHY IT'S COMMENTED OUT).
#lsd.freqLoadsCrackControl, # RC crack control under frequent loads
#lsd.quasiPermanentLoadsCrackControl, # RC crack control under quasi-permanent loads
#lsd.fatigueResistance # Fatigue resistance.
] 


# solution= predefined_solutions.SolutionProcedure()
# solution.convergenceTestTol= 1.0e-2
# solution.maxNumIter= 100
# solution.printFlag= 1

#customSolProcType= redefined_solutions.PenaltyNewtonRaphson
customSolProcType= redefined_solutions.SimpleStaticLinear

for ls in limitStates:
    ls.saveAll(combContainer,setCalc, solutionProcedureType= customSolProcType)
    print 'combinations for ', ls.label, ': ', loadCombinations.getKeys()


