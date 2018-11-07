# -*- coding: utf-8 -*-
#Calculates ELU01 combination

execfile('model_data.py')
def resultComb(prb,nmbComb):
  preprocessor.resetLoadCase()
  preprocessor.getLoadHandler.getLoadCombinations.addToDomain(nmbComb)
  #Solución
  solution= predefined_solutions.SolutionProcedure()
  analysis= solution.simpleStaticLinear(prb)
  result= analysis.analyze(1)
  preprocessor.getLoadHandler.getLoadCombinations.removeFromDomain(nmbComb)


combContainer.dumpCombinations(preprocessor)
resultComb(mainBeam,'ELU01')
