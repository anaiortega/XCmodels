# -*- coding: utf-8 -*-
#from postprocess.reports import graphical_reports

exec(open("../model_gen.py").read()) #FE model generation
exec(open('../load_state_data.py').read())


#ordered list of load cases (from those defined in ../load_state_data.py
#or redefined lately) to be displayed:
loadCasesToDisplay=[G1]

outFile=cfg.projectDirTree.getReportSimplLCFile()
grPath=cfg.projectDirTree.getReportSimplLCGrPath()
textfl=open(outFile,'w')  #tex file to be generated
for lc in loadCasesToDisplay:
    lc.simplLCReports(FEproblem=FEcase,pathGr=grPath ,texFile=textfl,cfg= cfg)

textfl.close()

