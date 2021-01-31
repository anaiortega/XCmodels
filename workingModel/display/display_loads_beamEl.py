# -*- coding: utf-8 -*-

from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import quick_graphics as qg

exec(open('../model_gen.py').read())
exec(open('../load_state_data.py').read())

#available components: 'axialComponent', 'transComponent', 'transYComponent',
#                      'transZComponent'

loadCasesToDisplay=[Q3,Q4,Q5,Q6,Q7]
#loadCasesToDisplay=[LS1,LS2]
#loadCasesToDisplay=[Q9]
#End data
#loadCasesToDisplay=[G1,Q1,Q2,Q8,Q10,Q11]
#loadCasesToDisplay=[Q3]

for lc in loadCasesToDisplay:
    lcs= qg.LoadCaseResults(FEcase, loadCaseName=lc.loadCaseName, loadCaseExpr= lc.loadCaseExpr)
    lcs.solve()
    for st in lc.setsToDispBeamLoads:
        capt=lc.loadCaseDescr + ', ' + st.description + ', '  + lc.unitsLoads
        lcs.displayLoads(elLoadComp=lc.compElLoad,setToDisplay=st,caption= capt,fileName=None)

