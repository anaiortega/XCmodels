# -*- coding: utf-8 -*-


exec(open('retaining_wall.py').read())

from postprocess.reports import common_formats as fmt

reactions= {}
forces= None


#Serviceability analysis.
combContainer.dumpCombinations(preprocessor)
sls_results= wall.performSLSAnalysis(['ELS00','ELS01'])
print 'SLS results= ', sls_results.rotation, sls_results.rotationComb
wall.setSLSInternalForcesEnvelope(sls_results.internalForces)

#ULS stability analysis.
sr= wall.performStabilityAnalysis(['SR1A','SR1B','SR2','SR3A','SR3B','SR4','SR5A','SR5B','SR6','SR7A','SR7B','SRS1A','SRS1B','SRS1C'],foundationSoilModel)

#ULS strength analysis.
uls_results= wall.performULSAnalysis(['SR9A', 'SR9B', 'SR10', 'SR11A', 'SR11B', 'SR12', 'SR13A', 'SR13B', 'SR14', 'SR15A', 'SR15B', 'SRS2A', 'SRS2B', 'SRS2C'])
wall.setULSInternalForcesEnvelope(uls_results.internalForces)

pth= "./results/"
# fsr= open(pth+'verification_results.tex','w')
# sr.writeOutput(fsr)
# fsr.close()

wall.writeResult(pth)
wall.drawSchema(pth)
