

execfile('../model_gen.py') #FE model generation

from postprocess.xcVtk.CAD_model import vtk_CAD_graphic
defDisplay= vtk_CAD_graphic.DisplaySettingsBlockTopo()
#defDisplay.displayBlocks(setToDisplay=overallSet,caption= 'Model grid')

defDisplay.displayBlocks(setToDisplay=overallSet,caption= 'Model grid')


