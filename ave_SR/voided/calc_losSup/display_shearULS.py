# -*- coding: utf-8 -*-
from postprocess.control_vars import *
from postprocess import limit_state_data as lsd
from postprocess.xcVtk import vtk_graphic_base
from postprocess import output_handler


#Project directory structure
execfile('./directs.py')

modelDataInputFile="../model_data.py" #data for FE model generation
execfile(modelDataInputFile)

#Load properties to display:
fName= dir_checks+'verifRsl_shearULS.py'
execfile(fName)
execfile('../../generic_bridges/voided_slab_bridge/captionTexts.py')
execfile("./setCalcDisp.py")


limitStateLabel= lsd.shearResistance.label
#attributeName= limitStateLabel + 'Sect1'   #Shear limit state direction 1.
#attributeName= limitStateLabel + 'Sect2'   #Shear limit state direction 2


#Possible arguments: 'CF', 'N', 'My', 'Mz', 'Mu', 'Vy', 'Vz', 'theta', 'Vcu', 'Vsu', 'Vu'
argument= 'CF'


# #Flatten values.
# if( "FCCP" in attributeName):
#   extrapolate_elem_attr.flatten_attribute(elemSet,attributeName,1,2)


#setDisp= allShells
setDisp=losSupV2
oh= output_handler.OutputHandler(modelSpace)
oh.outputStyle.cameraParameters= cameraParameters
oh.displayFieldDirs1and2(limitStateLabel,argument,setToDisplay=setDisp,component=None, fileName= None,defFScale=0.0)



