# -*- coding: utf-8 -*-

execfile('../model_data.py')
execfile('../loadStateData.py')

from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import quick_graphics as qg

#ordered list of load cases (from those defined in ../loadStateData.py
#or redefined lately) to be displayed:
loadCasesToDisplay=[G1,G2,G3,Q1ayb,Q1a,Q1b,Q2ayb,Q2a,Q2b]

#End data

for lc in loadCasesToDisplay:
    lcs= qg.LoadCaseResults(FEcase, loadCaseName=lc.loadCaseName, loadCaseExpr= lc.loadCaseExpr)
    lcs.solve()
    for st in lc.setsToDispLoads:
        capt=lc.loadCaseDescr + ', ' + st.description + ', '  + lc.unitsLoads
        lcs.displayLoadVectors(setToDisplay=overallSet,loadCaseNm=lc.loadCaseName,caption= capt,fileName=None,defFScale=1.0)



