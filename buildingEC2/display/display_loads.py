# -*- coding: utf-8 -*-

exec(open('../model_data.py').read())
exec(open('../loadStateData.py').read())


#ordered list of load cases (from those defined in ../loadStateData.py
#or redefined lately) to be displayed:
loadCasesToDisplay=[LC1_deadLoadBearingStructure,LC2_deadLoadInterior,LC3_deadLoadFacade,LC51_windX,LC101_windY,LC201_snowRoof,LC202_snowAx1_2,LC203_snowAx2_3,LC204_snowAx3_4,LC205_snowAx4_5,LC206_snowAx5_6,LC1326_servRoof,LC1336_servRoof,LC1356_servRoof,LC1366_servRoof,LC10001_serv1,LC10011_serv1,LC10021_serv1,LC10031_serv1,LC10101_servParking,LC10111_servParking,LC10121_servParking,LC10131_servParking]

#End data

for lc in loadCasesToDisplay:
    lcs= qg.LoadCaseResults(FEcase, loadCaseName=lc.loadCaseName, loadCaseExpr= lc.loadCaseExpr)
    lcs.solve()
    for st in lc.setsToDispLoads:
        capt=lc.loadCaseDescr + ', ' + st.genDescr + ', '  + lc.unitsLoads
        model.displayLoad(setToDisplay=st.elSet,loadCaseNm=lc.loadCaseName,caption= capt,fileName=None)



