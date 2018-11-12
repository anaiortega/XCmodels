# -*- coding: utf-8 -*-


import datetime
import vtk
from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import vtk_FE_graphic
from postprocess.xcVtk import control_var_diagram as cvd
import os
from postprocess.control_vars import *

model_path="./"
#Project directory structure

modelDataInputFile=model_path+"test_export_internal_forces_beam_2d.py" #data for FE model generation
execfile(modelDataInputFile)


#Load properties to display:
#fName= model_path+'verifRsl_normStrsULS.py'
fName= model_path+'verifRsl_shearULS.py'
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

defDisplay= vtk_FE_graphic.RecordDefDisplayEF()
#defDisplay.windowHeight= 300
defDisplay.cameraParameters= vtk_graphic_base.CameraParameters('YPos') #Point of view.
defDisplay.setupGrid(totalSet)
defDisplay.defineMeshScene(None)
defDisplay.appendDiagram(diagram) #Append diagram to the scene.

#execfile('draw_supports.py')
#defDisplay.renderer.AddActor(supportsActor)

defDisplay.displayScene('Noise barrier: '+ 'N [kN]')
