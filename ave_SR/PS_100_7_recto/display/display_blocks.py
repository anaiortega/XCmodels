execfile('../model_data.py')
from postprocess.xcVtk.CAD_model import vtk_CAD_graphic

defDisplay= vtk_CAD_graphic.DisplaySettingsBlockTopo()
defDisplay.displayBlocks(setToDisplay=imposta,caption= 'Model grid')


