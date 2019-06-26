# -*- coding: utf-8 -*-


execfile('basement_wall_2.py')

from postprocess.reports import common_formats as fmt

reactions= {}
forces= None


#Serviceability analysis.
combContainer.dumpCombinations(preprocessor)
sls_results= wall.performSLSAnalysis(['ELS00'])
print 'SLS results= ', sls_results.rotation, sls_results.rotationComb
wall.setSLSInternalForcesEnvelope(sls_results.internalForces)

#ULS stability analysis.
sr= wall.performStabilityAnalysis(['SR102A', 'SR102B', 'SR103A', 'SR103B', 'SR103C', 'SR104A', 'SR104B', 'SR105A', 'SR105B'],foundationSoilModel, sg_adm)

#ULS strength analysis.
uls_results= wall.performULSAnalysis(['SR102A', 'SR102B', 'SR103A', 'SR103B', 'SR103C', 'SR104A', 'SR104B', 'SR105A', 'SR105B'])
wall.setULSInternalForcesEnvelope(uls_results.internalForces)

pth= "./results/"
# fsr= open(pth+'verification_results.tex','w')
# sr.writeOutput(fsr)
# fsr.close()

wall.writeResult(pth)
wall.drawSchema(pth)
