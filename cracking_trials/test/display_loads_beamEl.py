# -*- coding: utf-8 -*-

from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import quick_graphics as qg

exec(open('./test_cracking.py').read()))

#available components: 'axialComponent', 'transComponent', 'transYComponent',
#                      'transZComponent'

lcs=qg.LoadCaseResults(FEcase)
lcs.dispLoadCaseBeamEl(loadCaseName="lcase01",setToDisplay=beamSet,fUnitConv=1e-3,elLoadComp='transComponent',elLoadScaleF=1,nodLoadScaleF=1)
quit()
#End data

for lc in loadCasesToDisplay:
    lcs= qg.LoadCaseResults(FEcase, loadCaseName=lc.loadCaseName, loadCaseExpr= lc.loadCaseExpr)
    lcs.solve()
    for st in lc.setsToDispBeamLoads:
        print 'set:', st.name
#        capt=lc.loadCaseDescr + ', ' + st.genDescr + ', '  + lc.unitsLoads
        capt=lc.loadCaseDescr + ', ' +  ', '  + lc.unitsLoads
        lcs.displayLoads(elLoadComp=lc.compElLoad,setToDisplay=st,caption= capt,fileName=None)

