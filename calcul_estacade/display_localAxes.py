# -*- coding: utf-8 -*-

execfile('./model_data.py')
execfile('./captionTexts.py')

from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import vtk_FE_graphic
from postprocess.xcVtk.fields import local_axes_vector_field as lavf
import vtk

lcs= qg.LoadCaseResults(gilamontDock)

lcs.displayLocalAxes(setToDisplay=setParapet,caption= setParapet.genDescr.capitalize() + ', '+ capTexts['LocalAxes'],fileName=None)


