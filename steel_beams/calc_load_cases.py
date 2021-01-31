# -*- coding: utf-8 -*-
# This script calculates and prints reactions on bearings for each load case


exec(open('model_data.py').read())
def resultAction(prb,nmbAction):
  prb.getPreprocessor.resetLoadCase()
  prb.getPreprocessor.getLoadHandler.addToDomain(nmbAction)
  #Solución
  solution= predefined_solutions.SolutionProcedure()
  analysis= solution.simpleStaticLinear(prb)
  result= analysis.analyze(1)
  prb.getPreprocessor.getLoadHandler.removeFromDomain(nmbAction)

from postprocess import get_reactions as gr
 
def getReactions(prb,nmbAction):
  preprocessor= prb.getPreprocessor   
  resultAction(prb,nmbAction)
  reactions= gr.Reactions(preprocessor,supportNodes)
  forces= reactions.getReactionForces()
  for key in forces:
    reac= forces[key]
    print "Appui ", key , nmbAction, reac*1e-3, " (kN)"
    #print "M= ", tmp[2]/1e3
  return reactions

reactions= {}

for lc in loadCaseNames:
  r= getReactions(mainBeam,lc)
  reactions[lc]= r
  R= r.getResultant().reduceTo(pt[10].getPos)
  print 'lc= ', lc, ' resultant: ', R

