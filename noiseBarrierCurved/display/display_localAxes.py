# -*- coding: utf-8 -*-

exec(open('../model_data.py').read()))
exec(open('../captionTexts.py').read()))

from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import vtk_FE_graphic
import vtk

    # lcs.displayLocalAxes: vector field display of the element local axes.
    # Parameters:
    #   setToDisplay:   set of elements to be displayed
    #                   (defaults to 'total')
    #   vectorScale:    factor to apply to the vectors length in the 
    #                   representation (defaults to 1).
    #   viewDef:        camera parameters (position, orientation,...)
    #                   options: "XYZPos", "XPos", "XNeg","YPos", "YNeg",
    #                   "ZPos", "ZNeg") (defaults to "XYZPos")
    #   fileName:       full name of the graphic file to generate. Defaults to 
    #                   None, in this case it returns a console output graphic.

stDisp=colsSet  #set to display
lcs= qg.LoadCaseResults(FEcase)
lcs.displayLocalAxes(setToDisplay=stDisp.elSet,caption= stDisp.genDescr.capitalize() + ', '+ capTexts['LocalAxes'])



