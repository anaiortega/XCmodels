# -*- coding: utf-8 -*-
from postprocess.control_vars import *
from postprocess import limit_state_data as lsd
from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import vtk_display_limit_state as dls


#choose env_config file:
execfile("../env_config_deck.py")
#execfile("../env_config_abutment.py")
#
#FE model generation
execfile("../model_gen.py")

#Load properties to display:
execfile(cfg.verifNormStrFile)


#  Config
argument= 'CF' #Possible arguments: 'CF', 'N', 'My','Mz'
fUnitConv=1.0  #unit conversion factor (i.e N->kN => fUnitConv= 1e-3)
setDisp= setArmados  #Set of shell elements to be displayed
#setDisp= setArmLosa  #Set of shell elements to be displayed
#setDisp= sets_arm_losa[4]
setDisp= setArmZ5
#setDisp=sets_arm_cartInt[5]
#setDisp=sets_arm_volInt[5]

#setDisp= setArmCart  #Set of shell elements to be displayed
#setDisp= setArmVol  #Set of shell elements to be displayed
#setDisp= setArmREstr  #Set of shell elements to be displayed
#setDisp=setArmadosEstr
#setDisp=setArmZapEstr
#setDisp=setArmMurEstr
#setDisp=aletDerSet
cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
rgMinMax=[0,1]     #truncate values to be included in the range
rgMinMax=None                     #(if None -> don't truncate)
                     
#  End config 


dls.displayFieldDirs1and2(limitStateLabel=lsd.normalStressesResistance.label,argument=argument,elementSet=setDisp,component=None,fUnitConv=fUnitConv,fileName=None,captionTexts=cfg.capTexts,defFScale=0.0,viewDef= cameraParameters,rgMinMax=rgMinMax)




