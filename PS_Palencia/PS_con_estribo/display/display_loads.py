# -*- coding: utf-8 -*-

execfile("../model_gen.py") #FE model generation

execfile(path_loads_def+'load_state_data.py')

if abutment.lower()[0]=='y':
    execfile(path_loads_abutment+'load_state_data.py')
from postprocess.xcVtk.FE_model import quick_graphics as qg

#ordered list of load cases (from those defined in ../load_state_data.py
#or redefined lately) to be displayed:
loadCasesToDisplay=LSD_disp
#loadCasesToDisplay=[LS1,LS2]
loadCasesToDisplay=[G4,Q4]
for lc in loadCasesToDisplay:
    for st in lc.setsToDispLoads:
#        capt=lc.loadCaseDescr + ', ' + st.genDescr + ', '  + lc.unitsLoads
        capt=lc.loadCaseDescr + ', '  + lc.unitsLoads
        st=zapEstr+murEstrSet+aletIzqSet+aletDerSet
        qg.display_load(preprocessor=prep,setToDisplay=st,loadCaseNm=lc.loadCaseName,unitsScale=lc.unitsScaleLoads,vectorScale=lc.vectorScaleLoads, multByElemArea=lc.multByElemAreaLoads,viewDef= lc.cameraParameters,caption= capt,fileName=None,defFScale=1.0)



