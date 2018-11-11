# -*- coding: utf-8 -*-

execfile('./model_data.py')
execfile('./loadStateData.py')

from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import quick_graphics as qg

#ordered list of load cases (from those defined in ../loadStateData.py
#or redefined lately) to be displayed:
loadCasesToDisplay=[Q664Det1B_point]#[G1,G2,Q269A_point,Q269A_unif,Q269B_point,Q269B_unif,Q664CraneA_point,Q664CraneB_point,Q664Det1A_point,Q664Det1B_point,T]

#End data

for lc in loadCasesToDisplay:
    for st in lc.setsToDispLoads:
#        capt=lc.loadCaseDescr + ', ' + st.genDescr + ', '  + lc.unitsLoads
        capt=lc.loadCaseDescr + ', '  + lc.unitsLoads
        qg.displayLoad(preprocessor,setToDisplay=st,loadCaseNm=lc.loadCaseName,unitsScale=lc.unitsScaleLoads,vectorScale=lc.vectorScaleLoads, multByElemArea=lc.multByElemAreaLoads,viewDef= lc.cameraParameters,caption= capt,fileName=None,defFScale=1.0)



