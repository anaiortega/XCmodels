execfile('../model_data.py')
from postprocess.xcVtk.CAD_model import vtk_CAD_graphic

setToDisp=lin2Glue01+lin2Glue02+lin2Glue03+lin2Glue04+lin2Glue05+lin2Glue06+lin2Glue07+lin2Glue08+lin2Glue09+lin2Glue10+lin2Glue11+lin2Glue12+lin2Glue13+lin2Glue14
setToDisp=lin2Glue13+lin2Glue14
displaySettings= vtk_CAD_graphic.DisplaySettingsBlockTopo()
displaySettings.displayBlocks(setToDisplay=setToDisp,caption= 'Model grid')


