# -*- coding: utf-8 -*-
from postprocess.config import default_config

workingDirectory= default_config.findWorkingDirectory()+'/'
execfile(workingDirectory+'model_gen.py')
execfile(workingDirectory+'../../generic_bridges/voided_slab_bridge/loadStateDataActions.py')
#execfile('../../generic_bridges/voided_slab_bridge/loadStateData.py')
execfile(workingDirectory+'loadStateData.py')

from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import quick_graphics as qg

#ordered list of load cases (from those defined in ../loadStateData.py
#or redefined lately) to be displayed:

loadCasesToDisplay=resLoadCases

#End data

for lc in loadCasesToDisplay:
    lcs= qg.LoadCaseResults(FEcase, loadCaseName=lc.loadCaseName, loadCaseExpr= lc.loadCaseExpr)
    lcs.solve()
    for st in lc.setsToDispLoads:
#        capt=lc.loadCaseDescr + ', ' + st.genDescr + ', '  + lc.unitsLoads
        capt=lc.loadCaseDescr + ', '  + lc.unitsLoads
        lcs.displayLoadVectors(setToDisplay=st,caption= capt,fileName=None,defFScale=1.0)



