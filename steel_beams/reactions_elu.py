# -*- coding: utf-8 -*-


exec(open('model_data.py').read()))

from postprocess import get_reactions as gr

reactions= {}

def resultComb(prb,nmbComb):
  preprocessor= prb.getPreprocessor   
  preprocessor.resetLoadCase()
  preprocessor.getLoadHandler.addToDomain(nmbComb)
  #Solución
  solution= predefined_solutions.SolutionProcedure()
  analysis= solution.simpleStaticLinear(prb)
  result= analysis.analyze(1)
  reactions= gr.Reactions(preprocessor,supportNodes)
  forces= reactions.getReactionForces()
  for key in forces:
    reac= forces[key]
    print "Appui ", key , nmbComb, reac*1e-3, " (kN)"
    #print "M= ", tmp[2]/1e3
  preprocessor.getLoadHandler.removeFromDomain(nmbComb)
  return reactions


analysis= predefined_solutions.simple_static_linear(mainBeam)


combContainer.dumpCombinations(preprocessor)
resultComb(mainBeam,"ELU00")
resultComb(mainBeam,"ELU01")
resultComb(mainBeam,"ELU02")
resultComb(mainBeam,"ELU03")


orderedSupports= dict()
print 'supportNodes: '
for n in supportNodes:
  orderedSupports[n.getInitialPos3d.x]= n.tag

for key in sorted(orderedSupports):
  print 'x= ', key, ' tag= ', orderedSupports[key]
