# -*- coding: utf-8 -*-
from postprocess.control_vars import *
from postprocess import limit_state_data as lsd
from postprocess.xcVtk.FE_model import vtk_FE_graphic
from postprocess.xcVtk import control_var_diagram as cvd

execfile("../model_gen.py") #FE model generation


setDispRes=beamX   #set of linear elements to which display results 
setDisp=beamX    #set of elements (any type) to be displayed

#Available arguments: 'N', 'My','Mz','s_rmax','eps_sm','wk'
argument= 'N'


#Load properties to display:
execfile(cfg.verifCrackFreqFile)

limitStateLabel= lsd.freqLoadsCrackControl.label

diagram= cvd.ControlVarDiagram(scaleFactor= 1,fUnitConv= 1e-3,sets=[setDispRes],attributeName= limitStateLabel,component= argument)
diagram.addDiagram()

defDisplay= vtk_FE_graphic.RecordDefDisplayEF()
 #predefined view names: 'XYZPos','XNeg','XPos','YNeg','YPos',
 #                        'ZNeg','ZPos'  (defaults to 'XYZPos')
#defDisplay.viewName= "YPos" #Point of view.
defDisplay.setupGrid(setDisp)
defDisplay.defineMeshScene(None,defFScale=0.0)
defDisplay.appendDiagram(diagram) #Append diagram to the scene.

caption= cfg.capTexts[limitStateLabel] + ', ' + cfg.capTexts[argument] + '. '+ setDispRes.description.capitalize() 
caption= cfg.capTexts[limitStateLabel] + ', ' + cfg.capTexts[argument] + '. '+ setDispRes.description.capitalize() + ', ' + 'Dir. 1'
defDisplay.displayScene(caption)



