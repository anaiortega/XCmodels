# -*- coding: utf-8 -*-
import os
from postprocess.xcVtk.FE_model import quick_graphics as QGrph
from postprocess.xcVtk.FE_model import vtk_FE_graphic


execfile('../model_gen.py')

execfile(path_loads_def+'load_state_data.py')

#ordered list of load cases (from those defined in ../load_state_data.py
#or redefined lately) to be displayed:
loadCasesToDisplay=LSD_disp
#loadCasesToDisplay=[Q31,Q32,Q33,Q34]
loadCasesToDisplay=[G1]
#End data
for lc in loadCasesToDisplay:
#    lc.setsToDispBeamIntForc=[struts,ties]
#    lc.setsToDispBeamIntForc=[setArmPil]+[struts,ties,piles]
    lc.setsToDispIntForc=[setArmLosa]
#    lc.listBeamIntForc=['N']
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
            lcs.displayIntForc(itemToDisp=arg,setToDisplay=st,fileName=None,defFScale=1)
    #Internal forces displays on sets of «beam» elements
    for st in lc.setsToDispBeamIntForc:
        for arg in lc.listBeamIntForc:
            lcs.displayIntForcDiag(itemToDisp=arg,setToDisplay=st,fileName=None,defFScale=1)
    # if abutment.lower()[0]=='y': 
    #     defDisplay= vtk_FE_graphic.DisplaySettingsFE() 
    #     found_wink.displayPressures(defDisplay,lc.loadCaseName +'Ground pressures',fUnitConv= 1e-6,unitDescription= '[MPa]')


            
