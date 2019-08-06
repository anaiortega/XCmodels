# -*- coding: utf-8 -*-

from solution import predefined_solutions

execfile('model_data.py')

resistingForces= list()

def resultComb(prb,nmbComb):
    preprocessor= prb.getPreprocessor   
    preprocessor.resetLoadCase()
    preprocessor.getLoadHandler.getLoadCombinations.addToDomain(nmbComb)
    #Solución
    solution= predefined_solutions.SolutionProcedure()
    analysis= solution.simpleStaticLinear(prb)
    result= analysis.analyze(1)
    for e in abutmentBearingElements.elements:
        row=[nmbComb, 'abutment']
        row.append(e.tag)
        rf= e.getResistingForce()
        for i in range(0,6):
            row.append(rf[i])
        resistingForces.append(row)
    for e in pierBearingElements.elements:
        row=[nmbComb, 'pier']
        row.append(e.tag)
        rf= e.getResistingForce()
        for i in range(0,6):
            row.append(rf[i])
        resistingForces.append(row)
    preprocessor.getLoadHandler.getLoadCombinations.removeFromDomain(nmbComb)



analisis= predefined_solutions.simple_static_linear(model)


combContainer.dumpCombinations(preprocessor)
resultComb(model,"ELU01")
resultComb(model,"ELU02")
resultComb(model,"ELU03")
resultComb(model,"ELU04")
resultComb(model,"ELU05")
resultComb(model,"ELU06")
resultComb(model,"ELU07")
resultComb(model,"ELU08")

import csv
with open('bearing_resisting_forces.csv','w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(resistingForces)

resistingForces= list()
resultComb(model,"A")
import csv
with open('bearing_resisting_forces_during_earthquake.csv','w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(resistingForces)



