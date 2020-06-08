execfile('../model_data.py')
from postprocess.xcVtk.CAD_model import vtk_CAD_graphic

displaySettings= vtk_CAD_graphic.DisplaySettingsBlockTopo()
displaySettings.displayBlocks(setToDisplay=lane_Bern,caption= 'Model grid')


