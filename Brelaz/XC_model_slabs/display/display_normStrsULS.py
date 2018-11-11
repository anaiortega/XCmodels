# -*- coding: utf-8 -*-
from postprocess.control_vars import *
from postprocess import limit_state_data as lsd
from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import vtk_display_limit_state as dls

model_path="../"

modelDataInputFile=model_path+"model_data.py" #data for FE model generation
execfile(modelDataInputFile)


#Load properties to display:
preprocessor= FEcase.getPreprocessor
execfile(projectDirs.getNormalStressesULSFileName())
execfile('../captionTexts.py')

limitStateLabel= lsd.normalStressesResistance.label

#Possible arguments: 'CF', 'N', 'My', 'Mz'
argument= 'CF'


# if("FCCP" in attributeName):
#   extrapolate_elem_attr.flatten_attribute(xcSet.getElements,attributeName,1,2)

#Set of shell elements to display
#setDisp= deckSet
#setDisp= deck
setDisp=deckCenter
#setDisp= curb
dls.displayFieldDirs1and2(limitStateLabel,argument,setDisp,None,1.0,None,capTexts,defFScale=0.0)




