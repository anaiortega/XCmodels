# -*- coding: utf-8 -*-
import os

exec(open('../model_data.py').read()))
exec(open('../loadStateData.py').read()))

#ordered list of load cases (from those defined in ../loadStateData.py
#or redefined lately) to be displayed:
loadCasesToDisplay=[Q1]

#End data

for lc in loadCasesToDisplay:
    lcs=QGrph.LoadCaseResults(model,lc.loadCaseName,lc.loadCaseExpr)
    #solve for load case
    lcs.solve()
    #Displacements and rotations displays
    for st in lc.setsToDispDspRot:
        for arg in lc.listDspRot:
            lcs.displayDispRot(itemToDisp=arg,setToDisplay=st.elSet)
    #Internal forces displays
    for st in lc.setsToDispIntForc:
        for arg in lc.listIntForc:
            lcs.displayIntForc(itemToDisp=arg,setToDisplay=st.elSet)


