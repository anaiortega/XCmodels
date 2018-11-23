# -*- coding: utf-8 -*-

execfile('../model_data.py')
execfile('../loadStateData.py')

from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import quick_graphics as qg

#ordered list of load cases (from those defined in ../loadStateData.py
#or redefined lately) to be displayed:
loadCasesToDisplay=[G1,G2a,G2b,G2c,G3,Q1a,Q1b,Q1c,Q2b,A1a,A1b,C1]

#End data

for lc in loadCasesToDisplay:
    for st in lc.setsToDispLoads:
#        capt=lc.loadCaseDescr + ', ' + st.genDescr + ', '  + lc.unitsLoads
        capt=lc.loadCaseDescr + ', '  + lc.unitsLoads
        qg.display_load(preprocessor=prep,setToDisplay=st,loadCaseNm=lc.loadCaseName,unitsScale=lc.unitsScaleLoads,vectorScale=lc.vectorScaleLoads, multByElemArea=lc.multByElemAreaLoads,viewDef= lc.cameraParameters,caption= capt,fileName=None,defFScale=1.0)



