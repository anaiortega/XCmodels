# -*- coding: utf-8 -*-
from postprocess.control_vars import *
from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import vtk_FE_graphic
from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import Fields


model_path="../"
#Project directory structure
exec(open(model_path+'env_config.py').read())

modelDataInputFile=model_path+"model_data.py" #data for FE model generation
exec(open(modelDataInputFile).read())


#Load properties to display:
preprocessor= model.getPreprocessor()
fName=  cfg.projectDirTree.getVerifCrackFreqFile()
exec(open(fName).read())


limitStateLabel= lsd.freqLoadsCrackControl.label
#attributeName= limitStateLabel + 'Sect1'   #Crack control limit state direction 1.
attributeName= limitStateLabel + 'Sect2'   #Crack control limit state direction 2.
argument= 'getMaxSteelStress'
#argument= 'crackControlVarsNeg.steelStress'

xcSet=wallsSet

field= Fields.getScalarFieldFromControlVar(attributeName,argument,xcSet,None,1.0)

displaySettings= vtk_FE_graphic.DisplaySettingsFE()
field.plot(displaySettings,caption= 'Crack control '+ attributeName + ' '+argument+' [MPa]')
