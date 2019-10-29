# -*- coding: utf-8 -*-

execfile('../model_data.py')
execfile('../../PSs/loadStateDataActions.py')
execfile('../../PSs/loadStateData.py')

from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import quick_graphics as qg

#ordered list of load cases (from those defined in ../loadStateData.py
#or redefined lately) to be displayed:
#Qcarro=[G2,Q1a_1_carro,Q1a_2_carro,Q1b_1_carro,Q1b_2_carro,Q1c_carro,Q1d_carro,Q1e_carro,Q1f_carro]
#qunif=[q_sit1,q_sit2,q_sit3,q_sit4,q_sit5]


loadCasesToDisplay=resLoadCases

#End data

for lc in loadCasesToDisplay:
    lcs= qg.LoadCaseResults(FEcase, loadCaseName=lc.loadCaseName, loadCaseExpr= lc.loadCaseExpr)
    lcs.solve()
    for st in lc.setsToDispLoads:
#        capt=lc.loadCaseDescr + ', ' + st.genDescr + ', '  + lc.unitsLoads
        capt=lc.loadCaseDescr + ', '  + lc.unitsLoads
        lcs.displayLoadVectors(setToDisplay=st,caption= capt,fileName=None,defFScale=1.0)



