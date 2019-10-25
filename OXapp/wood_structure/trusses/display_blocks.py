# -*- coding: utf-8 -*-
import sys
arg1= str(sys.argv[1])
execfile(arg1)

from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.CAD_model import vtk_CAD_graphic

defDisplay= vtk_CAD_graphic.RecordDefDisplayCAD()
defDisplay.cameraParameters= vtk_graphic_base.CameraParameters('Custom')
defDisplay.cameraParameters.viewUpVc= [0,0,1]
defDisplay.cameraParameters.posCVc= [0,-100,0]
setToDisplay= xcTotalSet
defDisplay.displayBlocks(setToDisplay,caption= setToDisplay.name+' set')
