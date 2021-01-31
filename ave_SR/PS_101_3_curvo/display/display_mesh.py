# -*- coding: utf-8 -*-

exec(open('../model_data.py').read())
exec(open('../../PSs/captionTexts.py').read())
from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import vtk_FE_graphic

#  caption:  text to write in the graphic
#  defFScale: factor to apply to current displacement of nodes so that the
#             display position of each node equals to the initial position plus
#             its displacement multiplied by this factor. (Defaults to 0.0,
#             i.e. display of initial/undeformed shape)

#  nodeSize:  size of the points that represent nodes (defaults to 0.01)
#  scaleConstr: scale of SPContraints symbols (defaults to 0.2)

displaySettings= vtk_FE_graphic.DisplaySettingsFE()

'''
displaySettings.displayMesh(xcSets=[pilasInf,pilasSup,losInf,losSup,murAlig,murExtAlig,voladzCent,voladzExtr],caption='Mesh',nodeSize=0.030,scaleConstr=0.70)
displaySettings.displayMesh(xcSets=[losInf,losSup,murAlig,murExtAlig,voladzCent],caption='Mesh',nodeSize=0.030,scaleConstr=0.70)
displaySettings.displayMesh(xcSets=[riostrEstr1,riostrEstr2],caption='Mesh',nodeSize=0.030,scaleConstr=0.70)
displaySettings.displayMesh(xcSets=[losInf,murExtAlig],caption='Mesh',nodeSize=0.030,scaleConstr=0.70)
displaySettings.displayMesh(xcSets=[murRP1,murRP2,diafRP1,diafRP2,murAlig,murExtAlig],caption='Mesh',nodeSize=0.030,scaleConstr=0.70)
'''
#displaySettings.displayMesh(xcSets=[pilasInf,pilasSup,losInf,losSup,murAlig,murExtAlig,murRP1,murRP2,voladzCent,voladzExtr,riostrEstr1,riostrEstr2], fileName= 'PS_101_3_01.jpg',caption='PS 100.7. Modelo de cálculo, vista superior',nodeSize=0.030,scaleConstr=0.70)
#displaySettings.displayMesh(xcSets=[pilasInf,pilasSup,losInf,losSup,murAlig,murExtAlig,murRP1,murRP2,voladzCent,voladzExtr,riostrEstr1,riostrEstr2], fileName= 'PS_101_3_02.jpg',caption='PS 100.7. Modelo de cálculo, vista inferior',nodeSize=0.030,scaleConstr=0.70)
#displaySettings.displayMesh(xcSets=[losInf,murRP1,murRP2,diafRP1,diafRP2,murAlig,murExtAlig],caption='PS 101.3. Modelo de cálculo, detalles',nodeSize=0.020,scaleConstr=0.70)
#displaySettings.displayMesh(xcSets=[losInf,losSup,murAlig,murExtAlig,murRP1,murRP2,voladzCent,voladzExtr,riostrEstr1,riostrEstr2],caption='PS 101.3. Modelo de cálculo, detalle',nodeSize=0.020,scaleConstr=0.70)
#displaySettings.displayMesh(xcSets=[pilas],caption='Mesh',nodeSize=0.030,scaleConstr=0.70)
displaySettings.displayMesh(xcSets=[riostrEstr1],caption='Mesh',nodeSize=0.030,scaleConstr=0.70)
