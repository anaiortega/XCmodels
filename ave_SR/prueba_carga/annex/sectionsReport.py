# -*- coding: utf-8 -*-
from materials.sections.fiber_section import section_report 
from postprocess.reports import graph_material 
import matplotlib.pyplot as plt

import os
model_path="../"
#Project directory structure
exec(open(model_path+'env_config.py').read())
modelDataInputFile=model_path+'model_data.py' #data for FE model generation
exec(open(modelDataInputFile).read())
sectDataInputFile=model_path+'sectionsDef.py'  #script that carries out the section definition
exec(open(sectDataInputFile).read())
report_graphics_outDir= cfg.projectDirTree.getReportSectionsGrPath()

reportDir='./text'     #directory where sections report will be placed


reportFileName= cfg.projectDirTree.getReportSectionsFile()

report=open(reportFileName,'w')    #report latex file
#Functions to represent the interaction diagrams

def plotIntDiag(diag,title,xAxLab,yAxLab,grFileNm,reportFile):
  diagGraphic=graph_material.InteractionDiagramGraphic(title)
  diagGraphic.decorations.xLabel= xAxLab
  diagGraphic.decorations.yLabel= yAxLab
  diagGraphic.setupGraphic(diag)
  diagGraphic.savefig(grFileNm+'.eps')
  diagGraphic.savefig(grFileNm+'.jpeg')
  reportFile.write('\\begin{center}\n')
  reportFile.write('\includegraphics[width=120mm]{'+grFileNm+'}\n')
  reportFile.write('\end{center}\n')

#header
report.write('# \documentclass{article}\n')
report.write('# \usepackage{graphicx}\n')
report.write('# \usepackage{multirow}\n')
report.write('# \usepackage{wasysym}\n')
report.write('# \usepackage{gensymb}\n\n')

report.write('# \\begin{document}\n\n')

scSteel=None
scConcr=None
for sect in sections.sections:
  sect1=sect.lstRCSects[0]
  sect2=sect.lstRCSects[1]
  sect1.defRCSection(preprocessor,'d')
  sect2.defRCSection(preprocessor,'d')
  #plotting of steel stress-strain diagram (only if not equal to precedent steel)
  if sect1.fiberSectionParameters.reinfSteelType!=scSteel or sect1.fiberSectionParameters.concrType!=scConcr:
     scSteel=sect1.fiberSectionParameters.reinfSteelType
     steelDiag=scSteel.plotDesignStressStrainDiagram(preprocessor,path=report_graphics_outDir)
     steelGrphFile=scSteel.materialName+'_design_stress_strain_diagram'
     report.write('\\begin{center}\n')
     report.write('\includegraphics[width=120mm]{'+report_graphics_outDir+steelGrphFile+'}\n')
     report.write('\end{center}\n')
     scConcr=sect1.fiberSectionParameters.concrType
     concrDiag=scConcr.plotDesignStressStrainDiagram(preprocessor,path=report_graphics_outDir)
     concrGrphFile=scConcr.materialName+'_design_stress_strain_diagram'
     report.write('\\begin{center}\n')
     report.write('\includegraphics[width=120mm]{'+report_graphics_outDir+concrGrphFile+'}\n')
     report.write('\end{center}\n')
     report.write('\\newpage\n\n')
  #Section 1
  # plotting of section geometric and mechanical properties
  sect1inf=section_report.SectionInfoHASimple(preprocessor,sect1)
  texFileName=report_graphics_outDir+sect1.name+'.tex'
  epsFileName=report_graphics_outDir+sect1.name+'.eps'
  sect1inf.writeReport(texFileName,epsFileName)
  report.write('\input{'+texFileName+'}\n')
  # plotting of interaction diagrams
  diagNMy= sect1.defInteractionDiagramNMy(preprocessor)
  grFileName=report_graphics_outDir+sect1.name+'NMy'
  plotIntDiag(diag=diagNMy,title=sect1.name+ ' N-My interaction diagram',xAxLab='My [kNm]',yAxLab='N [kN]',grFileNm=grFileName,reportFile=report)
  diagNMz= sect1.defInteractionDiagramNMz(preprocessor)
  grFileName=report_graphics_outDir+sect1.name+'NMz'
  plotIntDiag(diag=diagNMz,title=sect1.name+ ' N-Mz interaction diagram',xAxLab='Mz [kNm]',yAxLab='N [kN]',grFileNm=grFileName,reportFile=report)
  #Section 2
  # plotting of section geometric and mechanical properties
  sect2inf=section_report.SectionInfoHASimple(preprocessor,sect2)
  texFileName=report_graphics_outDir+sect2.name+'.tex'
  epsFileName=report_graphics_outDir+sect2.name+'.eps'
  sect2inf.writeReport(texFileName,epsFileName)
  report.write('\input{'+texFileName+'}\n')
  # plotting of interaction diagrams
  diagNMy= sect2.defInteractionDiagramNMy(preprocessor)
  grFileName=report_graphics_outDir+sect2.name+'NMy'
  plotIntDiag(diag=diagNMy,title=sect2.name+ ' N-My interaction diagram',xAxLab='My [kNm]',yAxLab='N [kN]',grFileNm=grFileName,reportFile=report)
  diagNMz= sect2.defInteractionDiagramNMz(preprocessor)
  grFileName=report_graphics_outDir+sect2.name+'NMz'
  plotIntDiag(diag=diagNMz,title=sect2.name+ ' N-Mz interaction diagram',xAxLab='Mz [kNm]',yAxLab='N [kN]',grFileNm=grFileName,reportFile=report)
  
report.write('# \end{document}\n')

report.close()
