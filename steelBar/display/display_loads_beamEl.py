# -*- coding: utf-8 -*-

from postprocess.xcVtk.FE_model import quick_graphics as qg

exec(open('../model_gen.py').read())
exec(open('../loadStateData.py').read())

#available components: 'axialComponent', 'transComponent', 'transYComponent',
#                      'transZComponent'

loadCasesToDisplay=[Q1]
#End data

for lc in loadCasesToDisplay:
    lcs= qg.LoadCaseResults(FEcase, loadCaseName=lc.loadCaseName, loadCaseExpr= lc.loadCaseExpr)
    lcs.solve()
    for st in lc.setsToDispBeamLoads:
        capt=lc.loadCaseDescr + ', ' + st.description + ', '  + lc.unitsLoads
        lcs.displayLoads(setToDisplay=st,elLoadComp=lc.compElLoad,caption= capt,fileName=None)

