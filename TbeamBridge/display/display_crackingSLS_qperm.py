# -*- coding: utf-8 -*-

from postprocess.control_vars import *
from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import vtk_FE_graphic
from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import Fields


model_path="../"
#Project directory structure
execfile(model_path+'project_directories.py')

modelDataInputFile=model_path+"model_data.py" #data for FE model generation
execfile(modelDataInputFile)


#Load properties to display:
preprocessor= model.getPreprocessor()
fName= model_path+check_results_directory+'verifRsl_crackingSLS_qperm.py'
execfile(fName)

#xcSet= deckSet
#xcSet= foundationSet
xcSet= wallsSet

limitStateLabel= lsd.quasiPermanentLoadsCrackControl.label
attributeName= limitStateLabel + 'Sect1'   #Crack control limit state direction 1.
#attributeName= limitStateLabel + 'Sect2'   #Crack control limit state direction 2

argument= 'getMaxSteelStress'
#argument= 'crackControlVarsNeg.steelStress'


field= Fields.getScalarFieldFromControlVar(attributeName,argument,xcSet,None,1.0)

defDisplay= vtk_FE_graphic.RecordDefDisplayEF()
field.plot(defDisplay,caption= 'Crack control '+ attributeName + ' '+argument+' [MPa]')
