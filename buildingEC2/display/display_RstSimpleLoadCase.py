# -*- coding: utf-8 -*-
import os

execfile('../model_data.py')
execfile('../loadStateData.py')

#ordered list of load cases (from those defined in ../loadStateData.py
#or redefined lately) to be displayed:
loadCasesToDisplay=[ELUmaxMy,ELUmaxMz,ELUmaxVy,ELUmaxVz,ELUmaxN,ELUminMy,ELUminMz,ELUminVy,ELUminVz,ELUminN]
# loadCasesToDisplay=[LC1_deadLoadBearingStructure]
# loadCasesToDisplay=[LC2_deadLoadInterior]
#End data

for lc in loadCasesToDisplay:
    lcs=gm.QuickGraphics(model)
    #solve for load case
    lcs.solve(loadCaseName=lc.loadCaseName,loadCaseExpr=lc.loadCaseExpr)
    #Displacements and rotations displays
    for st in lc.setsToDispDspRot:
        for arg in lc.listDspRot:
            if arg[0]=='u':
                fcUn=lc.unitsScaleDispl
                unDesc=lc.unitsDispl
            else:
                fcUn=1.0
                unDesc=''
            lcs.displayDispRot(itemToDisp=arg,setToDisplay=st.elSet,fConvUnits=fcUn,unitDescription=unDesc,viewName=lc.viewName,hCamFct=lc.hCamFct,fileName=None)
    #Internal forces displays on sets of «shell» elements
    for st in lc.setsToDispIntForc:
        for arg in lc.listIntForc:
            if arg[0]=='M':
                fcUn=lc.unitsScaleMom
                unDesc=lc.unitsMom
            else:
                fcUn=lc.unitsScaleForc
                unDesc=lc.unitsForc

            lcs.displayIntForc(itemToDisp=arg,setToDisplay=st.elSet,fConvUnits= fcUn,unitDescription=unDesc,viewName=lc.viewName,hCamFct=lc.hCamFct,fileName=None)
    #Internal forces displays on sets of «beam» elements
    for st in lc.setsToDispBeamIntForc:
        for arg in lc.listBeamIntForc:
            if arg[0]=='M':
                fcUn=lc.unitsScaleMom
                unDesc=lc.unitsMom
                scaleFact=lc.scaleDispBeamIntForc[2]
            else:
                fcUn=lc.unitsScaleForc
                unDesc=lc.unitsForc
                if arg[0]=='N':
                  scaleFact=lc.scaleDispBeamIntForc[0]
                else:
                  scaleFact=lc.scaleDispBeamIntForc[1]
            lcs.displayIntForcDiag(itemToDisp=arg,setToDisplay=st.elSet,fConvUnits= fcUn,scaleFactor=scaleFact,unitDescription=unDesc,viewName=lc.viewNameBeams,hCamFct=lc.hCamFctBeams,fileName=None)
