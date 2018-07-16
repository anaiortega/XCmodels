# -*- coding: utf-8 -*-

execfile('../model_data.py')

from solution import predefined_solutions

def resultAction(model,nmbAction):
  preprocessor= model.getPreprocessor()
  loadCases= preprocessor.getLoadHandler.getLoadPatterns
  preprocessor.resetLoadCase()
  loadCases.addToDomain(nmbAction)
  #Solución
  analisis= predefined_solutions.simple_static_linear(model.getFEProblem())
  result= analisis.analyze(1)
  loadCases.removeFromDomain(nmbAction)

#List of load ids.
lps= model.getPreprocessor().getLoadHandler.getLoadPatterns.getKeys()
print 'load patterns= ', lps

center_of_mass= foundationElasticSupports.getCenterOfMass()
print 'center_of_mass= ', center_of_mass
for lp in lps:
  resultAction(model,lp)
  reac= foundationElasticSupports.calcPressures().reduceTo(center_of_mass)
  print "load: ", lp, " reac= ", reac
