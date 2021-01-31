# -*- coding: utf-8 -*-

exec(open('model_data.py').read()))

from postprocess import utils_display
from postprocess.xcVtk import vtk_internal_force_diagram as ifd


def resultAction(prb,nmbAction):
  ''' Triggers the analysis of the structure.'''
  prb.getPreprocessor.resetLoadCase()
  prb.getPreprocessor.getLoadHandler.addToDomain(nmbAction)
  #Solución
  solution= predefined_solutions.SolutionProcedure()
  analysis= solution.simpleStaticLinear(prb)
  result= analysis.analyze(1)
  prb.getPreprocessor.getLoadHandler.removeFromDomain(nmbAction)

setBeams= preprocessor.getSets.getSet("total")

internalForcesFigList= []

txtN= "Effort normal"
txtMz= "Efforts de flexion (autour de l'axe fort)"
txtVy= "Effort tranchant (parallel à l'axe faible)"


figN= utils_display.SlideDefinition("Beams","N",figDescr= txtN,reinfDescr= '',units= "[kN]")
figN.diagrams.append(ifd.InternalForceDiagram(2.0,1e-3,[setMainBeam],"N"))
figN.cameraParameters= vtk_graphic_base.CameraParameters('YPos')
internalForcesFigList.append(figN)
figMz= utils_display.SlideDefinition("Beams","Mz",figDescr= txtMz,reinfDescr= '',units= "[kN m]")
figMz.diagrams.append(ifd.InternalForceDiagram(0.05,1e-3,[setMainBeam],"Mz"))
figMz.cameraParameters= vtk_graphic_base.CameraParameters('YPos')
internalForcesFigList.append(figMz)
figVy= utils_display.SlideDefinition("Beams","Vy",figDescr= txtVy,reinfDescr= '',units= "[kN]")
figVy.diagrams.append(ifd.InternalForceDiagram(0.2,1e-3,[setMainBeam],"Qy"))
figVy.cameraParameters= vtk_graphic_base.CameraParameters('YPos')
internalForcesFigList.append(figVy)

tp= utils_display.TakePhotos("total")
#tp.displaySettings.cameraParameters= vtk_graphic_base.CameraParameters('YPos')
tp.pthGraphOutput= "figures/"

import os
for lc in loadCaseNames:
  resultAction(mainBeam,lc)
  for f in internalForcesFigList:
    f.oldVerifLabel= f.verifLabel
    f.oldDescription= f.figDescription
    f.verifLabel= '_' + lc + '_' + f.verifLabel
    f.figDescription= '\\_' + lc + ': ' + f.figDescription
  baseFileName= "results/internal_efforts_" + lc
  tp.displayFigures(preprocessor,internalForcesFigList,baseFileName+".tex",baseFileName+"_list_figures.tex")
  fTex= open(baseFileName+".tex",'a')
  fTex.write('\\cleardoublepage\n')
  fTex.close()
  for f in internalForcesFigList:
    f.verifLabel= f.oldVerifLabel
    f.figDescription= f.oldDescription
