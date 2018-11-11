# -*- coding: utf-8 -*-
import os

execfile('model_data.py')
execfile('loadStateData.py')
from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import quick_graphics as qg

#ordered list of load cases (from those defined in ./loadStateData.py
#or redefined lately) to be displayed:
loadCasesToDisplay=[Snow]

for lc in loadCasesToDisplay:
    lcs= qg.QuickGraphics(gilamontDock)
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
            lcs.displayDispRot(itemToDisp=arg,setToDisplay=st,fConvUnits=fcUn,unitDescription=unDesc)
    #Display internal forces
    for st in lc.setsToDispIntForc:
        for arg in lc.listIntForc:
            if arg[0]=='M':
                fcUn=lc.unitsScaleMom
                unDesc=lc.unitsMom
            else:
                fcUn=lc.unitsScaleForc
                unDesc=lc.unitsForc
            lcs.displayIntForc(itemToDisp=arg,setToDisplay=st,fConvUnits= fcUn,unitDescription=unDesc)
