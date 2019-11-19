# -*- coding: utf-8 -*-
from postprocess.control_vars import *
from postprocess import limit_state_data as lsd
from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import vtk_FE_graphic
from postprocess.xcVtk.diagrams import control_var_diagram as cvd


modelDataInputFile="../model_data.py" #data for FE model generation
execfile(modelDataInputFile)
execfile('./directs.py')
execfile('./setCalcDisp.py')


#Load properties to display:
fName= dir_checks + 'verifRsl_normStrsULS.py'
execfile(fName)
execfile('../../generic_bridges/voided_slab_bridge/captionTexts.py')

limitStateLabel= lsd.normalStressesResistance.label

#Possible arguments: 'CF', 'N', 'My', 'Mz'
argument= 'CF'

setDispRes=setDisp   #set of linear elements to which display results 
setDisp=setDisp   #set of elements (any type) to be displayed


diagram= cvd.ControlVarDiagram(scaleFactor= 10,fUnitConv= 1,sets=[setDisp],attributeName= limitStateLabel,component= argument)
diagram.addDiagram()


defDisplay= vtk_FE_graphic.RecordDefDisplayEF()
 #predefined view names: 'XYZPos','XNeg','XPos','YNeg','YPos',
 #                        'ZNeg','ZPos'  (defaults to 'XYZPos')
#defDisplay.cameraParameters= vtk_graphic_base.CameraParameters('YPos') #Point of view.
defDisplay.setupGrid(setDisp)
defDisplay.defineMeshScene(None,defFScale=0.0)
defDisplay.appendDiagram(diagram) #Append diagram to the scene.

caption= cfg.capTexts[limitStateLabel] + ', ' + cfg.capTexts[argument] + '. '+ setDispRes.description.capitalize() + ', ' + 'Dir. 1'
defDisplay.displayScene(caption)



