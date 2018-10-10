# -*- coding: utf-8 -*-
import os
from postprocess.xcVtk.FE_model import quick_graphics as QGrph

execfile('../model_gen.py')
execfile('../loadStateData.py')

#ordered list of load cases (from those defined in ../loadStateData.py
#or redefined lately) to be displayed:
loadCasesToDisplay=[G1,Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8,Q9,Q10,Q11]
#loadCasesToDisplay=[LS1,LS2]
#End data

for lc in loadCasesToDisplay:
    lcs=QGrph.QuickGraphics(FEcase)
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
            lcs.displayDispRot(itemToDisp=arg,setToDisplay=st,fConvUnits=fcUn,unitDescription=unDesc,viewName=lc.viewName,hCamFct=lc.hCamFct,fileName=None,defFScale=1)
    #Internal forces displays on sets of «shell» elements
    for st in lc.setsToDispIntForc:
        for arg in lc.listIntForc:
            if arg[0]=='M':
                fcUn=lc.unitsScaleMom
                unDesc=lc.unitsMom
            else:
                fcUn=lc.unitsScaleForc
                unDesc=lc.unitsForc

            lcs.displayIntForc(itemToDisp=arg,setToDisplay=st,fConvUnits= fcUn,unitDescription=unDesc,viewName=lc.viewName,hCamFct=lc.hCamFct,fileName=None,defFScale=1)
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
            lcs.displayIntForcDiag(itemToDisp=arg,setToDisplay=st,fConvUnits= fcUn,scaleFactor=scaleFact,unitDescription=unDesc,viewName=lc.viewNameBeams,hCamFct=lc.hCamFctBeams,fileName=None,defFScale=1)


            
