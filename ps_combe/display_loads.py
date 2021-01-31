# -*- coding: utf-8 -*-

exec(open('./model_data.py').read()))
exec(open('./loadStateData.py').read()))

from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import quick_graphics as qg

#ordered list of load cases (from those defined in ../loadStateData.py
#or redefined lately) to be displayed:
loadCasesToDisplay=[Q664Det1B_point]#[G1,G2,Q269A_point,Q269A_unif,Q269B_point,Q269B_unif,Q664CraneA_point,Q664CraneB_point,Q664Det1A_point,Q664Det1B_point,T]

#End data

for lc in loadCasesToDisplay:
    lcs= qg.LoadCaseResults(model, loadCaseName=lc.loadCaseName, loadCaseExpr= lc.loadCaseExpr)
    lcs.solve()
    for st in lc.setsToDispLoads:
#        capt=lc.loadCaseDescr + ', ' + st.genDescr + ', '  + lc.unitsLoads
        capt=lc.loadCaseDescr + ', '  + lc.unitsLoads
        lcs.displayLoadVectors(setToDisplay=st,caption= capt,fileName=None,defFScale=1.0)



