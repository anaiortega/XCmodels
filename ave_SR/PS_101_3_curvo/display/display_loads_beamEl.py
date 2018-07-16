# -*- coding: utf-8 -*-

from postprocess.xcVtk.FE_model import quick_graphics as qg

execfile('../model_data.py')
execfile('../../PSs/loadStateDataActions.py')
execfile('../../PSs/loadStateData.py')


#available components: 'axialComponent', 'transComponent', 'transYComponent',
#                      'transZComponent'

vient=[Q2_1,Q2_2]
loadCasesToDisplay=vient
#loadCasesToDisplay=[G1]
#End data

for lc in loadCasesToDisplay:
    for st in lc.setsToDispBeamLoads:
        print 'set:', st.name
        lcs=qg.QuickGraphics(FEcase)
#        capt=lc.loadCaseDescr + ', ' + st.genDescr + ', '  + lc.unitsLoads
        capt=lc.loadCaseDescr + ', ' +  ', '  + lc.unitsLoads
        lcs.dispLoadCaseBeamEl(loadCaseName=lc.loadCaseName,setToDisplay=st,fUnitConv=lc.unitsScaleLoads,elLoadComp=lc.compElLoad,elLoadScaleF=lc.vectorScaleLoads,nodLoadScaleF=lc.vectorScalePointLoads,viewName=lc.viewName,hCamFct=lc.hCamFct,caption= capt,fileName=None)

