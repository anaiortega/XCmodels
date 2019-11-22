# -*- coding: utf-8 -*-
import os
from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import quick_graphics as QGrph

execfile('xc_model_data.py')
execfile('loadStateData.py')

#ordered list of load cases (from those defined in loadStateData.py
#or redefined lately) to be displayed:
#loadCasesToDisplay= [G2]
loadCasesToDisplay= [lcDisplays['SLSQP_1']]

#End data

for lc in loadCasesToDisplay:
    lcs=QGrph.LoadCaseResults(FEcase,lc.loadCaseName,lc.loadCaseExpr)
    #solve for load case
    lcs.solve()
    #Displacements and rotations displays
    for st in lc.setsToDispDspRot:
        for arg in lc.listDspRot:
            lcs.displayDispRot(itemToDisp=arg,setToDisplay=st,fileName=None,defFScale=1)
    #Internal forces displays on sets of «shell» elements
    for st in lc.setsToDispIntForc:
        for arg in lc.listIntForc:
            lcs.displayIntForc(itemToDisp=arg,setToDisplay=st,fileName=None,defFScale=1)

            
