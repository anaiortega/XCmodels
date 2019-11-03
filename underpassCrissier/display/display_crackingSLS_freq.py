# -*- coding: utf-8 -*-
from postprocess.control_vars import *


model_path="../"
#Project directory structure
execfile(model_path+'project_directories.py')

modelDataInputFile=model_path+"model_data.py" #data for FE model generation
execfile(modelDataInputFile)


#Load properties to display:
preprocessor= model.getPreprocessor()
fName= model_path+check_results_directory+'verifRsl_crackingSLS_freq.py'
execfile(fName)
execfile('../captionTexts.py')


limitStateLabel= lsd.freqLoadsCrackControl.label
argument= 'getMaxSteelStress'
#argument= 'crackControlVarsNeg.steelStress'

setDisp= deckSet
#setDisp= leftWallSet
#setDisp= rightWallSet
#setDisp= foundationSet 

oh= output_handler.OutputHandler(modelSpace)
oh.outputStyle.cameraParameters= cameraParameters
oh.displayFieldDirs1and2(limitStateLabel,argument,setToDisplay=setDisp,component=None, fileName= None)




