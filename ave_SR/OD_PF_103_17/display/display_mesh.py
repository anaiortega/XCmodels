# -*- coding: utf-8 -*-

execfile('../model_data.py')

from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import vtk_FE_graphic


displaySettings= vtk_FE_graphic.DisplaySettingsFE()
setToDisp=overallSet
displaySettings.FEmeshGraphic(xcSet=setToDisp,caption='',cameraParameters= vtk_graphic_base.CameraParameters('XYZPos'),defFScale=1.0)

