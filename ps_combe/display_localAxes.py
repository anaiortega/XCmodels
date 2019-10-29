# -*- coding: utf-8 -*-

execfile('./model_data.py')
execfile('./captionTexts.py')

from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import quick_graphics as qg

    # lcs.displayLocalAxes: vector field display of the element local axes.
    # Parameters:
    #   setToDisplay:   set of elements to be displayed
    #                   (defaults to 'total')
    #   vectorScale:    factor to apply to the vectors length in the 
    #                   representation (defaults to 1).
    #    viewDef:        camera parameters (position, orientation,...)
    #                   options: "XYZPos","XYZNeg", "XPos", "XNeg","YPos","YNeg"
    #                   "ZPos", "ZNeg") (defaults to "XYZPos")

    #   fileName:       full name of the graphic file to generate. Defaults to 
    #                   None, in this case it returns a console output graphic.

#setToDisp= webElements
#setToDisp= abutmentBearingElements+beamLinesType4+beamLinesType5+beamLinesType6
setToDisp= pierBearingElements
#setToDisp= xcTotalSet
#setToDisp= beamLinesType4+beamLinesType5+beamLinesType6
lcs= qg.LoadCaseResults(model)
lcs.displayLocalAxes(setToDisplay=setToDisp,caption=capTexts['LocalAxes'],fileName=None,defFScale=0.0)


