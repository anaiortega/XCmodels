# -*- coding: utf-8 -*-
import os

exec(open('../model_data.py').read())
exec(open('../loadStateData.py').read())

#ordered list of load cases (from those defined in ../loadStateData.py
#or redefined lately) to be displayed:
loadCasesToDisplay=[ELUmaxMy,ELUmaxMz,ELUmaxVy,ELUmaxVz,ELUmaxN,ELUminMy,ELUminMz,ELUminVy,ELUminVz,ELUminN]
# loadCasesToDisplay=[LC1_deadLoadBearingStructure]
# loadCasesToDisplay=[LC2_deadLoadInterior]
#End data

for lc in loadCasesToDisplay:
    lcs=QGrph.LoadCaseResults(model,lc.loadCaseName,lc.loadCaseExpr)
    #solve for load case
    lcs.solve()
    #Displacements and rotations displays
    for st in lc.setsToDispDspRot:
        for arg in lc.listDspRot:
            lcs.displayDispRot(itemToDisp=arg,setToDisplay=st.elSet,fileName=None)
    #Internal forces displays on sets of «shell» elements
    for st in lc.setsToDispIntForc:
        for arg in lc.listIntForc:
            lcs.displayIntForc(itemToDisp=arg,setToDisplay=st.elSet,fileName=None)
    #Internal forces displays on sets of «beam» elements
    for st in lc.setsToDispBeamIntForc:
        for arg in lc.listBeamIntForc:
            lcs.displayIntForcDiag(itemToDisp=arg,setToDisplay=st.elSet,fileName=None)
