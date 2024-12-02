import os
from postprocess.xcVtk.FE_model import quick_graphics as QGrph

exec(open('../model_data.py').read())
exec(open('../loadStateData.py').read())

#ordered list of load cases (from those defined in ../loadStateData.py
#or redefined lately) to be displayed:
loadCasesToDisplay=[Q1,Q2,Q3,PrueCarga,Qtren1via,Qtren2vias]
#loadCasesToDisplay=[PrueCarga,Qtren]
for lc in loadCasesToDisplay:
    lcs=QGrph.LoadCaseResults(FEcase)
    #solve for load case
    lcs.solve(loadCaseName=lc.loadCaseName,loadCaseExpr=lc.loadCaseExpr)
    
    listM2=list()
    elCentral=dintelBcentral.elements
    for e in elCentral:
        e.getResistingForce()
        listM2.append(e.getMeanInternalForce('m2'))
    print 'Accion:', lc.loadCaseName, '\n'
    print 'Sum of the moments at mid span: ', sum(listM2)*1e-3, 'kN.m \n'
    
