# -*- coding: utf-8 -*-

execfile('../model_data.py')

from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import vtk_FE_graphic


defDisplay= vtk_FE_graphic.DisplaySettingsFE()
setToDisp=overallSet
defDisplay.FEmeshGraphic(xcSet=setToDisp,caption='',cameraParameters= vtk_graphic_base.CameraParameters('XYZPos'),defFScale=1.0)

