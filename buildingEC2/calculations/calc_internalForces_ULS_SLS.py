# -*- coding: utf-8 -*-
import os
from postprocess import limit_state_data as lsd
from postprocess import element_section_map

model_path="../"
#Project directory structure
execfile(model_path+'env_config.py')
lsd.LimitStateData.internal_forces_results_directory= cfg.projectDirTree.intForcPath

modelDataInputFile=model_path+"model_data.py" #data for FE model generation
execfile(modelDataInputFile)


#Define section names for each element.
mapSectionsForEveryElement= ElementSectionMap.ShellElementSectionMap()
preprocessor= model.getPreprocessor()
mapSectionsForEveryElement.assign(preprocessor.getSets.getSet('wallBasYmin').elements,'wallBasYmin')
mapSectionsForEveryElement.assign(preprocessor.getSets.getSet('wallBasYmax').elements,'wallBasYmax')
mapSectionsForEveryElement.assign(preprocessor.getSets.getSet('wallBasXmin').elements,'wallBasXmin')
mapSectionsForEveryElement.assign(preprocessor.getSets.getSet('wallBasXmax').elements,'wallBasXmax')
mapSectionsForEveryElement.assign(preprocessor.getSets.getSet('columnFacYmin').elements,'columnFacYmin')
mapSectionsForEveryElement.assign(preprocessor.getSets.getSet('columnFacYmax').elements,'columnFacYmax')
mapSectionsForEveryElement.assign(preprocessor.getSets.getSet('columnFacXmin').elements,'columnFacXmin')
mapSectionsForEveryElement.assign(preprocessor.getSets.getSet('columnFacXmax').elements,'columnFacXmax')
mapSectionsForEveryElement.assign(preprocessor.getSets.getSet('ShearWallStaircaseXmin').elements,'ShearWallStaircaseXmin')
mapSectionsForEveryElement.assign(preprocessor.getSets.getSet('ShearWallStaircaseXmax').elements,'ShearWallStaircaseXmax')
mapSectionsForEveryElement.assign(preprocessor.getSets.getSet('ShearWallStaircaseZ').elements,'ShearWallStaircaseZ')
mapSectionsForEveryElement.assign(preprocessor.getSets.getSet('SlabLevelBas1').elements,'SlabLevelBas1')
mapSectionsForEveryElement.assign(preprocessor.getSets.getSet('SlabLevel0').elements,'SlabLevel0')
mapSectionsForEveryElement.assign(preprocessor.getSets.getSet('SlabLevel1').elements,'SlabLevel1')
mapSectionsForEveryElement.assign(preprocessor.getSets.getSet('SlabLevel2').elements,'SlabLevel2')
mapSectionsForEveryElement.assign(preprocessor.getSets.getSet('SlabLevel3').elements,'SlabLevel3')
mapSectionsForEveryElement.assign(preprocessor.getSets.getSet('SlabLevel4').elements,'SlabLevel4')
mapSectionsForEveryElement.assign(preprocessor.getSets.getSet('SlabLevel5').elements,'SlabLevel5')
mapSectionsForEveryElement.assign(preprocessor.getSets.getSet('SlabLevel6').elements,'SlabLevel6')
mapSectionsForEveryElement.assign(preprocessor.getSets.getSet('columnB2').elements,'columnB2')
mapSectionsForEveryElement.assign(preprocessor.getSets.getSet('columnB3').elements,'columnB3')
mapSectionsForEveryElement.assign(preprocessor.getSets.getSet('columnB4').elements,'columnB4')
mapSectionsForEveryElement.assign(preprocessor.getSets.getSet('columnB5').elements,'columnB5')

mapSectionsForEveryElement.dump()

#Set of entities for which analysis is going to be performed.
#setCalc= allSet
setCalc= shellSet
loadCombinations= preprocessor.getLoadHandler.getLoadCombinations

#Limit states to calculate internal forces for.
# limitStates= [lsd.normalStressesResistance, # Normal stresses resistance.
# lsd.shearResistance, # Shear stresses resistance (IS THE SAME AS NORMAL STRESSES, THIS IS WHY IT'S COMMENTED OUT).
# lsd.freqLoadsCrackControl, # RC crack control under frequent loads
# lsd.quasiPermanentLoadsCrackControl, # RC crack control under quasi-permanent loads
# lsd.fatigueResistance # Fatigue resistance.
# ] 
limitStates= [lsd.normalStressesResistance] # Normal stresses resistance.

for ls in limitStates:
  ls.saveAll(model.getFEProblem(),combContainer,setCalc)
  print 'combinations for ', ls.label, ': ', loadCombinations.getKeys()

