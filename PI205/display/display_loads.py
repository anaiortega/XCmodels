# -*- coding: utf-8 -*-

exec(open('../model_data.py').read())
exec(open('../loadStateData.py').read())

from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import quick_graphics as qg

#ordered list of load cases (from those defined in ../loadStateData.py
#or redefined lately) to be displayed:
loadCasesToDisplay=[G1,G2,G3,Q1ayb,Q1a,Q1aEss,Q1b,Q1bEss,Q2ayb,Q2a,Q2aEss,Q2b,Q2bEss,Q3]

#End data

for lc in loadCasesToDisplay:
    lcs= qg.LoadCaseResults(FEcase, loadCaseName=lc.loadCaseName, loadCaseExpr= lc.loadCaseExpr)
    lcs.solve()
    for st in lc.setsToDispLoads:
        capt=lc.loadCaseDescr + ', ' + st.description + ', '  + lc.unitsLoads
        lcs.displayLoadVectors(setToDisplay=overallSet,loadCaseNm=lc.loadCaseName,caption= capt,fileName=None,defFScale=1.0)



