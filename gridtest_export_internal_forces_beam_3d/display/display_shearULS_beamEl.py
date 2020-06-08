# -*- coding: utf-8 -*-
from postprocess.control_vars import *
from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import vtk_FE_graphic
from postprocess.xcVtk.diagrams import control_var_diagram as cvd

model_path="../"
#Project directory structure
execfile(model_path+'env_config.py')

modelDataInputFile=model_path+"model_data.py" #data for FE model generation
execfile(modelDataInputFile)


#Load properties to display:
preprocessor= model.getPreprocessor()
fName=  cfg.projectDirTree.getVerifShearFile()
execfile(fName)
execfile('../captionTexts.py')


limitStateLabel= lsd.shearResistance.label


#Possible arguments: 'CF', 'N', 'My', 'Mz', 'Mu', 'Vy', 'Vz', 'theta', 'Vcu', 'Vsu', 'Vu'
argument= 'CF'
setDisp=colsSet
#setDisp=botColSet

diagram= cvd.ControlVarDiagram(scaleFactor= 10,fUnitConv= 1,sets=[setDisp.elSet],attributeName= limitStateLabel,component= argument)
diagram.addDiagram()


displaySettings= vtk_FE_graphic.DisplaySettingsFE()
displaySettings.cameraParameters= vtk_graphic_base.CameraParameters('YPos') #Point of view.
displaySettings.setupGrid(preprocessor.getSets.getSet('total'))
displaySettings.defineMeshScene(None)
displaySettings.appendDiagram(diagram) #Append diagram to the scene.

#execfile('draw_supports.py')
#displaySettings.renderer.AddActor(supportsActor)

caption= capTexts[limitStateLabel] + ', ' + capTexts[argument] + '. '+ setDisp.genDescr.capitalize() + ', ' + setDisp.sectDescr[1]
displaySettings.displayScene(caption)



