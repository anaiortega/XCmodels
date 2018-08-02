# -*- coding: utf-8 -*-
import os
from postprocess.xcVtk.FE_model import quick_graphics as QGrph

execfile('xc_model_data.py')
execfile('loadStateData.py')

#ordered list of load cases (from those defined in loadStateData.py
#or redefined lately) to be displayed:
loadCasesToDisplay= [G2]
#End data

for lc in loadCasesToDisplay:
    lcs=QGrph.QuickGraphics(tourRamps)
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

            
