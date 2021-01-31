# -*- coding: utf-8 -*-
from postprocess.reports import graphical_reports

exec(open("../model_gen.py").read())) #FE model generation
exec(open('../load_state_data.py').read()))
loadCasesToDisplay=[G1,Q1]

pathGrph= cfg.projectDirTree.getReportLoadsGrPath()   #directory to place the figures
                                  #(do not use ./text/....)'
texReportFile= cfg.projectDirTree.getReportLoadsFile()  #laTex file where to include the graphics 
#ordered list of load cases (from those defined in ../load_state_data.py
#or redefined lately) to be displayed:

textfl=open(texReportFile,'w')  #tex file to be generated
for lc in loadCasesToDisplay:
    lc.loadReports(FEcase=FEcase,pathGr=pathGrph,texFile=textfl,cfg= cfg)
    

textfl.close()
  
