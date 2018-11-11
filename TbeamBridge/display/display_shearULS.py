# -*- coding: utf-8 -*-
from postprocess.control_vars import *
from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import vtk_FE_graphic
from postprocess.xcVtk.FE_model import Fields

model_path="../"
#Project directory structure
execfile(model_path+'project_directories.py')

modelDataInputFile=model_path+"model_data.py" #data for FE model generation
execfile(modelDataInputFile)


#Load properties to display:
preprocessor= model.getPreprocessor()
fName= model_path+check_results_directory+'verifRsl_shearULS.py'
execfile(fName)


#xcSet= deckSet
#xcSet= foundationSet
#xcSet= wallsSet

limitStateLabel= lsd.shearResistance.label
#attributeName= limitStateLabel + 'Sect1'   #Shear limit state direction 1.
#attributeName= limitStateLabel + 'Sect2'   #Shear limit state direction 2


#Possible arguments: 'CF', 'N', 'My', 'Mz', 'Mu', 'Vy', 'Vz', 'theta', 'Vcu', 'Vsu', 'Vu'
argument= 'CF'


# #Flatten values.
# if( "FCCP" in attributeName):
#   extrapolate_elem_attr.flatten_attribute(elemSet,attributeName,1,2)


defDisplay= vtk_FE_graphic.RecordDefDisplayEF()
xcSet= deckSet
attributeName= limitStateLabel + 'Sect1'
field= Fields.getScalarFieldFromControlVar(attributeName,argument,xcSet,None,1.0)
field.plot(defDisplay,caption= 'Shear check '+ attributeName + '  '+xcSet.name+ '  '+argument)
attributeName= limitStateLabel + 'Sect2'
field= Fields.getScalarFieldFromControlVar(attributeName,argument,xcSet,None,1.0)
field.plot(defDisplay,caption= 'Shear check '+ attributeName + ' '+xcSet.name+ '  '+argument)
xcSet= foundationSet
attributeName= limitStateLabel + 'Sect1'
field= Fields.getScalarFieldFromControlVar(attributeName,argument,xcSet,None,1.0)
field.plot(defDisplay,caption= 'Shear check '+ attributeName + ' '+xcSet.name+ '  '+argument)
attributeName= limitStateLabel + 'Sect2'
field= Fields.getScalarFieldFromControlVar(attributeName,argument,xcSet,None,1.0)
field.plot(defDisplay,caption= 'Shear check '+ attributeName + ' '+xcSet.name+ '  '+argument)
xcSet= wallsSet
attributeName= limitStateLabel + 'Sect1'
field= Fields.getScalarFieldFromControlVar(attributeName,argument,xcSet,None,1.0)
field.plot(defDisplay,caption= 'Shear check '+ attributeName + ' '+xcSet.name+ '  '+argument)
attributeName= limitStateLabel + 'Sect2'
field= Fields.getScalarFieldFromControlVar(attributeName,argument,xcSet,None,1.0)
field.plot(defDisplay,caption= 'Shear check '+ attributeName + ' '+xcSet.name+ '  '+argument)

