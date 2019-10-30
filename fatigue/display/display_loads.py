# -*- coding: utf-8 -*-

execfile('../model_data.py')
execfile('../loadStateData.py')


#ordered list of load cases (from those defined in ../loadStateData.py
#or redefined lately) to be displayed:
loadCasesToDisplay=[G1,Q1]

#End data

for lc in loadCasesToDisplay:
    lcs= qg.LoadCaseResults(FEcase, loadCaseName=lc.loadCaseName, loadCaseExpr= lc.loadCaseExpr)
    lcs.solve()
    for st in lc.setsToDispLoads:
        capt=lc.loadCaseDescr + ', ' + st.genDescr + ', '  + lc.unitsLoads
        model.displayLoad(setToDisplay=st.elSet,loadCaseNm=lc.loadCaseName,caption= capt,fileName=None)



