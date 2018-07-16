# -*- coding: utf-8 -*-

execfile('../model_data.py')
execfile('../captionTexts.py')
from postprocess.xcVtk.FE_model import vtk_FE_graphic

#  partToDisplay: XC set of elements to be displayed
#  caption:  text to write in the graphic
#  viewNm:   name of the view to use
#            predefined view names: 'XYZPos','XYZNeg','XNeg','XPos','YNeg','YPos',
#            'ZNeg','ZPos'  (defaults to 'XYZPos')
#  defFScale: factor to apply to current displacement of nodes so that the
#             display position of each node equals to the initial position plus
#             its displacement multiplied by this factor. (Defaults to 0.0,
#             i.e. display of initial/undeformed shape)

defDisplay= vtk_FE_graphic.RecordDefDisplayEF()
#setToDisp=shells
setToDisp=overallSet
#setToDisp=shellsPcable
#setToDisp=rest_Acc

defDisplay.FEmeshGraphic(xcSets=[setToDisp],caption='',viewNm='XPos',defFScale=1.0)

