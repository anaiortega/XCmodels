execfile('../model_gen.py')
from postprocess.xcVtk.CAD_model import vtk_CAD_graphic

displaySettings= vtk_CAD_graphic.DisplaySettingsBlockTopo()
displaySettings.displayBlocks(setToDisplay=imposta,caption= 'Model grid')


