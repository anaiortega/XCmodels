# -*- coding: utf-8 -*-
from postprocess.control_vars import *
from postprocess import limit_state_data as lsd
from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import vtk_FE_graphic
from postprocess.xcVtk.diagrams import control_var_diagram as cvd

modelDataInputFile="../model_data.py" #data for FE model generation
exec(open(modelDataInputFile).read())
exec(open('./directs.py').read())
exec(open('./setCalcDisp.py').read())


#Load properties to display:
fName= dir_checks +'verifRsl_shearULS.py'
exec(open(fName).read())
exec(open('../../PSs/captionTexts.py').read())


limitStateLabel= lsd.shearResistance.label


#Available arguments: 'CF', 'N', 'My', 'Mz', 'Mu', 'Vy', 'Vz', 'theta', 'Vcu', 'Vsu', 'CF'
argument= 'CF'

setDispRes=setDisp   #set of linear elements to which display results 

#setDisp=overallSet    #set of elements (any type) to be displayed
setDisp=setDisp

diagram= cvd.ControlVarDiagram(scaleFactor= 5,fUnitConv= 1,sets=[setDispRes],attributeName= limitStateLabel,component= argument)
diagram.addDiagram()


displaySettings= vtk_FE_graphic.DisplaySettingsFE()
 #predefined view names: 'XYZPos','XNeg','XPos','YNeg','YPos',
 #                        'ZNeg','ZPos'  (defaults to 'XYZPos')
displaySettings.cameraParameters= vtk_graphic_base.CameraParameters('YPos') #Point of view.
displaySettings.setupGrid(setDisp)
displaySettings.defineMeshScene(None,defFScale=0.0)
displaySettings.appendDiagram(diagram) #Append diagram to the scene.

caption= cfg.capTexts[limitStateLabel] + ', ' + cfg.capTexts[argument] + '. '+ setDispRes.description.capitalize() + ', ' + 'Dir. 1'
displaySettings.displayScene(caption)



