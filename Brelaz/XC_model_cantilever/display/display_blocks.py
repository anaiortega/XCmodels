execfile('../model_data.py')
from postprocess.xcVtk.CAD_model import vtk_CAD_graphic

setToDisp=overallSet
defDisplay= vtk_CAD_graphic.RecordDefDisplayCAD()
defDisplay.displayBlocks(xcSet=setToDisp,fName= None,caption= 'Model grid')


