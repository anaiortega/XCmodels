# -*- coding: utf-8 -*-

from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import quick_graphics as qg

execfile('./test_cracking.py')

#available components: 'axialComponent', 'transComponent', 'transYComponent',
#                      'transZComponent'

lcs=qg.QuickGraphics(FEcase)
lcs.dispLoadCaseBeamEl(loadCaseName="lcase01",setToDisplay=beamSet,fUnitConv=1e-3,elLoadComp='transComponent',elLoadScaleF=1,nodLoadScaleF=1)
quit()
#End data

for lc in loadCasesToDisplay:
    for st in lc.setsToDispBeamLoads:
        print 'set:', st.name
        lcs=qg.QuickGraphics(FEcase)
#        capt=lc.loadCaseDescr + ', ' + st.genDescr + ', '  + lc.unitsLoads
        capt=lc.loadCaseDescr + ', ' +  ', '  + lc.unitsLoads
        lcs.dispLoadCaseBeamEl(loadCaseName=lc.loadCaseName,setToDisplay=st,fUnitConv=lc.unitsScaleLoads,elLoadComp=lc.compElLoad,elLoadScaleF=lc.vectorScaleLoads,nodLoadScaleF=lc.vectorScalePointLoads,viewDef= lc.cameraParameters,caption= capt,fileName=None)

