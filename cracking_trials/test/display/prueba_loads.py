# -*- coding: utf-8 -*-

exec(open('../model_data.py').read()))

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
        lcs=qg.LoadCaseResults(FEcase, loadCaseName=lc.loadCaseName, loadCaseExpr= lc.loadCaseExpr)
#        capt=lc.loadCaseDescr + ', ' + st.genDescr + ', '  + lc.unitsLoads
        lcs.dispLoadCaseBeamEl(setToDisplay=overallSet,elLoadComp='transComponent',caption= '',fileName=None)




