# -*- coding: utf-8 -*-

execfile('xc_model_data.py')
execfile('captionTexts.py')
from postprocess.xcVtk.FE_model import vtk_FE_graphic
import vtk


displaySettings= vtk_FE_graphic.DisplaySettingsFE()
setToDisp= xcTotalSet #impactOnBody #totalSet

displaySettings.FEmeshGraphic(xcSet= setToDisp,caption='',cameraParameters= vtk_graphic_base.CameraParameters('-X+Y+Z'),defFScale=1.0)

writer = vtk.vtkXMLUnstructuredGridWriter();
writer.SetFileName("test.vtp");
writer.SetInputData(displaySettings.gridRecord.uGrid)
writer.Write()
