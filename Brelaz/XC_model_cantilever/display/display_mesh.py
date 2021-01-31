# -*- coding: utf-8 -*-

exec(open('../model_data.py').read()))
exec(open('../captionTexts.py').read()))
from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import vtk_FE_graphic


displaySettings= vtk_FE_graphic.DisplaySettingsFE()
#setToDisp=shells
setToDisp=overallSet
#setToDisp=shellsPcable
#setToDisp=rest_Acc

displaySettings.FEmeshGraphic(xcSets=[setToDisp],caption='',cameraParameters= vtk_graphic_base.CameraParameters('XPos'),defFScale=1.0)

