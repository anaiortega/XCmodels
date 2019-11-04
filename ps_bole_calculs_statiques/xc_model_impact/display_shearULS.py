# -*- coding: utf-8 -*-
from postprocess.control_vars import *
from postprocess import limit_state_data as lsd
from postprocess.xcVtk import vtk_graphic_base
from postprocess import output_handler


modelDataInputFile= "model_data.py" #data for FE model generation
execfile(modelDataInputFile)


#Load properties to display:
preprocessor= FEcase.getPreprocessor
execfile('results/verifications/verifRsl_shearULS.py')
execfile('captionTexts.py')


limitStateLabel= lsd.shearResistance.label
#attributeName= limitStateLabel + 'Sect1'   #Shear limit state direction 1.
#attributeName= limitStateLabel + 'Sect2'   #Shear limit state direction 2


#Possible arguments: 'CF', 'N', 'My', 'Mz', 'Mu', 'Vy', 'Vz', 'theta', 'Vcu', 'Vsu', 'Vu'
argument= 'Vu'


# #Flatten values.
# if( "FCCP" in attributeName):
#   extrapolate_elem_attr.flatten_attribute(elemSet,attributeName,1,2)


setDisp= parapetHeadSet #parapetBodySet #parapetHeadSet
oh= output_handler.OutputHandler(modelSpace)
oh.outputStyle.cameraParameters= cameraParameters
oh.displayFieldDirs1and2(limitStateLabel,argument,setToDisplay=setDisp,component=None, fileName= None,viewDef= vtk_graphic_base.CameraParameters("-X+Y+Z"),defFScale=0.0)



