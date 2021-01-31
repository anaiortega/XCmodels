# -*- coding: utf-8 -*-

exec(open('../model_data.py').read()))
exec(open('../captionTexts.py').read()))

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

setsToDisplay=[deck,walls,foundation]
vScale=0.3     #scale to apply to vector representation
for st in setsToDisplay:
    lcs= qg.LoadCaseResults(FEcase)
lcs.displayLocalAxes(setToDisplay=st,caption=st.description.capitalize() + ', '+  capTexts['LocalAxes'],fileName=None,defFScale=0.0)



