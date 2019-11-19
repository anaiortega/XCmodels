# -*- coding: utf-8 -*-

from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import quick_graphics as qg

execfile('../model_data.py')
execfile('../../generic_bridges/voided_slab_bridge/loadStateDataActions.py')
execfile('../../generic_bridges/voided_slab_bridge/loadStateData.py')


#available components: 'axialComponent', 'transComponent', 'transYComponent',
#                      'transZComponent'

vient=[Q2_1,Q2_2]
#loadCasesToDisplay=vient
loadCasesToDisplay=[G1]
#End data

for lc in loadCasesToDisplay:
    lcs= qg.LoadCaseResults(FEcase, loadCaseName=lc.loadCaseName, loadCaseExpr= lc.loadCaseExpr)
    lcs.solve()
    for st in lc.setsToDispBeamLoads:
        print 'set:', st.name
#        capt=lc.loadCaseDescr + ', ' + st.genDescr + ', '  + lc.unitsLoads
        capt=lc.loadCaseDescr + ', ' +  ', '  + lc.unitsLoads
        lcs.displayLoads(elLoadComp=lc.compElLoad,setToDisplay=st,caption= capt,fileName=None)

