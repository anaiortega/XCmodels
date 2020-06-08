# -*- coding: utf-8 -*-
'''Displays model block topology.'''

execfile('./model_data.py')
from postprocess.xcVtk.CAD_model import vtk_CAD_graphic

displaySettings= vtk_CAD_graphic.DisplaySettingsBlockTopo()

displaySettings.displayBlocks(xcTotalSet,caption= xcTotalSet.name+' set')
#displaySettings.displayBlocks(setParapet,caption= setParapet.name+' set')
#displaySettings.displayBlocks(setColumns,caption= setColumns.name+' set')
#displaySettings.displayBlocks(setTransverseBeams,caption= setTransverseBeams.name+' set')
#displaySettings.displayBlocks(springLines,caption= springLines.name+' set')
