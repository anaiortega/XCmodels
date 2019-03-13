# -*- coding: utf-8 -*-

from postprocess.xcVtk.FE_model import quick_graphics as qg

execfile('../model_gen.py')
execfile('../loadStateData.py')

#available components: 'axialComponent', 'transComponent', 'transYComponent',
#                      'transZComponent'

loadCasesToDisplay=[Q1]
#End data

for lc in loadCasesToDisplay:
    for st in lc.setsToDispBeamLoads:
        lcs=qg.QuickGraphics(FEcase)
        capt=lc.loadCaseDescr + ', ' + st.description + ', '  + lc.unitsLoads
        lcs.dispLoadCaseBeamEl(loadCaseName=lc.loadCaseName,setToDisplay=st,fUnitConv=lc.unitsScaleLoads,elLoadComp=lc.compElLoad,elLoadScaleF=lc.vectorScaleLoads,nodLoadScaleF=lc.vectorScalePointLoads,viewName=lc.viewName,hCamFct=lc.hCamFct,caption= capt,fileName=None)

