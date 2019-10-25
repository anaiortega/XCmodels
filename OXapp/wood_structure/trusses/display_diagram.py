# -*- coding: utf-8 -*-
#execfile('./xc_model.py')
execfile('./trusses_11_56.py')

#Graphic output
from postprocess.xcVtk import vtk_graphic_base
from postprocess.reports import graphical_reports as gr

loadCaseToDisplay= gr.getRecordLoadCaseDispFromLoadPattern(lp0)
loadCaseToDisplay.unitsForc='[kN]'
loadCaseToDisplay.unitsMom='[kN.m]'
loadCaseToDisplay.setToDisplay= xcTotalSet
loadCaseToDisplay.cameraParameters= vtk_graphic_base.CameraParameters('Custom')
loadCaseToDisplay.cameraParameters.viewUpVc= [0,0,1]
loadCaseToDisplay.cameraParameters.posCVc= [0,-100,0]

 
#Define the diagram to display:
# scaleFactor, unitConversionFactor, element sets and magnitude to display.

#lcs.displayIntForcDiag('N',xcTotalSet,1e-3,1,'(kN)',loadCaseToDisplay.cameraParameters)
loadCaseToDisplay.displayIntForcDiag(itemToDisp='N')
#lcs.displayIntForcDiag('Qy',xcTotalSet,1e-3,1,'(kN)',loadCaseToDisplay.cameraParameters)
