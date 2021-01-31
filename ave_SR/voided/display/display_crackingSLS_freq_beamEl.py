# -*- coding: utf-8 -*-
from postprocess.control_vars import *
from postprocess import limit_state_data as lsd
from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import vtk_FE_graphic
from postprocess.xcVtk.diagrams import control_var_diagram as cvd

model_path="../"
#Project directory structure
exec(open(model_path+'env_config.py').read())

modelDataInputFile=model_path+"model_gen.py" #data for FE model generation
exec(open(modelDataInputFile).read())


#Load properties to display:
fName=  cfg.projectDirTree.getVerifCrackFreqFile()
exec(open(fName).read())


limitStateLabel= lsd.freqLoadsCrackControl.label

#Available arguments: 'N', 'My','Mz','s_rmax','eps_sm','wk'
argument= 'N'

setDispRes=beamX   #set of linear elements to which display results 
setDisp=beamX    #set of elements (any type) to be displayed

diagram= cvd.ControlVarDiagram(scaleFactor= 1,fUnitConv= 1e-3,sets=[setDispRes],attributeName= limitStateLabel,component= argument)
diagram.addDiagram()

displaySettings= vtk_FE_graphic.DisplaySettingsFE()
 #predefined view names: 'XYZPos','XNeg','XPos','YNeg','YPos',
 #                        'ZNeg','ZPos'  (defaults to 'XYZPos')
#displaySettings.cameraParameters= vtk_graphic_base.CameraParameters('YPos') #Point of view.
displaySettings.setupGrid(setDisp)
displaySettings.defineMeshScene(None,defFScale=0.0)
displaySettings.appendDiagram(diagram) #Append diagram to the scene.

caption= cfg.capTexts[limitStateLabel] + ', ' + cfg.capTexts[argument] + '. '+ setDispRes.description.capitalize() 
caption= cfg.capTexts[limitStateLabel] + ', ' + cfg.capTexts[argument] + '. '+ setDispRes.description.capitalize() + ', ' + 'Dir. 1'
displaySettings.displayScene(caption)



