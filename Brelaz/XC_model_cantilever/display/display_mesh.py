# -*- coding: utf-8 -*-

execfile('../model_data.py')
execfile('../captionTexts.py')
from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import vtk_FE_graphic


defDisplay= vtk_FE_graphic.RecordDefDisplayEF()
#setToDisp=shells
setToDisp=overallSet
#setToDisp=shellsPcable
#setToDisp=rest_Acc

defDisplay.FEmeshGraphic(xcSets=[setToDisp],caption='',cameraParameters= vtk_graphic_base.CameraParameters('XPos'),defFScale=1.0)

