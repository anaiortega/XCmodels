# -*- coding: utf-8 -*-

exec(open('../model_data.py').read()))
exec(open('../loadStateData.py').read()))


#ordered list of load cases (from those defined in ../loadStateData.py
#or redefined lately) to be displayed:
loadCasesToDisplay=[Q1]

#End data

for lc in loadCasesToDisplay:
    for st in lc.setsToDispLoads:
        capt=lc.loadCaseDescr + ', ' + st.genDescr + ', '  + lc.unitsLoads
        model.displayLoad(setToDisplay=st.elSet,loadCaseNm=lc.loadCaseName,unitsScale=lc.unitsScaleLoads,vectorScale=lc.vectorScaleLoads, multByElemArea=lc.multByElemAreaLoads,viewDef=lc.cameraParameters,caption= capt)



