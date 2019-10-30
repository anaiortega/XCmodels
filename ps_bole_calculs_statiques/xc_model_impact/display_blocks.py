execfile('model_data.py')
from postprocess.xcVtk.CAD_model import vtk_CAD_graphic

setToDisp= totalSet
defDisplay= vtk_CAD_graphic.RecordDefDisplayCAD()
defDisplay.displayBlocks(setToDisplay=setToDisp,caption= 'Model grid')


