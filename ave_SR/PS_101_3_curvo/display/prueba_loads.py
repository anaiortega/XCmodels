# -*- coding: utf-8 -*-

execfile('../model_data.py')

from postprocess.xcVtk.FE_model import quick_graphics as qg

#ordered list of load cases (from those defined in ../loadStateData.py
#or redefined lately) to be displayed:
PP=lcases.LoadCase(preprocessor=prep,name="PP",loadPType="default",timeSType="constant_ts")
PP.create()
PP.addLstLoads([QpuntBeams])
#eval('1.3*sc_unif_carr')


loadCasesToDisplay=[PP]
#End data

for lc in loadCasesToDisplay:
        lcs=qg.QuickGraphics(FEcase)
#        capt=lc.loadCaseDescr + ', ' + st.genDescr + ', '  + lc.unitsLoads
        lcs.dispLoadCaseBeamEl(loadCaseName='PP',setToDisplay=overallSet,fUnitConv=1,elLoadComp='transComponent',elLoadScaleF=1,nodLoadScaleF=1,viewName="XYZPos",hCamFct=1,caption= '',fileName=None)




