# -*- coding: utf-8 -*-
from postprocess.control_vars import *
from postprocess import limit_state_data as lsd
from postprocess.xcVtk.FE_model import vtk_display_limit_state as dls


#FE model generation
execfile("../model_gen.py")

#Load properties to display:
execfile(cfg.verifNormStrFile)

limitStateLabel= lsd.normalStressesResistance.label

#Possible arguments: 'CF', 'N', 'My','Mz'
argument= 'CF'

# if("FCCP" in attributeName):
#   extrapolate_elem_attr.flatten_attribute(xcSet.getElements,attributeName,1,2)

#Set of shell elements to display
setDisp= found
dls.displayFieldDirs1and2(limitStateLabel,argument,setDisp,None,1.0,None,cfg.capTexts,defFScale=0.0,rgMinMax=(0,1))




