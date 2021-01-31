# -*- coding: utf-8 -*-
from postprocess.reports import graphical_reports

exec(open('../model_data.py').read()))
exec(open('../loadStateData.py').read()))
exec(open('../captionTexts.py').read()))
capTexts=enCapTextsSimplLC

pathGrph= cfg.projectDirTree.getReportSimplLCGrPath()   #directory to place the figures
                                        #(do not use ./text/....)'
texReportFile= cfg.projectDirTree.getReportSimplLCFile()  #laTex file where to include the graphics

#ordered list of load cases (from those defined in ../loadStateData.py
#or redefined lately) to be displayed:
#loadCasesToDisplay=[ELUmaxMy,ELUmaxMz,ELUmaxVy,ELUmaxVz,ELUmaxN,ELUminMy,ELUminMz,ELUminVy,ELUminVz,ELUminN]
loadCasesToDisplay=[ELUminVz,ELUminN]
cfg.grWidth='120mm'   #width of the graphics for the tex file

textfl=open(texReportFile,'w')  #tex file to be generated
for lc in loadCasesToDisplay:
    lc.simplLCReports(gridmodl=model,pathGr=pathGrph,texFile=textfl,grWdt= cfg.grWidth,capStdTexts=capTexts)

textfl.close()

