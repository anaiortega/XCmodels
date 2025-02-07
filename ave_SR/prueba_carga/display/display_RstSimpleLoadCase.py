# -*- coding: utf-8 -*-
import os
from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import quick_graphics as QGrph

exec(open('../model_data.py').read())
exec(open('../loadStateData.py').read())

#ordered list of load cases (from those defined in ../loadStateData.py
#or redefined lately) to be displayed:
loadCasesToDisplay=[Q1,Q2,Q3,PrueCarga,Qtren1via,Qtren2vias]

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
            
            fname='figures/'+lc.loadCaseName+'_M2.jpg'
            lcs.displayIntForc(itemToDisp=arg,setToDisplay=st,fileName=fname,defFScale=1)
    #Internal forces displays on sets of «beam» elements
    for st in lc.setsToDispBeamIntForc:
        for arg in lc.listBeamIntForc:
            lcs.displayIntForcDiag(itemToDisp=arg,setToDisplay=st,fileName=None,defFScale=1)


            
