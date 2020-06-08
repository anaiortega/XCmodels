execfile('../model_data.py')
from postprocess.xcVtk.CAD_model import vtk_CAD_graphic

defDisplay= vtk_CAD_graphic.DisplaySettingsBlockTopo()
totalSet= model.getPreprocessor().getSets.getSet('total')
defDisplay.displayBlocks(totalSet,caption= 'Model grid')

