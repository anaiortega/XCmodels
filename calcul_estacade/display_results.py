# -*- coding: utf-8 -*-
import os

exec(open('model_data.py').read())
exec(open('loadStateData.py').read())
from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import quick_graphics as qg

#ordered list of load cases (from those defined in ./loadStateData.py
#or redefined lately) to be displayed:
loadCasesToDisplay=[Snow]

for lc in loadCasesToDisplay:
    lcs= qg.QuickGraphics(gilamontDock)
    #solve for load case
    lcs.solve(loadCaseName=lc.loadCaseName,loadCaseExpr=lc.loadCaseExpr)
    #Displacements and rotations displays
    for st in lc.setsToDispDspRot:
        for arg in lc.listDspRot:
            lcs.displayDispRot(itemToDisp=arg,setToDisplay=st)
    #Display internal forces
    for st in lc.setsToDispIntForc:
        for arg in lc.listIntForc:
            lcs.displayIntForc(itemToDisp=arg,setToDisplay=st)
