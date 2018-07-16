# -*- coding: utf-8 -*-

execfile('../model_data.py')
execfile('../loadStateData.py')

from postprocess.xcVtk.FE_model import quick_graphics as qg

#ordered list of load cases (from those defined in ../loadStateData.py
#or redefined lately) to be displayed:

loadCasesToDisplay=[Q1]

#End data

for lc in loadCasesToDisplay:
    for st in lc.setsToDispLoads:
#        capt=lc.loadCaseDescr + ', ' + st.genDescr + ', '  + lc.unitsLoads
        capt='Prueba de carga: reparto de carga camiones sobre el dintel. [kN/m2]'
        qg.displayLoad(preprocessor=prep,setToDisplay=st,loadCaseNm=lc.loadCaseName,unitsScale=lc.unitsScaleLoads,vectorScale=lc.vectorScaleLoads, multByElemArea=lc.multByElemAreaLoads,viewNm=lc.viewName,hCamFct=lc.hCamFct,caption= capt,fileName='figures/Q1_loads.jpg',defFScale=1.0)

loadCasesToDisplay=[Q2]

#End data

for lc in loadCasesToDisplay:
    for st in lc.setsToDispLoads:
#        capt=lc.loadCaseDescr + ', ' + st.genDescr + ', '  + lc.unitsLoads
        capt='Reparto tren cargas UIC71 (ambas vías) sobre el dintel. [kN/m2]'
        qg.displayLoad(preprocessor=prep,setToDisplay=st,loadCaseNm=lc.loadCaseName,unitsScale=lc.unitsScaleLoads,vectorScale=lc.vectorScaleLoads, multByElemArea=lc.multByElemAreaLoads,viewNm=lc.viewName,hCamFct=lc.hCamFct,caption= capt,fileName='figures/Q2_loads.jpg',defFScale=1.0)

