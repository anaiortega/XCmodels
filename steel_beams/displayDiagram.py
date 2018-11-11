# -*- coding: utf-8 -*-

execfile('calc_combs.py')
import datetime
import vtk
from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import vtk_FE_graphic
from postprocess.xcVtk import vtk_internal_force_diagram as ifd

defGrid= vtk_graphic_base.RecordDefGrid()
defGrid.nmbSet= "total"

#diagram= ifd.InternalForceDiagram(scale=0.02,fUnitConv=1e-3,sets=[setMainBeam],component="Mz")
#diagram= ifd.InternalForceDiagram(scale= 10,fUnitConv=1e-3,sets=[setMainBeam],component= "My")
diagram= ifd.InternalForceDiagram(-0.02,fUnitConv=1e-3,sets=[setMainBeam],component= "Qy")
diagram.addDiagram()

defDisplay= vtk_FE_graphic.RecordDefDisplayEF()
#defDisplay.windowHeight= 300
defDisplay.viewName= "YPos" #Point of view.
defDisplay.setupGrid(preprocessor.getSets.getSet('total'))
defDisplay.defineMeshScene(None)
defDisplay.appendDiagram(diagram) #Append diagram to the scene.

# execfile('draw_supports.py')
# defDisplay.renderer.AddActor(supportsActor)

defDisplay.displayScene('Main warehouse beams: '+diagram.component + ' [kN m]')
