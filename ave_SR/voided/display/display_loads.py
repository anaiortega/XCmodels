# -*- coding: utf-8 -*-
exec(open('../model_gen.py').read()))
#exec(open(workingDirectory+'../../generic_bridges/voided_slab_bridge/loadStateDataActions.py').read()))
#exec(open('../../generic_bridges/voided_slab_bridge/loadStateData.py').read()))
exec(open('../loadStateData.py').read()))

from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import quick_graphics as qg

#ordered list of load cases (from those defined in ../loadStateData.py
#or redefined lately) to be displayed:

loadCasesToDisplay=[G1,G2,Q1a1,Q1a2,Q1b1,Q1b2,Q1c,Q1d,Q1e,Q1bFren,Q1dFren,Q1eFren,Q21,Q22]

#End data

for lc in loadCasesToDisplay:
    lcs= qg.LoadCaseResults(FEcase, loadCaseName=lc.loadCaseName, loadCaseExpr= lc.loadCaseExpr)
    lcs.solve()
    for st in lc.setsToDispLoads:
#        capt=lc.loadCaseDescr + ', ' + st.genDescr + ', '  + lc.unitsLoads
        capt=lc.loadCaseDescr + ', '  + lc.unitsLoads
        lcs.displayLoadVectors(setToDisplay=st,caption= capt,fileName=None,defFScale=1.0)



