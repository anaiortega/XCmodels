# -*- coding: utf-8 -*-

execfile('../model_data.py')
execfile('../../PSs/captionTexts.py')

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
lcs= qg.LoadCaseResults(FEcase)
'''
lcs.displayLocalAxes(setToDisplay=riostrEstr1,caption= cfg.capTexts['LocalAxes'],fileName=None,defFScale=0.0)
lcs.displayLocalAxes(setToDisplay=pilas,caption= cfg.capTexts['LocalAxes'],fileName=None,defFScale=0.0)
'''
lcs.displayLocalAxes(setToDisplay=losInf,caption=cfg.capTexts['LocalAxes'],fileName=None,defFScale=0.0)
lcs.displayLocalAxes(setToDisplay=supTablero,caption=cfg.capTexts['LocalAxes'],fileName=None,defFScale=0.0)
lcs.displayLocalAxes(setToDisplay=murAlig,caption=cfg.capTexts['LocalAxes'],fileName=None,defFScale=0.0)
lcs.displayLocalAxes(setToDisplay=murExtAlig,caption=cfg.capTexts['LocalAxes'],fileName=None,defFScale=0.0)
lcs.displayLocalAxes(setToDisplay=riostrEstr1,caption=cfg.capTexts['LocalAxes'],fileName=None,defFScale=0.0)
lcs.displayLocalAxes(setToDisplay=riostrPil1,caption=cfg.capTexts['LocalAxes'],fileName=None,defFScale=0.0)


