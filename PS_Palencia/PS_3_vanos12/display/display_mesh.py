# -*- coding: utf-8 -*-

execfile("../model_gen.py") #FE model generation

from postprocess.xcVtk.FE_model import vtk_FE_graphic

#  caption:  text to write in the graphic
#  defFScale: factor to apply to current displacement of nodes so that the
#             display position of each node equals to the initial position plus
#             its displacement multiplied by this factor. (Defaults to 0.0,
#             i.e. display of initial/undeformed shape)

#  nodeSize:  size of the points that represent nodes (defaults to 0.01)
#  scaleConstr: scale of SPContraints symbols (defaults to 0.2)

displaySettings= vtk_FE_graphic.DisplaySettingsFE()
#setsTodisp=[tablVano1,tablVano3,viaFictIzq_cent,viaFictDer_cent,pilas]
setsTodisp=sets_arm_losa+sets_arm_cartInt+sets_arm_cartExt+sets_arm_volInt+sets_arm_volExt
setsTodisp=[setArmados]
#setsTodisp=setArmREstr
setsTodisp=sets_arm_losa+[pilasBarlov]
#setsTodisp=[setArmPil]
#setsTodisp=[aceras,viaFictDer,viaFictIzq]
#setsTodisp=[calzada]
#setsTodisp=[aceras,viaFictDer_vano2,viaFictIzq_vano2]
#setsTodisp=allsets
#setsTodisp=[zapEstr,murestrZ1,murestrZ2,murestrZ3,aletiZ1,aletiZ2,aletiZ3,aletdZ1,aletdZ2,aletdZ3]
#setsTodisp=[setArmados+setArmadosEstr]
#setsTodisp=[setArmados]
#setsTodisp=[setArmPil,struts,ties]
#setsTodisp=[zapEstr,murestrZ1,murestrZ2,murestrZ3,aletiZ1,aletiZ2,aletiZ3,aletdZ1,aletdZ2,aletdZ3]
#setsTodisp=[setArmZapEstr]
setsTodisp=setsTablPilas+setsEstribo+[pilasSotav,ties,struts,piles]
setsTodisp=[calzada,aceras]
displaySettings.displayMesh(xcSets=setsTodisp,caption='Mesh',nodeSize=0.5,scaleConstr=0.30)
