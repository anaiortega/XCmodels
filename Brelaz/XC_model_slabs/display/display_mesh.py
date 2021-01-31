# -*- coding: utf-8 -*-

exec(open('../model_data.py').read())
exec(open('../captionTexts.py').read())
from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import vtk_FE_graphic

#  partToDisplay: XC set of elements to be displayed
#  caption:  text to write in the graphic
#  cameraParameters: camera parameters (position, orientation,...)
#            predefined view names: 'XYZPos','XYZNeg','XNeg','XPos','YNeg',
#            'YPos','ZNeg','ZPos'  (defaults to 'XYZPos')
#  defFScale: factor to apply to current displacement of nodes so that the
#             display position of each node equals to the initial position plus
#             its displacement multiplied by this factor. (Defaults to 0.0,
#             i.e. display of initial/undeformed shape)

displaySettings= vtk_FE_graphic.DisplaySettingsFE()
#setToDisp=shells
setToDisp=overallSet
#setToDisp=shellsPcable
#setToDisp=rest_Acc

displaySettings.FEmeshGraphic(xcSets=[setToDisp],caption='',cameraParameters= vtk_graphic_base.CameraParameters('XPos'),defFScale=1.0)

