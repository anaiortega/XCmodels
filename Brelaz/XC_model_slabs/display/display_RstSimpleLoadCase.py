# -*- coding: utf-8 -*-
import os
from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import quick_graphics as QGrph

execfile('../model_data.py')
execfile('../loadStateData.py')

#ordered list of load cases (from those defined in ../loadStateData.py
#or redefined lately) to be displayed:
loadCasesToDisplay=[G1,G2,QA,QB,QF,QAcc]
#loadCasesToDisplay=[ULS_A,ULS_B,ULS_Acc]
#loadCasesToDisplay=[G1]
#loadCasesToDisplay=[QAcc_point]
#End data

for lc in loadCasesToDisplay:
    lcs=QGrph.LoadCaseResults(FEcase,lc.loadCaseName,lc.loadCaseExpr)
    #solve for load case
    lcs.solve()
    #Displacements and rotations displays
    for st in lc.setsToDispDspRot:
        for arg in lc.listDspRot:
            lcs.displayDispRot(itemToDisp=arg,setToDisplay=st,fileName=None,defFScale=1)
    #Internal forces displays on sets of «shell» elements
    for st in lc.setsToDispIntForc:
        for arg in lc.listIntForc:
            lcs.displayIntForc(itemToDisp=arg,setToDisplay=st,unitDescription=unDesc,fileName=None,defFScale=1)
    # #Internal forces displays on sets of «beam» elements
    # for st in lc.setsToDispBeamIntForc:
    #     for arg in lc.listBeamIntForc:
    #         if arg[0]=='M':
    #             fcUn=lc.unitsScaleMom
    #             unDesc=lc.unitsMom
    #             scaleFact=lc.scaleDispBeamIntForc[2]
    #         else:
    #             fcUn=lc.unitsScaleForc
    #             unDesc=lc.unitsForc
    #             if arg[0]=='N':
    #               scaleFact=lc.scaleDispBeamIntForc[0]
    #             else:
    #               scaleFact=lc.scaleDispBeamIntForc[1]
    #         lcs.displayIntForcDiag(itemToDisp=arg,setToDisplay=st,fileName=None,defFScale=1)


            
