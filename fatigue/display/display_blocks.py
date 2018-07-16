execfile('../model_data.py')
from postprocess.xcVtk.CAD_model import vtk_CAD_graphic

defDisplay= vtk_CAD_graphic.RecordDefDisplayCAD()
totalSet= model.getPreprocessor().getSets.getSet('total')
defDisplay.displayBlocks(xcSet=totalSet,fName= None,caption= 'Model grid')



