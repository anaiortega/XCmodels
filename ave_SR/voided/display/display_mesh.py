# -*- coding: utf-8 -*-
from postprocess.config import default_config
workingDirectory= default_config.findWorkingDirectory()+'/'

execfile(workingDirectory+'model_gen.py')
#execfile('../../../generic_bridges/voided_slab_bridge/captionTexts.py')
from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import vtk_FE_graphic

#  caption:  text to write in the graphic
#  defFScale: factor to apply to current displacement of nodes so that the
#             display position of each node equals to the initial position plus
#             its displacement multiplied by this factor. (Defaults to 0.0,
#             i.e. display of initial/undeformed shape)

#  nodeSize:  size of the points that represent nodes (defaults to 0.01)
#  scaleConstr: scale of SPContraints symbols (defaults to 0.2)

defDisplay= vtk_FE_graphic.RecordDefDisplayEF()


#defDisplay.displayMesh(xcSets=[pilasInf,pilasSup,losInf,losSup,murAlig,murExtAlig,voladzCent,voladzExtr],caption='Mesh',nodeSize=0.030,scaleConstr=0.70)
#defDisplay.displayMesh(xcSets=[losInf,losSup,murAlig,murExtAlig,voladzCent],caption='Mesh',nodeSize=0.030,scaleConstr=0.70)
#defDisplay.displayMesh(xcSets=[riostrEstr1,riostrEstr2],caption='Mesh',nodeSize=0.030,scaleConstr=0.70)

#defDisplay.displayMesh(xcSets=[murRP1,murRP2,murAlig,murExtAlig,losInfV2,losInfRP1],caption='Mesh',nodeSize=0.030,scaleConstr=0.70)
#defDisplay.displayMesh(xcSets=[murRP1,murRP2,diafRP1,diafRP2,murAlig,murExtAlig,losSupV2,losSupRP1],caption='Mesh',nodeSize=0.030,scaleConstr=0.70)
#defDisplay.displayMesh(xcSets=[murRP1,murRP2],caption='Mesh',nodeSize=0.030,scaleConstr=0.70)
#defDisplay.displayMesh(xcSets=[murAligV2,murExtAligV2,losInfV2],caption='Mesh',nodeSize=0.030,scaleConstr=0.70)

#defDisplay.displayMesh(xcSets=[losInf,murRP1,murRP2,diafRP1,diafRP2,murAlig,murExtAlig],caption='PS 100.7. Vista de mallado de nervios de aligeramientos y diafragmas sobre pilas',nodeSize=0.030,scaleConstr=0.70)
#defDisplay.displayMesh(xcSets=[losInf,murRP1,murRP2,diafRP1,diafRP2,murAlig,murExtAlig],caption='PS 100.7. Vista de mallado de nervios de aligeramientos y diafragmas sobre pilas',nodeSize=0.030,scaleConstr=0.70)
'''
defDisplay.displayMesh(xcSets=[pilasInf,pilasSup,losInf,losSup,murAlig,murExtAlig,murRP1,murRP2,voladzCent,voladzExtr,riostrEstr1,riostrEstr2], fileName= 'PS_100_7_01.jpg',caption='PS 100.7. Modelo de cálculo, vista superior',nodeSize=0.030,scaleConstr=0.70)
defDisplay.displayMesh(xcSets=[pilasInf,pilasSup,losInf,losSup,murAlig,murExtAlig,murRP1,murRP2,voladzCent,voladzExtr,riostrEstr1,riostrEstr2], fileName= 'PS_100_7_02.jpg',caption='PS 100.7. Modelo de cálculo, vista inferior',nodeSize=0.030,scaleConstr=0.70)
'''
#defDisplay.displayMesh(xcSets=[losInf,murRP1,murRP2,diafRP1,diafRP2,murAlig,murExtAlig],caption='PS 100.7. Modelo de cálculo, detalles',nodeSize=0.020,scaleConstr=0.70)

#defDisplay.displayMesh(xcSets=[losInf,losSup,murAlig,murExtAlig,murRP1,murRP2,voladzCent,voladzExtr,riostrEstr1,riostrEstr2],caption='PS 100.7. Modelo de cálculo, detalle',nodeSize=0.020,scaleConstr=0.70)


#defDisplay.displayMesh(xcSets=[murAligV1],caption='PS 100.7. Modelo de cálculo, detalle',nodeSize=0.020,scaleConstr=0.70)



#defDisplay.displayMesh(xcSets=[murAlig],caption='PS 100.7. Modelo de cálculo, detalle',nodeSize=0.020,scaleConstr=0.70)
#defDisplay.displayMesh(xcSets=[pilasBarlov,pilasSotav],caption='PS 100.7. Modelo de cálculo, pilas',nodeSize=0.020,scaleConstr=0.70)
#defDisplay.displayMesh(xcSets=[pilasInf,pilasSup,ties,struts,piles],caption='PS 100.7. Modelo de cálculo, pilas',nodeSize=0.020,scaleConstr=0.70)
defDisplay.displayMesh([losInf,losSup,murAlig,murExtAlig,murRP1,murRP2,voladzCent,voladzExtr,riostrEstr1,riostrEstr2]+setsEstribo+[pilasInf,pilasSup,ties,struts,piles])
