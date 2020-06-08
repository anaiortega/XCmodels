execfile('./xc_model_data.py')
from postprocess.xcVtk.CAD_model import vtk_CAD_graphic

displaySettings= vtk_CAD_graphic.DisplaySettingsBlockTopo()
setDisp= roof_set+parapets_set # bulkheads_set #sides_set #floor_set
displaySettings.displayBlocks(setDisp,caption= setDisp.name+' set')
