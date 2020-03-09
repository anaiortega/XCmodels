!# -*- coding: utf-8 -*-


execfile('model_data.py')
lsd.LimitStateData.envConfig= cfg
from materials.ec3 import EC3Beam as ec3b

crossSectionClass= 1
ec3beams= list()
for key in lineDict:
  ec3beams.append(ec3b.EC3Beam(lineDict[key],IPE450A))

for l in ec3beams:
  l.installULSControlRecorder("element_prop_recorder",crossSectionClass)

analysis= predefined_solutions.simple_static_linear(mainBeam)


combContainer.dumpCombinations(preprocessor)
prb=mainBeam
nmbComb="ELU00"


preprocessor.resetLoadCase()
preprocessor.getLoadHandler.addToDomain(nmbComb)
#Solución
solution= predefined_solutions.SolutionProcedure()
analysis= solution.simpleStaticLinear(prb)
result= analysis.analyze(1)

l=ec3beams[0]
l.getLateralBucklingReductionFactor(1)

for l in ec3beams:
    l.updateLateralBucklingReductionFactor(crossSectionClass)
result= analysis.analyze(1) #Update resistant values 
#  preprocessor.getLoadHandler.removeFromDomain(nmbComb)


