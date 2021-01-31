# -*- coding: utf-8 -*-
from postprocess.reports import graphical_reports

exec(open('../model_data.py').read()))
exec(open('../../PSs_estribos/loadStateData.py').read()))

pathGrph='res_PS101_estribo2/graphics/loads/'   #directory to place the figures
                                  #(do not use ./text/....)'
texReportFile='res_PS101_estribo2/report_loads.tex'  #laTex file where to include the graphics 
#ordered list of load cases (from those defined in ../loadStateData.py
#or redefined lately) to be displayed:
loadCasesToDisplay=resLoadCases
cfg.grWidth='110mm'   #width of the graphics for the tex file

textfl=open(texReportFile,'w')  #tex file to be generated
for lc in loadCasesToDisplay:
    lc.loadReports(FEcase=FEcase,pathGr=pathGrph,texFile=textfl,grWdt= cfg.grWidth)

textfl.close()
  
