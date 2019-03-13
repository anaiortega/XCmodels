

execfile('../model_gen.py') #FE model generation

from postprocess.xcVtk.CAD_model import vtk_CAD_graphic
defDisplay= vtk_CAD_graphic.RecordDefDisplayCAD()
#defDisplay.displayBlocks(xcSet=overallSet,fName= None,caption= 'Model grid')

defDisplay.displayBlocks(xcSet=overallSet,fName= None,caption= 'Model grid')


