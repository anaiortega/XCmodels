# -*- coding: utf-8 -*-

exec(open('../model_data.py').read()))
exec(open('../loadStateData.py').read()))

from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import quick_graphics as qg

#ordered list of load cases (from those defined in ../loadStateData.py
#or redefined lately) to be displayed:

loadCasesToDisplay=[Q1]

#End data

for lc in loadCasesToDisplay:
    lcs= qg.LoadCaseResults(FEcase, loadCaseName=lc.loadCaseName, loadCaseExpr= lc.loadCaseExpr)
    lcs.solve()
    for st in lc.setsToDispLoads:
#        capt=lc.loadCaseDescr + ', ' + st.genDescr + ', '  + lc.unitsLoads
        capt='Prueba de carga: reparto de carga camiones sobre el dintel. [kN/m2]'
        lcs.displayLoadVectors(setToDisplay=st,caption= capt,fileName='figures/Q1_loads.jpg',defFScale=1.0)

loadCasesToDisplay=[Q2]

#End data

for lc in loadCasesToDisplay:
    lcs= qg.LoadCaseResults(FEcase, loadCaseName=lc.loadCaseName, loadCaseExpr= lc.loadCaseExpr)
    lcs.solve()
    for st in lc.setsToDispLoads:
#        capt=lc.loadCaseDescr + ', ' + st.genDescr + ', '  + lc.unitsLoads
        capt='Reparto tren cargas UIC71 (ambas vías) sobre el dintel. [kN/m2]'
        lcs.displayLoadVectors(setToDisplay=st,caption= capt,fileName='figures/Q2_loads.jpg',defFScale=1.0)

