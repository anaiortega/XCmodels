

exec(open('../model_gen.py').read()) #FE model generation

from postprocess.xcVtk.CAD_model import vtk_CAD_graphic
displaySettings= vtk_CAD_graphic.DisplaySettingsBlockTopo()
#displaySettings.displayBlocks(setToDisplay=overallSet,caption= 'Model grid')

displaySettings.displayBlocks(setToDisplay=overallSet,caption= 'Model grid')


