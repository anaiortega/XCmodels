# -*- coding: utf-8 -*-

execfile('../model_data.py')
execfile('../loadStateData.py')


#ordered list of load cases (from those defined in ../loadStateData.py
#or redefined lately) to be displayed:
loadCasesToDisplay=[G1]

#End data

for lc in loadCasesToDisplay:
    for st in lc.setsToDispLoads:
        capt=lc.loadCaseDescr + ', ' + st.genDescr + ', '  + lc.unitsLoads
        model.displayLoad(setToDisplay=st.elSet,loadCaseNm=lc.loadCaseName,unitsScale=lc.unitsScaleLoads,vectorScale=lc.vectorScaleLoads, multByElemArea=lc.multByElemAreaLoads,viewDef=lc.cameraParameters,caption= capt)



