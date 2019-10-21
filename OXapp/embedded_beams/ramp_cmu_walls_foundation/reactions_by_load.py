# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division

#execfile('ramp_cover_reactions.py')
execfile('ramp_cover_reactions_alcove.py')

from postprocess import get_reactions as gr

supportNodes= list()


reactions= {}

def resultLoadCase(prb,nmbLoadCase):
    preprocessor= prb.getPreprocessor   
    preprocessor.resetLoadCase()
    preprocessor.getLoadHandler.addToDomain(nmbLoadCase)
    #Solución
    solution= predefined_solutions.SolutionProcedure()
    analysis= solution.simpleStaticLinear(prb)
    result= analysis.analyze(1)
    nodes.calculateNodalReactions(True,1e-7)
    #print(nmbLoadCase,' RA= ', p0.getNode().getReaction[1]/1e3, ' kN/m, RB= ', p3.getNode().getReaction[1]/1e3,' kN/m')
    print(nmbLoadCase,' RA= ', p0.getNode().getReaction[1]/1e3,' RB= ', (p3a.getNode().getReaction[1]+p3b.getNode().getReaction[1])/1e3, ' kN/m, RC= ', p4.getNode().getReaction[1]/1e3,' kN/m')
    preprocessor.getLoadHandler.removeFromDomain(nmbLoadCase)
    return reactions



for name in loadCaseNames:
    resultLoadCase(precastPlanks,name)
