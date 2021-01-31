exec(open('../model_data.py').read()))
from postprocess.xcVtk.CAD_model import vtk_CAD_graphic

displaySettings= vtk_CAD_graphic.DisplaySettingsBlockTopo()
totalSet= model.getPreprocessor().getSets.getSet('total')
displaySettings.displayBlocks(totalSet,caption= 'Model grid')
