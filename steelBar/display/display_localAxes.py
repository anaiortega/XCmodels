# -*- coding: utf-8 -*-

exec(open("../model_gen.py").read()) #FE model generation

from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import quick_graphics as qg

    # lcs.displayLocalAxes: vector field display of the element local axes.
    # Parameters:
    #   setToDisplay:   set of elements to be displayed
    #                   (defaults to 'total')
    #   vectorScale:    factor to apply to the vectors length in the 
    #                   representation (defaults to 1).
    #   viewNm:         name of the view  that contains the renderer (possible
    #                   options: "XYZPos","XYZNeg", "XPos", "XNeg","YPos","YNeg"
    #                   "ZPos", "ZNeg") (defaults to "XYZPos")
    #   hCamFct:   factor that applies to the height of the camera position 
    #              in order to change perspective of isometric views 
    #              (defaults to 1, usual values 0.1 to 10)
    #   fileName:       full name of the graphic file to generate. Defaults to 
    #                   None, in this case it returns a console output graphic.

setToDisp=beamY
lcs= qg.LoadCaseResults(FEcase)
lcs.displayLocalAxes(setToDisplay=setToDisp,caption= cfg.capTexts['LocalAxes'],fileName=None,defFScale=0.0)




