# -*- coding: utf-8 -*-
from postprocess.control_vars import *
from postprocess import limit_state_data as lsd
from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import quick_graphics as qg


execfile("../model_gen.py") #FE model generation

#Load properties to display:
execfile(cfg.verifShearFile)

#  Config
argument= 'Vy'      #Available arguments:
                    # RC elements:'CF', 'N', 'My', 'Mz', 'Mu',
                    #             'Vy', 'Vz', 'theta', 'Vcu', 'Vsu', 'CF'
                    # steel elements: 
setDispRes=beamY   #list of linear elements sets for which
                                    #to display results 
setDisp=overallSet   #set of elements (any type) to be displayed
scaleFactor=1     #scale factor for the diagram (can be negative)
fUnitConv=1          #unit conversion factor (i.e N->kN => fUnitConv= 1e-3)
viewName='XYZPos'    #predefined view names: 'XYZPos','XNeg','XPos','YNeg',
                     #'YPos','ZNeg','ZPos'  (defaults to 'XYZPos')
#  End config 

caption= cfg.capTexts[lsd.shearResistance.label] + ', ' + cfg.capTexts[argument] + '. '#+ setsDispRes[0].description.capitalize() + ', ' 

qg.display_beam_result(attributeName=lsd.shearResistance.label,itemToDisp=argument,beamSetDispRes=setDispRes,setToDisplay=setDisp,fConvUnits=fUnitConv,scaleFactor=1.0,caption=caption,viewDef= vtk_graphic_base.CameraParameters('XYZPos'),fileName=None,defFScale=0.0)

