# -*- coding: utf-8 -*-

execfile("../model_gen.py") #FE model generation

from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import vtk_FE_graphic

#  caption:  text to write in the graphic
#  defFScale: factor to apply to current displacement of nodes so that the
#             display position of each node equals to the initial position plus
#             its displacement multiplied by this factor. (Defaults to 0.0,
#             i.e. display of initial/undeformed shape)
#  fName:     name of the graphic file to create (defaults to None -> screen
#             window).
#  nodeSize:  size of the points that represent nodes (defaults to 0.01)
#  scaleConstr: scale of SPContraints symbols (defaults to 0.2)

defDisplay= vtk_FE_graphic.RecordDefDisplayEF()
setsTodisp=[overallSet]
defDisplay.displayMesh(xcSets=setsTodisp,fName=None,caption='Mesh',nodeSize=0.02,scaleConstr=0.30)
