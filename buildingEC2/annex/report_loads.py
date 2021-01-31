# -*- coding: utf-8 -*-
from postprocess.reports import graphical_reports

exec(open('../model_data.py').read()))
exec(open('../loadStateData.py').read()))

pathGrph= cfg.projectDirTree.getReportLoadsGrPath()   #directory to place the figures
                                  #(do not use ./text/....)'
texReportFile= cfg.projectDirTree.getReportLoadsFile()  #laTex file where to include the graphics 
#ordered list of load cases (from those defined in ../loadStateData.py
#or redefined lately) to be displayed:
loadCasesToDisplay=[LC1_deadLoadBearingStructure,LC2_deadLoadInterior,LC3_deadLoadFacade,LC51_windX,LC101_windY,LC201_snowRoof,LC202_snowAx1_2,LC203_snowAx2_3,LC204_snowAx3_4,LC205_snowAx4_5,LC206_snowAx5_6,LC1326_servRoof,LC1336_servRoof,LC1356_servRoof,LC1366_servRoof,LC10001_serv1,LC10011_serv1,LC10021_serv1,LC10031_serv1,LC10101_servParking,LC10111_servParking,LC10121_servParking,LC10131_servParking]
cfg.grWidth='120mm'   #width of the graphics for the tex file

textfl=open(texReportFile,'w')  #tex file to be generated
for lc in loadCasesToDisplay:
    lc.loadReports(gridmodl=model,pathGr=pathGrph,texFile=textfl,grWdt= cfg.grWidth)

textfl.close()
  
