# -*- coding: utf-8 -*-

execfile('../model_data.py')

from postprocess.xcVtk.FE_model import vtk_FE_graphic


defDisplay= vtk_FE_graphic.RecordDefDisplayEF()
setToDisp=overallSet
defDisplay.FEmeshGraphic(xcSets=[setToDisp],caption='',viewNm='XYZPos',defFScale=1.0)

