# -*- coding: utf-8 -*-
#from postprocess.reports import graphical_reports

exec(open('../model_data.py').read())
exec(open('../../PSs/loadStateData.py').read())
exec(open('../../PSs/captionTexts.py').read())

pathGrph='res_PS101_curvo/graphics/resSimplLC/'   #directory to place the figures
                                        #(do not use ./text/....)'
texReportFile='res_PS101_curvo/report_resSimplLC.tex'  #laTex file where to include the graphics

#ordered list of load cases (from those defined in ../loadStateData.py
#or redefined lately) to be displayed:
loadCasesToDisplay=resLoadCases
cfg.grWidth='110mm'   #width of the graphics for the tex file

textfl=open(texReportFile,'w')  #tex file to be generated
for lc in loadCasesToDisplay:
    lc.simplLCReports(FEproblem=FEcase,pathGr=pathGrph,texFile=textfl,grWdt= cfg.grWidth,capStdTexts= cfg.capTexts)

textfl.close()

