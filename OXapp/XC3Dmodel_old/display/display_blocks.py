

execfile('../model_gen.py') #FE model generation

from postprocess.xcVtk.CAD_model import vtk_CAD_graphic
defDisplay= vtk_CAD_graphic.RecordDefDisplayCAD()
setToDisplay= overallSet # columns # beams, slabs_H, slabs_L, stag2Set
defDisplay.displayBlocks(xcSet= setToDisplay,fName= None,caption= 'Model grid')



