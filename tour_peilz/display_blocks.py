execfile('./xc_model_data.py')
from postprocess.xcVtk.CAD_model import vtk_CAD_graphic

defDisplay= vtk_CAD_graphic.RecordDefDisplayCAD()
setDisp= roof_set+parapets_set # bulkheads_set #sides_set #floor_set
defDisplay.displayBlocks(setDisp,caption= setDisp.name+' set')
