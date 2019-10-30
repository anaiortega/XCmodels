# -*- coding: utf-8 -*-
import os
from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import quick_graphics as QGrph

execfile('../model_data.py')
execfile('../loadStateData.py')

#ordered list of load cases (from those defined in ../loadStateData.py
#or redefined lately) to be displayed:
loadCasesToDisplay=[Q1]
Q1.listDspRot=['uZ']

#End data

for lc in loadCasesToDisplay:
    lcs=QGrph.LoadCaseResults(FEcase)
    #solve for load case
    lcs.solve(loadCaseName=lc.loadCaseName,loadCaseExpr=lc.loadCaseExpr)
    #Displacements and rotations displays
    for st in lc.setsToDispDspRot:
        for arg in lc.listDspRot:
            lcs.displayDispRot(itemToDisp=arg,setToDisplay=st,fileName='figures/uz_Q1.jpg',defFScale=1)
