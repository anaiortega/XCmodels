# -*- coding: utf-8 -*-

execfile('xc_model_data.py')
execfile('loadStateData.py')

from postprocess.xcVtk.FE_model import quick_graphics as qg

#ordered list of load cases (from those defined in ../loadStateData.py
#or redefined lately) to be displayed:
loadCasesToDisplay=[Q4]

#End data

for lc in loadCasesToDisplay:
    for st in lc.setsToDispLoads:
#        capt=lc.loadCaseDescr + ', ' + st.genDescr + ', '  + lc.unitsLoads
        capt=lc.loadCaseDescr + ', '  + lc.unitsLoads
        qg.displayLoad(preprocessor,setToDisplay=st,loadCaseNm=lc.loadCaseName,unitsScale=lc.unitsScaleLoads,vectorScale=lc.vectorScaleLoads, multByElemArea=lc.multByElemAreaLoads,viewNm=lc.viewName,hCamFct=lc.hCamFct,caption= capt,fileName=None,defFScale=1.0)



