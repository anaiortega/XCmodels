# -*- coding: utf-8 -*-

from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import quick_graphics as qg

exec(open('../model_data.py').read()))
exec(open('../loadStateData.py').read()))

#available components: 'axialComponent', 'transComponent', 'transYComponent',
#                      'transZComponent'

loadCasesToDisplay=[Q3,Q4,Q5,Q6]

#End data

for lc in loadCasesToDisplay:
    lcs= qg.LoadCaseResults(FEcase, loadCaseName=lc.loadCaseName, loadCaseExpr= lc.loadCaseExpr)
    lcs.solve()
    for st in lc.setsToDispBeamLoads:
        print 'set:', st.name
#        capt=lc.loadCaseDescr + ', ' + st.genDescr + ', '  + lc.unitsLoads
        capt=lc.loadCaseDescr + ', ' +  ', '  + lc.unitsLoads
        lcs.displayLoads(elLoadComp=lc.compElLoad,setToDisplay=st,caption= capt,fileName=None)

