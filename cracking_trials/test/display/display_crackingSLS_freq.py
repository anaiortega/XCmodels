# -*- coding: utf-8 -*-
from postprocess.control_vars import *
from postprocess import limit_state_data as lsd
from postprocess.xcVtk import vtk_graphic_base
from postprocess import output_handler


model_path="../"
#Project directory structure
execfile(model_path+'project_directories.py')

modelDataInputFile=model_path+"model_data.py" #data for FE model generation
execfile(modelDataInputFile)


#Load properties to display:
fName= model_path+check_results_directory+'verifRsl_crackingSLS_freq.py'
execfile(fName)
execfile('../captionTexts.py')


limitStateLabel= lsd.freqLoadsCrackControl.label
#Possible arguments: 'N', 'My','Mz','s_rmax','eps_sm','wk'
argument= 'wk'
argument= 'Mz'

setDisp= deck
oh= output_handler.OutputHandler(modelSpace)
oh.outputStyle.cameraParameters= cameraParameters
oh.displayFieldDirs1and2(limitStateLabel,argument,setDisp,component=None,fileName=None,defFScale=0.0)



