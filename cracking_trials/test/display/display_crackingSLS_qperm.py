# -*- coding: utf-8 -*-

from postprocess.control_vars import *
from postprocess import limit_state_data as lsd
from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import vtk_display_limit_state as dls


model_path="../"
#Project directory structure
execfile(model_path+'project_directories.py')

modelDataInputFile=model_path+"model_data.py" #data for FE model generation
execfile(modelDataInputFile)


#Load properties to display:
fName= model_path+check_results_directory+'verifRsl_crackingSLS_qperm.py'
execfile(fName)
execfile('../captionTexts.py')

limitStateLabel= lsd.quasiPermanentLoadsCrackControl.label

#Possible arguments: 'getMaxSteelStress', 'getCF'
argument= 'getMaxSteelStress'

setDisp= allShells
dls.displayFieldDirs1and2(limitStateLabel,argument,setDisp,None,1.0,None,capTexts,defFScale=1.0)
