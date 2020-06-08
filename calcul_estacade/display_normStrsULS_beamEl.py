# -*- coding: utf-8 -*-
from postprocess.control_vars import *
from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import vtk_FE_graphic
from postprocess.xcVtk.diagrams import control_var_diagram as cvd
from postprocess import limit_state_data as lsd

model_path="./"
#Project directory structure
execfile(model_path+'env_config.py')

modelDataInputFile=model_path+"model_data.py" #data for FE model generation
execfile(modelDataInputFile)


#Load properties to display:
fName= cfg.projectDirTree.getVerifNormStrFile()
execfile(fName)
execfile(model_path+'/captionTexts.py')


limitStateLabel= lsd.normalStressesResistance.label


#Possible arguments: 'CF', 'N', 'My', 'Mz'
argument= 'CF'
setDispRes= setColumns #set of linear elements to which display results 

diagram= cvd.ControlVarDiagram(scaleFactor= 1,fUnitConv= 1,sets=[setDispRes],attributeName= limitStateLabel,component= argument)
diagram.addDiagram()


defDisplay= vtk_FE_graphic.DisplaySettingsFE()
#defDisplay.cameraParameters= vtk_graphic_base.CameraParameters('YPos') #Point of view.
defDisplay.setupGrid(setDispRes)
defDisplay.defineMeshScene(None)
defDisplay.appendDiagram(diagram) #Append diagram to the scene.

#execfile('draw_supports.py')
#defDisplay.renderer.AddActor(supportsActor)

caption= capTexts[limitStateLabel] + ', ' + capTexts[argument] + '. '+ setDispRes.genDescr.capitalize() + ', ' + setDispRes.sectDescr[0]
defDisplay.displayScene(caption)



