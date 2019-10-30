# -*- coding: utf-8 -*-

from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import vtk_FE_graphic
from postprocess.xcVtk.fields import load_vector_field as lvf

execfile('model_data.py')
execfile('loadStateData.py')


#ordered list of load cases (from those defined in ../loadStateData.py
#or redefined lately) to be displayed:
#loadCasesToDisplay=[G1,G2,G3,QA,QB,T,Snow,EQ]
loadCasesToDisplay=[QA,QB]

#End data

for lc in loadCasesToDisplay:
    lcs= qg.LoadCaseResults(FEcase, loadCaseName=lc.loadCaseName, loadCaseExpr= lc.loadCaseExpr)
    lcs.solve()
    for st in lc.setsToDispLoads:
#        capt=lc.loadCaseDescr + ', ' + st.genDescr + ', '  + lc.unitsLoads
        capt=lc.loadCaseDescr + ', ' + lc.unitsLoads
#        model.displayLoad(setToDisplay=st.elSet,loadCaseNm=lc.loadCaseName,caption= capt)
        defDisplay= vtk_FE_graphic.RecordDefDisplayEF()
        defDisplay.setupGrid(st)
        vField=lvf.LoadVectorField(lc.loadCaseName,lc.unitsScaleLoads,lc.vectorScaleLoads)
        vField.multiplyByElementArea=lc.multByElemAreaLoads
        vField.dumpLoads(preprocessor)
        defDisplay.cameraParameters= lc.viewDef
        defDisplay.defineMeshScene(None) 
        vField.addToDisplay(defDisplay)
        defDisplay.displayScene(caption=capt)
 


