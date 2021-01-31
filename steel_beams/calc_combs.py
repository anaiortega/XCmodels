# -*- coding: utf-8 -*-
#Calculates ELU01 combination

exec(open('model_data.py').read())
def resultComb(prb,nmbComb):
  preprocessor.resetLoadCase()
  preprocessor.getLoadHandler.addToDomain(nmbComb)
  #Solución
  solution= predefined_solutions.SolutionProcedure()
  analysis= solution.simpleStaticLinear(prb)
  result= analysis.analyze(1)
  preprocessor.getLoadHandler.removeFromDomain(nmbComb)


combContainer.dumpCombinations(preprocessor)
resultComb(mainBeam,'ELU01')
