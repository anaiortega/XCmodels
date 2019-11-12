# -*- coding: utf-8 -*-
from postprocess.control_vars import *
from postprocess import limit_state_data as lsd
from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import quick_graphics as qg

execfile("../model_gen.py") #FE model generation

#Load properties to display:
execfile(cfg.projectDirTree.getVerifNormStrFile())

#  Config
argument= 'chiLT'       #Possible arguments steel: 'CF', 'N', 'My', 'Mz','Ncrd'
                     #'McRdy','McRdz','MvRdz','MbRdz','chiLT'
setsDispRes=beamY   #list of linear elements sets for which
                                    #to display results 
setDisp=beamY   #set of elements (any type) to be displayed
scaleFactor=1        #scale factor for the diagram (can be negative)
fUnitConv=1          #unit conversion factor (i.e N->kN => fUnitConv= 1e-3)
viewName='XYZPos'    #predefined view names: 'XYZPos','XNeg','XPos','YNeg',
                     #'YPos','ZNeg','ZPos'  (defaults to 'XYZPos')
#  End config 

caption= cfg.capTexts[lsd.normalStressesResistance.label] + ', ' + cfg.capTexts[argument] + '. '#+ setsDispRes[0].description.capitalize() + ', ' 

lcs= qg.LoadCaseResults(FEcase)
lcs.displayBeamResult(attributeName=lsd.normalStressesResistance.label,itemToDisp=argument,beamSetDispRes=setsDispRes,setToDisplay=setDisp,caption=caption,fileName=None,defFScale=0.0)




