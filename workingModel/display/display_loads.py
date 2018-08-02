# -*- coding: utf-8 -*-

execfile("../model_gen.py") #FE model generation

execfile('../loadStateData.py')

from postprocess.xcVtk.FE_model import quick_graphics as qg

#ordered list of load cases (from those defined in ../loadStateData.py
#or redefined lately) to be displayed:
loadCasesToDisplay=[G1,Q1,Q2,Q8,Q10,Q11]
#loadCasesToDisplay=[LS1,LS2]

for lc in loadCasesToDisplay:
    for st in lc.setsToDispLoads:
#        capt=lc.loadCaseDescr + ', ' + st.genDescr + ', '  + lc.unitsLoads
        capt=lc.loadCaseDescr + ', '  + lc.unitsLoads
        qg.displayLoad(preprocessor=prep,setToDisplay=st,loadCaseNm=lc.loadCaseName,unitsScale=lc.unitsScaleLoads,vectorScale=lc.vectorScaleLoads, multByElemArea=lc.multByElemAreaLoads,viewNm=lc.viewName,hCamFct=lc.hCamFct,caption= capt,fileName=None,defFScale=1.0)



