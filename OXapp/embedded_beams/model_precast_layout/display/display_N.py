# -*- coding: utf-8 -*-
import os
from postprocess.xcVtk.FE_model import quick_graphics as QGrph

execfile('../model_gen.py')
execfile('../load_state_data.py')

#ordered list of load cases (from those defined in ../load_state_data.py
#or redefined lately) to be displayed:
loadCasesToDisplay=[ULS01,ULS02_a,ULS02_b,ULS03_a,ULS03_b,ULS04_a,ULS04_b,ULS05_a,ULS05_b,ULS05_c,ULS05_d,ULS06_a,ULS06_b,ULS07_a,ULS07_b]
loadCasesToDisplay=[ULS01]
#End data
for lc in loadCasesToDisplay:
    lcs=QGrph.LoadCaseResults(FEcase,lc.loadCaseName,lc.loadCaseExpr)
    #solve for load case
    lcs.solve()
    #Displacements and rotations displays
    lcs.displayIntForc(itemToDisp='N1',setToDisplay=slabs)
    lcs.displayIntForc(itemToDisp='N2',setToDisplay=slabs)

    

            
