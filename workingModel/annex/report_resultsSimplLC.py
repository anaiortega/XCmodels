# -*- coding: utf-8 -*-
#from postprocess.reports import graphical_reports

execfile("../model_gen.py") #FE model generation
execfile('../load_state_data.py')


#ordered list of load cases (from those defined in ../load_state_data.py
#or redefined lately) to be displayed:
loadCasesToDisplay=[G1]

outFile=cfg.projectDirTree.getReportSimplLCFile()
grPath=cfg.projectDirTree.getReportSimplLCGrPath()
textfl=open(outFile,'w')  #tex file to be generated
for lc in loadCasesToDisplay:
    lc.simplLCReports(FEproblem=FEcase,pathGr=grPath ,texFile=textfl,cfg= cfg)

textfl.close()

