# -*- coding: utf-8 -*-

exec(open("../model_gen.py").read()) #FE model generation

from postprocess.xcVtk.FE_model import vtk_FE_graphic

#  caption:  text to write in the graphic
#  defFScale: factor to apply to current displacement of nodes so that the
#             display position of each node equals to the initial position plus
#             its displacement multiplied by this factor. (Defaults to 0.0,
#             i.e. display of initial/undeformed shape)

#  nodeSize:  size of the points that represent nodes (defaults to 0.01)
#  scaleConstr: scale of SPContraints symbols (defaults to 0.2)

displaySettings= vtk_FE_graphic.DisplaySettingsFE()
setsTodisp=[overallSet]
setsTodisp=[flatwall,cylwall,flatdeck,cyldeck,deck2]
displaySettings.displayMesh(xcSets=setsTodisp,caption='Mesh',nodeSize=0.02,scaleConstr=0.30)
