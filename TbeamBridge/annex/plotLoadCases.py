# -*- coding: utf-8 -*-
import os
model_path="../"
#Project directory structure
execfile(model_path+'env_config.py')
modelDataInputFile=model_path+"model_data.py" #data for FE model generation
execfile(modelDataInputFile)

loads_graphics_outDir= cfg.projectDirTree.getReportLoadsGrPath()

from postprocess.reports import graphLoadCase

textfl=open('./LoadCsGrForAnnex.tex','w')  #tex file to be generated

loadCasesGr=[]    #List of objects of type graphLoadCase.LoadCaseDispParameters
                  #to be considered
  # Definition of record objects with these attributes:
  #  loadCaseName:   name of the load case to be depicted
  #  setToDisplay:   set of elements to be displayed
  #                  (defaults to total set)
  #  unitsScale:     factor to apply to the results if we want to change
  #                  the units (defaults to 1).
  #  vectorScale:    factor to apply to the vectors length in the 
  #                  representation (defaults to 1).
  #  multByElemArea: boolean value that must be True if we want to 
  #                  represent the total load on each element 
  #                  (=load multiplied by element area) and False if we 
  #                  are going to depict the value of the uniform load 
  #                  per unit area (defaults to False)
  #  cameraParameters:  parameters that define the position and orientation of the
  #                     camera (defaults to "XYZPos")
  #  descGrph:       description text to be displayed in the graphic
  #  captTex:        caption to describe the graphic content in the tex file
  #  lablTex:        label to be associated to the graphic in the tex file

G1=graphLoadCase.LoadCaseDispParameters('GselfWeight')
#G1.setToDisplay=walls
G1.unitsScale=1e-3
G1.vectorScale=0.1
G1.descGrph='G1: Self weigth. [Units: m, kN]'
G1.lablTex='G1'
loadCasesGr.append(G1)

G2=graphLoadCase.LoadCaseDispParameters('GdeadLoad')
#G2.setToDisplay=foundation
G2.unitsScale=1e-3
G2.vectorScale=0.1
G2.descGrph='G2: Dead load. [Units: m, kN]'
G2.lablTex='G2'
loadCasesGr.append(G2)


G3=graphLoadCase.LoadCaseDispParameters('GearthPress')
#G3.setToDisplay=deck
G3.unitsScale=1e-3
G3.vectorScale=0.2
G3.descGrph='G3: Earth pressure. [Units: m, kN]'
G3.lablTex='G3'
loadCasesGr.append(G3)

Q1ayb=graphLoadCase.LoadCaseDispParameters('QtrafSit1unif')
Q1ayb.unitsScale=1e-3
Q1ayb.vectorScale=0.5
Q1ayb.descGrph='Q1ayb: Traffic distributed loads, configurations 1a and 1b. [Units: m, kN]'
Q1ayb.lablTex='Q1ayb'
loadCasesGr.append(Q1ayb)

Q1a=graphLoadCase.LoadCaseDispParameters('QtrafSit1a')
Q1a.unitsScale=1e-3
Q1a.vectorScale=0.05
Q1a.descGrph='Q1a: Traffic punctual loads, configuration 1a. [Units: m, kN]'
Q1a.lablTex='Q1a'
loadCasesGr.append(Q1a)

Q1b=graphLoadCase.LoadCaseDispParameters('QtrafSit1b')
Q1b.unitsScale=1e-3
Q1b.vectorScale=0.05
Q1b.descGrph='Q1b: Traffic punctual loads, configuration 1b. [Units: m, kN]'
Q1b.lablTex='Q1b'
loadCasesGr.append(Q1b)

Q2ayb=graphLoadCase.LoadCaseDispParameters('QtrafSit2unif')
Q2ayb.unitsScale=1e-3
Q2ayb.vectorScale=0.5
Q2ayb.descGrph='Q2ayb: Traffic distributed loads, configurations 2a and 2b. [Units: m, kN]'
Q2ayb.lablTex='Q2ayb'
loadCasesGr.append(Q2ayb)

Q2a=graphLoadCase.LoadCaseDispParameters('QtrafSit2a')
Q2a.unitsScale=1e-3
Q2a.vectorScale=0.05
Q2a.descGrph='Q2a: Traffic punctual loads, configuration 2a. [Units: m, kN]'
Q2a.lablTex='Q2a'
loadCasesGr.append(Q2a)

Q2b=graphLoadCase.LoadCaseDispParameters('QtrafSit2b')
Q2b.unitsScale=1e-3
Q2b.vectorScale=0.05
Q2b.descGrph='Q2b: Traffic punctual loads, configuration 2b. [Units: m, kN]'
Q2b.lablTex='Q2b'
loadCasesGr.append(Q2b)



#Generation of graphics and insertion in tex file for the annex
grWidth='120mm'   #width of the graphics for the tex file
for i in range(0,len(loadCasesGr)):
  lc=loadCasesGr[i]
  lc.createGraphicFile(model,loads_graphics_outDir+lc.loadCaseName+'.jpg')
  lc.createGraphicFile(model,loads_graphics_outDir+lc.loadCaseName+'.eps')
  lc.insertGraphic(loads_graphics_outDir+lc.loadCaseName,grWidth,textfl)

textfl.close()
 
