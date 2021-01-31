# -*- coding: utf-8 -*-

exec(open('../model_data.py').read())
#exec(open('../../PSs/captionTexts.py').read())
from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import vtk_FE_graphic

#  caption:  text to write in the graphic
#  defFScale: factor to paply to current displacement of nodes so that the
#             display position of each node equals to the initial position plus
#             its displacement multiplied by this factor. (Defaults to 0.0,
#             i.e. display of initial/undeformed shape)

#  nodeSize:  size of the points that represent nodes (defaults to 0.01)
#  scaleConstr: scale of SPContraints symbols (defaults to 0.2)

displaySettings= vtk_FE_graphic.DisplaySettingsFE()

lstSets=[zap,murestrZ1,murestrZ2,aletiZ1,aletiZ2,aletiZ3,aletdZ1,aletdZ2,aletdZ3]
if Lvoladzi >0:
    lstSets.append(voladzi)
if Lvoladzd >0:
    lstSets.append(voladzd)

#lstSets=[zap,murestr,aleti,aletd]


displaySettings.displayMesh(xcSets=lstSets,caption='P.S. 101.3. Estribo 2. Malla de elementos. Vista dorsal',nodeSize=0.050,scaleConstr=0.70)
displaySettings.displayMesh(xcSets=lstSets,caption='P.S. 101.3. Estribo 2. Malla de elementos. Vista frontal',nodeSize=0.050,scaleConstr=0.70)
