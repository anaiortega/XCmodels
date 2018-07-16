# -*- coding: utf-8 -*-
import os
from postprocess import limit_state_data as lsd
from postprocess import element_section_map

model_path="../"
#Project directory structure
execfile(model_path+'project_directories.py')
lsd.LimitStateData.internal_forces_results_directory= '../'+internal_forces_results_directory

modelDataInputFile=model_path+"model_data.py" #data for FE model generation
execfile(modelDataInputFile)


#Define section names for each element.
mapSectionsForEveryElement= ElementSectionMap.ShellElementSectionMap()
preprocessor= model.getPreprocessor()
mapSectionsForEveryElement.assign(preprocessor.getSets.getSet('wallBasYmin').getElements,'wallBasYmin')
mapSectionsForEveryElement.assign(preprocessor.getSets.getSet('wallBasYmax').getElements,'wallBasYmax')
mapSectionsForEveryElement.assign(preprocessor.getSets.getSet('wallBasXmin').getElements,'wallBasXmin')
mapSectionsForEveryElement.assign(preprocessor.getSets.getSet('wallBasXmax').getElements,'wallBasXmax')
mapSectionsForEveryElement.assign(preprocessor.getSets.getSet('columnFacYmin').getElements,'columnFacYmin')
mapSectionsForEveryElement.assign(preprocessor.getSets.getSet('columnFacYmax').getElements,'columnFacYmax')
mapSectionsForEveryElement.assign(preprocessor.getSets.getSet('columnFacXmin').getElements,'columnFacXmin')
mapSectionsForEveryElement.assign(preprocessor.getSets.getSet('columnFacXmax').getElements,'columnFacXmax')
mapSectionsForEveryElement.assign(preprocessor.getSets.getSet('ShearWallStaircaseXmin').getElements,'ShearWallStaircaseXmin')
mapSectionsForEveryElement.assign(preprocessor.getSets.getSet('ShearWallStaircaseXmax').getElements,'ShearWallStaircaseXmax')
mapSectionsForEveryElement.assign(preprocessor.getSets.getSet('ShearWallStaircaseZ').getElements,'ShearWallStaircaseZ')
mapSectionsForEveryElement.assign(preprocessor.getSets.getSet('SlabLevelBas1').getElements,'SlabLevelBas1')
mapSectionsForEveryElement.assign(preprocessor.getSets.getSet('SlabLevel0').getElements,'SlabLevel0')
mapSectionsForEveryElement.assign(preprocessor.getSets.getSet('SlabLevel1').getElements,'SlabLevel1')
mapSectionsForEveryElement.assign(preprocessor.getSets.getSet('SlabLevel2').getElements,'SlabLevel2')
mapSectionsForEveryElement.assign(preprocessor.getSets.getSet('SlabLevel3').getElements,'SlabLevel3')
mapSectionsForEveryElement.assign(preprocessor.getSets.getSet('SlabLevel4').getElements,'SlabLevel4')
mapSectionsForEveryElement.assign(preprocessor.getSets.getSet('SlabLevel5').getElements,'SlabLevel5')
mapSectionsForEveryElement.assign(preprocessor.getSets.getSet('SlabLevel6').getElements,'SlabLevel6')
mapSectionsForEveryElement.assign(preprocessor.getSets.getSet('columnB2').getElements,'columnB2')
mapSectionsForEveryElement.assign(preprocessor.getSets.getSet('columnB3').getElements,'columnB3')
mapSectionsForEveryElement.assign(preprocessor.getSets.getSet('columnB4').getElements,'columnB4')
mapSectionsForEveryElement.assign(preprocessor.getSets.getSet('columnB5').getElements,'columnB5')

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

