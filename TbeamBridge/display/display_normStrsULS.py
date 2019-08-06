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
fName= model_path+check_results_directory+'verifRsl_normStrsULS.py'
execfile(fName)




limitStateLabel= lsd.normalStressesResistance.label

#Possible arguments: 'CF', 'N', 'My', 'Mz'
argument= 'CF'


# if("FCCP" in attributeName):
#   extrapolate_elem_attr.flatten_attribute(xcSet.elements,attributeName,1,2)
defDisplay= vtk_FE_graphic.RecordDefDisplayEF()
xcSet= deckSet
attributeName= limitStateLabel + 'Sect1'   #Normal stresses limit state direction 1.
field= Fields.getScalarFieldFromControlVar(attributeName,argument,xcSet,None,1.0)
field.plot(defDisplay,caption= 'Normal stresses check '+ attributeName +'   ' + argument+ '   '+xcSet.name )
attributeName= limitStateLabel + 'Sect2'   #Normal stresses limit state direction 2
field= Fields.getScalarFieldFromControlVar(attributeName,argument,xcSet,None,1.0)
field.plot(defDisplay,caption= 'Normal stresses check '+ attributeName +'   ' + argument+ '   '+xcSet.name )
xcSet= foundationSet
attributeName= limitStateLabel + 'Sect1'   #Normal stresses limit state direction 1.
field= Fields.getScalarFieldFromControlVar(attributeName,argument,xcSet,None,1.0)
field.plot(defDisplay,caption= 'Normal stresses check '+ attributeName +'   ' + argument+ '   '+xcSet.name )
attributeName= limitStateLabel + 'Sect2'   #Normal stresses limit state direction 2
field= Fields.getScalarFieldFromControlVar(attributeName,argument,xcSet,None,1.0)
field.plot(defDisplay,caption= 'Normal stresses check '+ attributeName +'   ' + argument+ '   '+xcSet.name )
xcSet= wallsSet
attributeName= limitStateLabel + 'Sect1'   #Normal stresses limit state direction 1.
field= Fields.getScalarFieldFromControlVar(attributeName,argument,xcSet,None,1.0)
field.plot(defDisplay,caption= 'Normal stresses check '+ attributeName +'   ' + argument+ '   '+xcSet.name )
attributeName= limitStateLabel + 'Sect2'   #Normal stresses limit state direction 2
field= Fields.getScalarFieldFromControlVar(attributeName,argument,xcSet,None,1.0)
field.plot(defDisplay,caption= 'Normal stresses check '+ attributeName +'   ' + argument+ '   '+xcSet.name )


