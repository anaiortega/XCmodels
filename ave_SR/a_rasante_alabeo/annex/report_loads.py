# -*- coding: utf-8 -*-
from postprocess.reports import graphical_reports

exec(open('../model_data.py').read()))
exec(open('../loadStateData.py').read()))


pathGrph='res_alabeo/graphics/loads/'   #directory to place the figures
                                  #(do not use ./text/....)'
texReportFile='res_alabeo/report_loads.tex'  #laTex file where to include the graphics 
#ordered list of load cases (from those defined in ../loadStateData.py
#or redefined lately) to be displayed:
loadCasesToDisplay=[Q1a,Q1a1via,Q1a_alabTot,Q1a1via_alabTot]
loadCasesToDisplay=[Q1a1via_alabTot]
cfg.grWidth='110mm'   #width of the graphics for the tex file

textfl=open(texReportFile,'w')  #tex file to be generated
for lc in loadCasesToDisplay:
    lc.loadReports(FEcase=FEcase,pathGr=pathGrph,texFile=textfl,grWdt= cfg.grWidth)

textfl.close()
  
