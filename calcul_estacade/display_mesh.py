# -*- coding: utf-8 -*-

execfile('model_data.py')
from postprocess.xcVtk import vtk_grafico_base
from postprocess.xcVtk.FE_model import vtk_FE_graphic
from postprocess.xcVtk import linear_load_diagram as lld
import vtk

setToDisplay= xcTotalSet
defDisplay= vtk_FE_graphic.RecordDefDisplayEF()
defDisplay.viewName= "XYZPos" #Point of view.
defDisplay.setupGrid(setToDisplay)
defDisplay.defineMeshScene(None)

defDisplay.displayScene(caption= setToDisplay.name+' set')
