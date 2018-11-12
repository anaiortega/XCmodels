# -*- coding: utf-8 -*-

execfile('../model_data2.py')
from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import vtk_FE_graphic
import vtk

    # displayLocalAxes: vector field display of the element local axes.
    # Parameters:
    #   setToDisplay:   set of elements to be displayed
    #                   (defaults to 'total')
    #   vectorScale:    factor to apply to the vectors length in the 
    #                   representation (defaults to 1).
    #   viewNm:         name of the view  that contains the renderer (possible
    #                   options: "XYZPos", "XPos", "XNeg","YPos", "YNeg",
    #                   "ZPos", "ZNeg") (defaults to "XYZPos")
    #   fileName:       full name of the graphic file to generate. Defaults to 
    #                   None, in this case it returns a console output graphic.
 
model.displayLocalAxes(setToDisplay=deckSet,vectorScale=0.3,viewNm="XYZPos",caption= 'Deck slab, local axes')
model.displayLocalAxes(setToDisplay=beamSet,vectorScale=0.3,viewNm="XYZPos",caption= 'Beams, local axes')


