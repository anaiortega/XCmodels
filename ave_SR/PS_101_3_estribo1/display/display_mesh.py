# -*- coding: utf-8 -*-

execfile('../model_data.py')
execfile('../../PSs/captionTexts.py')
from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import vtk_FE_graphic

#  caption:  text to write in the graphic
#  defFScale: factor to paply to current displacement of nodes so that the
#             display position of each node equals to the initial position plus
#             its displacement multiplied by this factor. (Defaults to 0.0,
#             i.e. display of initial/undeformed shape)
#  fName:     name of the graphic file to create (defaults to None -> screen
#             window).
#  nodeSize:  size of the points that represent nodes (defaults to 0.01)
#  scaleConstr: scale of SPContraints symbols (defaults to 0.2)

defDisplay= vtk_FE_graphic.RecordDefDisplayEF()

lstSets=[zap,murestrZ1,murestrZ2,aletiZ1,aletiZ2,aletiZ3,aletdZ1,aletdZ2,aletdZ3]
if Lvoladzi >0:
    lstSets.append(voladzi)
if Lvoladzd >0:
    lstSets.append(voladzd)
                   
lstSets=[zap,murestr,aleti,aletd]



#defDisplay.displayMesh(xcSets=[pilasInf,pilasSup,losInf,losSup,murAlig,murExtAlig,voladzCent,voladzExtr],fName= None,caption='Mesh',nodeSize=0.030,scaleConstr=0.70)
#defDisplay.displayMesh(xcSets=[losInf,losSup,murAlig,murExtAlig,voladzCent],fName= None,caption='Mesh',nodeSize=0.030,scaleConstr=0.70)
#defDisplay.displayMesh(xcSets=lstSets,fName= 'estribo1.jpg',caption='P.S. 101.3. Estribo 1. Malla de elementos',nodeSize=0.050,scaleConstr=0.70)
#defDisplay.displayMesh(xcSets=lstSets,fName= None,caption='P.S. 101.3. Estribo 1. Malla de elementos',nodeSize=0.050,scaleConstr=0.70)
defDisplay.displayMesh(xcSets=lstSets,fName= 'estribo1_dors.jpg',caption='P.S. 101.3. Estribo 1. Malla de elementos. Vista dorsal',nodeSize=0.050,scaleConstr=0.70)
defDisplay.displayMesh(xcSets=lstSets,fName= 'estribo1_fron.jpg',caption='P.S. 101.3. Estribo 1. Malla de elementos. Vista frontal',nodeSize=0.050,scaleConstr=0.70)

