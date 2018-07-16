# -*- coding: utf-8 -*-
from postprocess.control_vars import *
from postprocess import limit_state_data as lsd
from postprocess.xcVtk.FE_model import vtk_display_limit_state as dls


model_path="../"
#Project directory structure
execfile(model_path+'project_directories.py')

modelDataInputFile=model_path+"model_data.py" #data for FE model generation
execfile(modelDataInputFile)
preprocessor=prep

#Load properties to display:
fName= model_path+check_results_directory+'verifRsl_crackingSLS_freq.py'
execfile(fName)



limitStateLabel= lsd.freqLoadsCrackControl.label
#Possible arguments: 'getMaxSteelStress', 'getCF'
argument= 'getMaxSteelStress'
argument= 'getCF'
setDisp= losCim_M1
dls.displayFieldDirs1and2(limitStateLabel,argument,setDisp,None,1.0,None,cfg.capTexts,defFScale=0.0)



