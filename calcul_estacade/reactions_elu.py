# -*- coding: utf-8 -*-


exec(open('model_data.py').read())

from postprocess import get_reactions as gr

supportNodes= list()


for pos in footingPositions:
  n= xcTotalSet.getNearestNode(geom.Pos3d(pos[0],pos[1],pos[2]))
  supportNodes.append(n)

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


analysis= predefined_solutions.simple_static_linear(gilamontDock)


combContainer.dumpCombinations(preprocessor)
resultComb(gilamontDock,"ELU2A")
resultComb(gilamontDock,"ELU2B")
resultComb(gilamontDock,"ELU3A")
resultComb(gilamontDock,"ELU3B")
resultComb(gilamontDock,"ELU4A")
resultComb(gilamontDock,"ELU4B")
resultComb(gilamontDock,"ELU5A")
resultComb(gilamontDock,"ELU5B")
resultComb(gilamontDock,"ELU6A")
resultComb(gilamontDock,"ELU6B")


orderedSupports= dict()
print 'supportNodes: '
for n in supportNodes:
  orderedSupports[n.getInitialPos3d.x]= n.tag

for key in sorted(orderedSupports):
  print 'x= ', key, ' tag= ', orderedSupports[key]
