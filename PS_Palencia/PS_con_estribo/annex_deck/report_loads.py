# -*- coding: utf-8 -*-
from postprocess.reports import graphical_reports

#execfile("../env_config.py")
execfile("../model_gen.py") #FE model generation
execfile("../env_config_deck.py")

execfile(path_loads_def+'load_state_data.py')

pathGrph= cfg.projectDirTree.getReportLoadsGrPath()   #directory to place the figures
                                  #(do not use ./text/....)'
texReportFile= cfg.projectDirTree.getReportLoadsFile()  #laTex file where to include the graphics 
#ordered list of load cases (from those defined in ../load_state_data.py
#or redefined lately) to be displayed:
loadCasesToDisplay=[G1]
cfg.grWidth='120mm'   #width of the graphics for the tex file

textfl=open(texReportFile,'w')  #tex file to be generated
for lc in loadCasesToDisplay:
    lc.loadReports(FEcase=FEcase,pathGr=pathGrph,texFile=textfl,grWdt= cfg.grWidth)
    

textfl.close()
  
