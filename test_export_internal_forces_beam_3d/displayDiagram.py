# -*- coding: utf-8 -*-


import datetime
import vtk
from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import vtk_FE_graphic
from postprocess.xcVtk.diagrams import control_var_diagram as cvd
import os
from postprocess.control_vars import *

model_path="./"
#Project directory structure

modelDataInputFile=model_path+"test_export_internal_forces_beam_2d.py" #data for FE model generation
execfile(modelDataInputFile)


#Load properties to display:

fName= cfg.projectDirTree.getVerifShearFile()
execfile(fName)
#execfile(model_path+'/captionTexts.py')

defGrid= vtk_graphic_base.RecordDefGrid()
defGrid.nmbSet= "total"

#diagram= cvd.ControlVarDiagram(scaleFactor= 1,fUnitConv= 1,sets=[totalSet],attributeName= lsd.normalStressesResistance.label,component= 'N')
diagram= cvd.ControlVarDiagram(scaleFactor= 1,fUnitConv= 1,sets=[totalSet],attributeName= lsd.normalStressesResistance.label,component= 'Mz')
#diagram= cvd.ControlVarDiagram(scaleFactor= 1,fUnitConv= 1,sets=[totalSet],attributeName= lsd.normalStressesResistance.label,component= 'CF')
diagram= cvd.ControlVarDiagram(scaleFactor= 10,fUnitConv= 1,sets=[totalSet],attributeName= lsd.shearResistance.label,component= 'CF')
#diagram= npd.InternalForceDiagram(-0.02,fUnitConv=1e-3,sets=[colsSet.elSet],component= "Qy")
diagram.addDiagram()

displaySettings= vtk_FE_graphic.DisplaySettingsFE()
#displaySettings.windowHeight= 300
displaySettings.cameraParameters= vtk_graphic_base.CameraParameters('YPos') #Point of view.
displaySettings.setupGrid(totalSet)
displaySettings.defineMeshScene(None)
displaySettings.appendDiagram(diagram) #Append diagram to the scene.

#execfile('draw_supports.py')
#displaySettings.renderer.AddActor(supportsActor)

displaySettings.displayScene('Noise barrier: '+ 'N [kN]')
