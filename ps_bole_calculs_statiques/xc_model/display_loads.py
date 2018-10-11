# -*- coding: utf-8 -*-

from postprocess.xcVtk.FE_model import quick_graphics as qg

execfile('./fe_model.py')
execfile('./loadStateData.py')

#available components: 'axialComponent', 'transComponent', 'transYComponent',
#                      'transZComponent'

loadCasesToDisplay=[G2]

#End data

for lc in loadCasesToDisplay:
    for st in lc.setsToDispBeamLoads:
        lcs=qg.QuickGraphics(deck)
#        capt=lc.loadCaseDescr + ', ' + st.genDescr + ', '  + lc.unitsLoads
        capt=lc.loadCaseDescr + ', ' +  ', '  + lc.unitsLoads
        lcs.dispLoadCaseBeamEl(loadCaseName=lc.loadCaseName,setToDisplay=st,fUnitConv=lc.unitsScaleLoads,elLoadComp=lc.compElLoad,elLoadScaleF=lc.vectorScaleLoads,nodLoadScaleF=lc.vectorScalePointLoads,viewName=lc.viewName,hCamFct=lc.hCamFct,caption= capt,fileName=None)

