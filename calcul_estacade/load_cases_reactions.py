# -*- coding: utf-8 -*-
import xc_base
import geom

exec(open("model_data.py").read()))

def resultAction(nmbAction):
  preprocessor.resetLoadCase()
  loadCases.addToDomain(nmbAction)
  #Solución
  analysis= predefined_solutions.simple_static_linear(gilamontDock)
  result= analysis.analyze(1)
  loadCases.removeFromDomain(nmbAction)

def getReaction(preprocessor,nmbAction,nodeSet):
  resultAction(nmbAction)
  retval= xc.Vector([0,0,0])
  #m= xc.Vector([0,0,0])
  dispXYZ= xc.Vector([0,0,0])
  dispXMax= -1e6
  dispXMin= 1e6
  dispYMax= -1e6
  dispYMin= 1e6
  dispZMax= -1e6
  dispZMin= 1e6
  meshNodes= preprocessor.getNodeHandler
  meshNodes.calculateNodalReactions(True,1e-6)
  for n in nodeSet:
    tmp= n.getDisp
    dispXYZ+= xc.Vector([tmp[0],tmp[1],tmp[2]])
    dispXMax= max(dispXMax,tmp[0])
    dispXMin= min(dispXMin,tmp[0])
    dispYMax= max(dispYMax,tmp[1])
    dispYMin= min(dispYMin,tmp[1])
    dispZMax= max(dispZMax,tmp[2])
    dispZMin= min(dispZMin,tmp[2])
  dispXYZ/= len(nodeSet)
  for n in fixedNodes:
    tmp= n.getReaction
    retval+= xc.Vector([tmp[0],tmp[1],tmp[2]])
    #m+= xc.Vector([tmp[3],tmp[4],tmp[5]])
    #print "Support ", n.tag , nmbAction, "[", tmp[0]/1e3, tmp[1]/1e3, tmp[2]/1e3, "] (kN)"
  print "Action= ", nmbAction
  print "  max X disp.= ", dispXMax*1e3, " mm"
  print "  min X disp.= ", dispXMin*1e3, " mm"
  print "  max Y disp.= ", dispYMax*1e3, " mm"
  print "  min Y disp.= ", dispYMin*1e3, " mm"
  print "  max Z disp.= ", dispZMax*1e3, " mm"
  print "  min Z disp.= ", dispZMin*1e3, " mm"
  print "  average disp. = ", dispXYZ*1e3, " mm"
  #print "  m= ", m/1e3, " kN.m"
  print "  retval= ", retval/1e3, " kN"
  return retval

nodeSet= setDeck.nodes
reactions= {}
for lcName in loadCaseNames:
  reactions[lcName]= getReaction(preprocessor,lcName,nodeSet)
#reactionG= getReaction(preprocessor,'selfWeight',nodeSet)
#reactionGaster= getReaction(preprocessor,'deadLoad',nodeSet)
#reactionShrinkage= getReaction(preprocessor,'shrinkage',nodeSet)
#reactionLiveLoadA= getReaction(preprocessor,'liveLoadA',nodeSet)
#reactionLiveLoadB= getReaction(preprocessor,'liveLoadB',nodeSet)
#reactionTemperature= getReaction(preprocessor,'temperature',nodeSet)
#reactionSnowLoad= getReaction(preprocessor,'snowLoad',nodeSet)
#reactionEarthquake= getReaction(preprocessor,'earthquake',nodeSet)
# reactionLM5= getReaction(preprocessor,"LM5",nodeSet)
# reactionLM6= getReaction(preprocessor,"LM6",nodeSet)
# reactionLM7= getReaction(preprocessor,"LM7",nodeSet)
# reactionLM8= getReaction(preprocessor,"LM8",nodeSet)
# reactionLM7DF= getReaction(preprocessor,"LM7DF",nodeSet)
# reactionLM7FC= getReaction(preprocessor,"LM7FC",nodeSet)
#reactionV= getReaction(preprocessor,"V",nodeSet)
#reactionTPos= getReaction(preprocessor,"TNeg",nodeSet)
#reactionTPos= getReaction(preprocessor,"TPos",nodeSet)
#reactionLM6DR1= getReaction(preprocessor,"LM6DR1",nodeSet)
#reactionLM7DR1= getReaction(preprocessor,"LM7DR1",nodeSet)
#reactionLMDR2= getReaction(preprocessor,"LMDR2",nodeSet)
#reactionChoc= getReaction(preprocessor,"Choc",nodeSet)
#reactionS= getReaction(preprocessor,"S",nodeSet)

