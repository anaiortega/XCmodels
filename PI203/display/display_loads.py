# -*- coding: utf-8 -*-

execfile('../model_data.py')
execfile('../loadStateData.py')

from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import quick_graphics as qg

#ordered list of load cases (from those defined in ../loadStateData.py
#or redefined lately) to be displayed:
loadCasesToDisplay=[G1,G2,G3,Q1ayb,Q1a,Q1aEss,Q1b,Q1bEss,Q2ayb,Q2a,Q2aEss,Q2b,Q2bEss,Q3]

#End data

for lc in loadCasesToDisplay:
    for st in lc.setsToDispLoads:
        capt=lc.loadCaseDescr + ', ' + st.description + ', '  + lc.unitsLoads
        qg.displayLoad(preprocessor=prep,setToDisplay=overallSet,loadCaseNm=lc.loadCaseName,unitsScale=lc.unitsScaleLoads,vectorScale=lc.vectorScaleLoads, multByElemArea=lc.multByElemAreaLoads,viewDef= lc.cameraParameters,caption= capt,fileName=None,defFScale=1.0)



