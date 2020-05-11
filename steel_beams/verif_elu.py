# -*- coding: utf-8 -*-

from postprocess import output_handler

execfile('model_data.py')
#lsd.LimitStateData.envConfig= cfg
from materials.ec3 import EC3Beam as ec3b

crossSectionClass= 1
ec3beams= list()
for key in lineDict:
    l= lineDict[key]
    ec3beams.append(ec3b.EC3Beam(l.name,IPE450A, lstLines= [l]))

def resultComb(prb,nmbComb):
    preprocessor.resetLoadCase()
    preprocessor.getLoadHandler.addToDomain(nmbComb)
    #Solución
    solution= predefined_solutions.SolutionProcedure()
    analysis= solution.simpleStaticLinear(prb)
    result= analysis.analyze(1)
    for l in ec3beams:
      l.updateLateralBucklingReductionFactor()
    result= analysis.analyze(1) #Update resistant values 
    preprocessor.getLoadHandler.removeFromDomain(nmbComb)

# chiLT= 1.0 #Lateral-torsional buckling reduction factor
# recorder= IPE450A.installULSControlRecorder("element_prop_recorder",setMainBeam.elements,crossSectionClass,chiLT)
for l in ec3beams:
  l.installULSControlRecorder("element_prop_recorder",crossSectionClass)

analysis= predefined_solutions.simple_static_linear(mainBeam)


combContainer.dumpCombinations(preprocessor)
resultComb(mainBeam,"ELU00")
resultComb(mainBeam,"ELU01")
#resultComb(mainBeam,"ELU02")
#resultComb(mainBeam,"ELU03")

#########################################################
# Graphic stuff.
oh= output_handler.OutputHandler(modelSpace)

oh.displayElementValueDiagram('chiLT', setToDisplay= setMainBeam)

