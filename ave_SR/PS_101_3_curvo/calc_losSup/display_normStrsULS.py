# -*- coding: utf-8 -*-
from postprocess.control_vars import *
from postprocess import limit_state_data as lsd
from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import vtk_display_limit_state as dls


#Project directory structure
execfile('./directs.py')

modelDataInputFile="../model_data.py" #data for FE model generation
execfile(modelDataInputFile)
execfile("./setCalcDisp.py")


#Load properties to display:
fName= dir_checks+'verifRsl_normStrsULS.py'
execfile(fName)
execfile('../../PSs/captionTexts.py')

limitStateLabel= lsd.normalStressesResistance.label

#Possible arguments: 'CF', 'N', 'My', 'Mz'
argument= 'CF'


# if("FCCP" in attributeName):
#   extrapolate_elem_attr.flatten_attribute(xcSet.elements,attributeName,1,2)

#Set of shell elements to display


dls.displayFieldDirs1and2(limitStateLabel,argument,setDisp,None,1.0,None,cfg.capTexts,defFScale=0.0)




