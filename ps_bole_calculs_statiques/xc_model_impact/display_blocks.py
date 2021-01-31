exec(open('model_data.py').read())
from postprocess.xcVtk.CAD_model import vtk_CAD_graphic

setToDisp= totalSet
displaySettings= vtk_CAD_graphic.DisplaySettingsBlockTopo()
displaySettings.displayBlocks(setToDisplay=setToDisp,caption= 'Model grid')


