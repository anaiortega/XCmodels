exec(open('fe_model.py').read())
from postprocess.xcVtk.CAD_model import vtk_CAD_graphic

displaySettings= vtk_CAD_graphic.DisplaySettingsBlockTopo()
totalSet= deck.getPreprocessor.getSets.getSet('total')
displaySettings.displayBlocks(setToDisplay=totalSet,caption= 'Model grid')



