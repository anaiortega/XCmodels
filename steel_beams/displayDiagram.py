# -*- coding: utf-8 -*-

exec(open('calc_combs.py').read()))
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

displaySettings= vtk_FE_graphic.DisplaySettingsFE()
#displaySettings.windowHeight= 300
displaySettings.cameraParameters= vtk_graphic_base.CameraParameters('YPos') #Point of view.
displaySettings.setupGrid(preprocessor.getSets.getSet('total'))
displaySettings.defineMeshScene(None)
displaySettings.appendDiagram(diagram) #Append diagram to the scene.

# exec(open('draw_supports.py').read()))
# displaySettings.renderer.AddActor(supportsActor)

displaySettings.displayScene('Main warehouse beams: '+diagram.component + ' [kN m]')
