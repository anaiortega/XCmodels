# -*- coding: utf-8 -*-

exec(open('../model_data.py').read())

from postprocess.xcVtk.FE_model import quick_graphics as qg

#ordered list of load cases (from those defined in ../loadStateData.py
#or redefined lately) to be displayed:
#loadCasesToDisplay=[G1,G2a,G2b,G2c,G3,Q1a,Q1b,Q1c,Q2b,A1a,A1b,C1]

PP=lcases.LoadCase(preprocessor=prep,name="PP",loadPType="default",timeSType="constant_ts")
PP.create()
PP.addLstLoads([Qptren_v1_e1,Qptren_v1_e2,Qptren_v1_e3,Qptren_v1_e4])
loadCasesToDisplay=[PP]
#End data

for lc in loadCasesToDisplay:
    lcs= qg.LoadCaseResults(FEcase, loadCaseName=lc.loadCaseName, loadCaseExpr= lc.loadCaseExpr)
    lcs.solve()
    lcs.displayLoadVectors(setToDisplay=overallSet,caption='',fileName=None,defFScale=1.0)



