# -*- coding: utf-8 -*-
from materials.sections.fiber_section import sectionReport 
from postprocess.reports import graph_material 
from postprocess import element_section_map
from postprocess import RC_material_distribution
from postprocess.control_vars import *
import matplotlib.pyplot as plt
import os
import re

execfile('./xc_model_data.py') #data for FE model generation
execfile('./sectionsDef.py') #script that carries out the section definition
execfile(cfg.projectDirTree.getVerifNormStrFile())
report_graphics_outDir= cfg.projectDirTree.getReportSectionsGrPath()

#Reinforced concrete sections on each element.
reinfConcreteSections= RC_material_distribution.loadRCMaterialDistribution()

reportFileName= cfg.projectDirTree.getReportSectionsFile()

report=open(reportFileName,'w')    #report latex file
#Functions to represent the interaction diagrams

def plotIntDiag(diag,internalForces,title,xAxLab,yAxLab,grFileNm,reportFile):
  diagGraphic=graph_material.InteractionDiagramGraphic(title)
  diagGraphic.decorations.xLabel= xAxLab
  diagGraphic.decorations.yLabel= yAxLab
  diagGraphic.setupGraphic(diag, internalForces)
  diagGraphic.savefig(grFileNm+'.eps')
  diagGraphic.savefig(grFileNm+'.jpeg')
  reportFile.write('\\begin{center}\n')
  reportFile.write('\includegraphics[width=120mm]{'+grFileNm+'}\n')
  reportFile.write('\end{center}\n')
  diagGraphic.close()

def getSectionInternalForces(elemSet,sectionName):
  retvalN= []; retvalMy= []
  suffix= ''
  for v in re.findall(r'Sect\d+', sectionName):
    suffix= v
  propName= 'ULS_normalStressesResistance'+suffix
  print '*** ', sectionName, propName
  for e in elemSet:
    if(e.hasProp(propName)):
      controlVars= e.getProp(propName)
      if(controlVars.idSection==sectionName):
        retvalN.append(controlVars.N*1e3)
        retvalMy.append(controlVars.My*1e3)
  return (retvalN, retvalMy)
  

#header
report.write('%% \documentclass{article}\n')
report.write('%% \usepackage{graphicx}\n')
report.write('%% \usepackage{multirow}\n')
report.write('%% \usepackage{wasysym}\n')
report.write('%% \usepackage{gensymb}\n\n')

report.write('%% \\begin{document}\n\n')

scSteel=None
scConcr=None
for sect in sections.sections:
  sect1=sect.lstRCSects[0]
  sect2=sect.lstRCSects[1]
  sect1.defRCSimpleSection(preprocessor,'d')
  sect2.defRCSimpleSection(preprocessor,'d')
  #plotting of steel stress-strain diagram (only if not equal to precedent steel)
  if sect1.reinfSteelType!=scSteel or sect1.concrType!=scConcr:
     scSteel=sect1.reinfSteelType
     steelDiag=scSteel.plotDesignStressStrainDiagram(preprocessor,path=report_graphics_outDir)
     steelGrphFile=scSteel.materialName+'_design_stress_strain_diagram'
     report.write('\\begin{center}\n')
     report.write('\includegraphics[width=120mm]{'+report_graphics_outDir+steelGrphFile+'}\n')
     report.write('\end{center}\n')
     scConcr=sect1.concrType
     concrDiag=scConcr.plotDesignStressStrainDiagram(preprocessor,path=report_graphics_outDir)
     concrGrphFile=scConcr.materialName+'_design_stress_strain_diagram'
     report.write('\\begin{center}\n')
     report.write('\includegraphics[width=120mm]{'+report_graphics_outDir+concrGrphFile+'}\n')
     report.write('\end{center}\n')
     report.write('\\newpage\n\n')
  #Section 1
  # plotting of section geometric and mechanical properties
  sect1inf=sectionReport.SectionInfoHASimple(preprocessor,sect1)
  texFileName=report_graphics_outDir+sect1.sectionName+'.tex'
  epsFileName=report_graphics_outDir+sect1.sectionName+'.eps'
  sect1inf.writeReport(texFileName,epsFileName)
  report.write('\input{'+texFileName+'}\n')
  # plotting of interaction diagrams
  diagNMy= sect1.defInteractionDiagramNMy(preprocessor)
  grFileName=report_graphics_outDir+sect1.sectionName+'NMy'
  sect1_internalForces= getSectionInternalForces(xcTotalSet.elements,sect1.sectionName)
  plotIntDiag(diag=diagNMy,internalForces= sect1_internalForces,title=sect1.sectionName+ ' N-My interaction diagram',xAxLab='My [kNm]',yAxLab='N [kN]',grFileNm=grFileName,reportFile=report)
  diagNMz= sect1.defInteractionDiagramNMz(preprocessor)
  grFileName=report_graphics_outDir+sect1.sectionName+'NMz'
  plotIntDiag(diag=diagNMz,internalForces= None,title=sect1.sectionName+ ' N-Mz interaction diagram',xAxLab='Mz [kNm]',yAxLab='N [kN]',grFileNm=grFileName,reportFile=report)
  #Section 2
  # plotting of section geometric and mechanical properties
  sect2inf=sectionReport.SectionInfoHASimple(preprocessor,sect2)
  texFileName=report_graphics_outDir+sect2.sectionName+'.tex'
  epsFileName=report_graphics_outDir+sect2.sectionName+'.eps'
  sect2inf.writeReport(texFileName,epsFileName)
  report.write('\input{'+texFileName+'}\n')
  # plotting of interaction diagrams
  diagNMy= sect2.defInteractionDiagramNMy(preprocessor)
  grFileName=report_graphics_outDir+sect2.sectionName+'NMy'
  sect2_internalForces= getSectionInternalForces(xcTotalSet.elements,sect2.sectionName)
  plotIntDiag(diag=diagNMy,internalForces= sect2_internalForces,title=sect2.sectionName+ ' N-My interaction diagram',xAxLab='My [kNm]',yAxLab='N [kN]',grFileNm=grFileName,reportFile=report)
  diagNMz= sect2.defInteractionDiagramNMz(preprocessor)
  grFileName=report_graphics_outDir+sect2.sectionName+'NMz'
  plotIntDiag(diag=diagNMz,internalForces= None,title=sect2.sectionName+ ' N-Mz interaction diagram',xAxLab='Mz [kNm]',yAxLab='N [kN]',grFileNm=grFileName,reportFile=report)
  
report.write('%% \end{document}\n')

report.close()
