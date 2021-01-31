# -*- coding: utf-8 -*-
from postprocess.control_vars import *
from postprocess import limit_state_data as lsd
from postprocess.xcVtk import vtk_graphic_base
from postprocess import output_handler


model_path="../"
#Project directory structure
exec(open(model_path+'env_config.py').read()))

modelDataInputFile=model_path+"model_data.py" #data for FE model generation
exec(open(modelDataInputFile).read()))


#Load properties to display:
fName=  cfg.projectDirTree.getVerifCrackFreqFile()
exec(open(fName).read()))
exec(open('../captionTexts.py').read()))


limitStateLabel= lsd.freqLoadsCrackControl.label
#Possible arguments: 'N', 'My','Mz','s_rmax','eps_sm','wk'
argument= 'wk'
argument= 'Mz'

setDisp= deck
oh= output_handler.OutputHandler(modelSpace)
oh.outputStyle.cameraParameters= cameraParameters
oh.displayFieldDirs1and2(limitStateLabel,argument,setDisp,component=None,fileName=None,defFScale=0.0)



