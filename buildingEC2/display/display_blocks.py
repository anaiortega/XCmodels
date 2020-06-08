execfile('../model_data.py')
from postprocess.xcVtk.CAD_model import vtk_CAD_graphic

displaySettings= vtk_CAD_graphic.DisplaySettingsBlockTopo()
totalSet= model.getPreprocessor().getSets.getSet('total')
displaySettings.displayBlocks(setToDisplay=totalSet ,caption= 'Model grid')


