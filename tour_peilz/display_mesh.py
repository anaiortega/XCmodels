# -*- coding: utf-8 -*-

execfile('xc_model_data.py')
execfile('captionTexts.py')
from postprocess.xcVtk.FE_model import vtk_FE_graphic
import vtk


defDisplay= vtk_FE_graphic.RecordDefDisplayEF()
setToDisp= xcTotalSet #impactOnBody #totalSet

defDisplay.FEmeshGraphic(xcSet= setToDisp,caption='',viewNm="-X+Y+Z",defFScale=1.0)

