# -*- coding: utf-8 -*-

from postprocess.control_vars import *


model_path="../"
#Project directory structure
execfile(model_path+'env_config.py')

modelDataInputFile=model_path+"model_data.py" #data for FE model generation
execfile(modelDataInputFile)


#Load properties to display:
preprocessor= model.getPreprocessor()
fName=  cfg.projectDirTree.getVerifCrackQpermFile()
execfile(fName)
execfile('../captionTexts.py')

limitStateLabel= lsd.quasiPermanentLoadsCrackControl.label

#Possible arguments: 'getCF', 'getMaxSteelStress'
argument= 'getMaxSteelStress'


displaySettings= vtk_FE_graphic.DisplaySettingsFE()

setDisp= shellElements
oh= output_handler.OutputHandler(modelSpace)
oh.outputStyle.cameraParameters= cameraParameters
oh.displayFieldDirs1and2(limitStateLabel,argument,setToDisplay=setDisp,component=None, fileName= None)

