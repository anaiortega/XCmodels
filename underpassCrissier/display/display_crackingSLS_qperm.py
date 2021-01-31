# -*- coding: utf-8 -*-

from postprocess.control_vars import *


model_path="../"
#Project directory structure
exec(open(model_path+'env_config.py').read())

modelDataInputFile=model_path+"model_data.py" #data for FE model generation
exec(open(modelDataInputFile).read())


#Load properties to display:
preprocessor= model.getPreprocessor()
fName=  cfg.projectDirTree.getVerifCrackQpermFile()
exec(open(fName).read())
exec(open('../captionTexts.py').read())

limitStateLabel= lsd.quasiPermanentLoadsCrackControl.label

argument= 'getMaxSteelStress'
#argument= 'getMaxN'
#argument= 'crackControlVarsNeg.steelStress'

setDisp= deckSet
#setDisp= leftWallSet
#setDisp= rightWallSet
#setDisp= foundationSet 

oh= output_handler.OutputHandler(modelSpace)
oh.outputStyle.cameraParameters= cameraParameters
oh.displayFieldDirs1and2(limitStateLabel,argument,setToDisplay=setDisp,component=None, fileName= None)
