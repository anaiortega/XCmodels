# -*- coding: utf-8 -*-
from postprocess.control_vars import *
from postprocess import limit_state_data as lsd
from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import vtk_display_limit_state as dls

execfile("../model_gen.py") #FE model generation

#choose env_config file:
execfile("../env_config_deck.py")
#execfile("../env_config_abutment.py")
#
#Load properties to display:
execfile(cfg.verifShearFile)


#  Config
argument= 'CF'       #Possible arguments: 'CF', 'N', 'My', 'Mz', 'Mu', 'Vy',
                     #'Vz', 'theta', 'Vcu', 'Vsu', 'Vu'
setDisp= setArmados
#setDisp= setArmLosa
#setDisp=setArmCart
#setDisp= setArmVol
#setDisp=setArmREstr
#setDisp=setArmLosa+setArmCart+setArmVol
#setDisp=sets_arm_losa[0]
#setDisp=setArmZ4
#setDisp=sets_arm_volInt[0]
#setDisp=sets_arm_cartInt[0]
#setDisp=sets_arm_cartExt[0]

#setDisp=setArmadosEstr

fUnitConv=1.0        #Set of shell elements to be displayed
cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
rgMinMax=[0,1.1]  #truncate values to be included in the range
                     #(if None -> don't truncate)

#rgMinMax=None
#  End config 


dls.displayFieldDirs1and2(limitStateLabel=lsd.shearResistance.label,argument=argument,elementSet=setDisp,component=None,fUnitConv=fUnitConv,fileName=None,captionTexts=cfg.capTexts,defFScale=0.0,viewDef= cameraParameters,rgMinMax=rgMinMax)




