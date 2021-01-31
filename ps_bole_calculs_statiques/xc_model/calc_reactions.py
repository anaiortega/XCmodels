# -*- coding: utf-8 -*-


exec(open('fe_model.py').read()))

from postprocess import get_reactions as gr

def resultComb(prb,nmbComb):
  preprocessor= prb.getPreprocessor   
  preprocessor.resetLoadCase()
  preprocessor.getLoadHandler.addToDomain(nmbComb)
  #Solución
  solution= predefined_solutions.SolutionProcedure()
  analysis= solution.simpleStaticLinear(prb)
  result= analysis.analyze(1)
  spandrelReactions= gr.Reactions(preprocessor,spandrelFixedNodes)
  spandrelForces= spandrelReactions.getReactionForces()
  for key in spandrelForces:
    reac= spandrelForces[key]
    print "Support ", key , nmbComb, reac*1e-3, " (kN)"
    #print "M= ", tmp[2]/1e3
  fillReactions= gr.Reactions(preprocessor,fillFixedNodes)
  fillForces= fillReactions.getReactionForces()
  for key in fillForces:
    reac= fillForces[key]
    print "Support ", key , nmbComb, reac*1e-3, " (kN)"
    #print "M= ", tmp[2]/1e3
  preprocessor.getLoadHandler.removeFromDomain(nmbComb)
  return spandrelReactions, fillReactions


analysis= predefined_solutions.simple_static_linear(deck)


combContainer.dumpCombinations(preprocessor)
spandrelReactions, fillReactions= resultComb(deck,"PP")

orderedSupports= dict()
print 'spandrelFixedNodes positions: '
for n in spandrelFixedNodes:
  orderedSupports[n.getInitialPos3d.x]= n.tag

for key in sorted(orderedSupports):
  print 'x= ', key, ' tag= ', orderedSupports[key]

orderedSupports= dict()
print 'fillFixedNodes positions: '
for n in fillFixedNodes:
  orderedSupports[n.getInitialPos3d.x]= n.tag

for key in sorted(orderedSupports):
  print 'x= ', key, ' tag= ', orderedSupports[key]

svdSpandrelReactions= spandrelReactions.getResultant().reduceTo(geom.Pos3d(xCenter,0,0))
svdFillReactions= fillReactions.getResultant().reduceTo(geom.Pos3d(xCenter,0,0))
svdTotalReaction= (svdSpandrelReactions+svdFillReactions).reduceTo(geom.Pos3d(xCenter,0,0))
print 'spandrel reactions: ', svdSpandrelReactions
print  'fill reactions: ', svdFillReactions
print 'total reaction: ', svdTotalReaction

#print impactLoad
print deckUnitWeight*totalLength

