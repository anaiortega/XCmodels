# -*- coding: utf-8 -*-
from postprocess.control_vars import *
from postprocess import limit_state_data as lsd
from postprocess.xcVtk import vtk_graphic_base
from postprocess import output_handler

#FE model generation
execfile("../model_gen.py")

#choose env_config file:
execfile("../env_config_deck.py")
#execfile("../env_config_abutment.py")
#
#Load properties to display:
execfile(cfg.projectDirTree.getVerifNormStrFile())


#  Config
argument= 'N' #Possible arguments: 'CF', 'N', 'My','Mz'

#setDisp= setArmados  #Set of shell elements to be displayed
setDisp= setArmLosa  #Set of shell elements to be displayed
#setDisp= sets_arm_losa[2]
#setDisp= setArmCart  #Set of shell elements to be displayed
#setDisp= sets_arm_cartInt[1]
#setDisp= sets_arm_volInt[3]
#setDisp= setArmVol  #Set of shell elements to be displayed
#setDisp= setArmREstr  #Set of shell elements to be displayed
#setDisp=setArmadosEstr
#setDisp=setArmZapEstr
#setDisp=setArmMurEstr
#setDisp=aletDerSet
cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
rgMinMax=[0,1]     #truncate values to be included in the range
#rgMinMax=None                     #(if None -> don't truncate)
                     
#  End config 


oh= output_handler.OutputHandler(modelSpace)
oh.outputStyle.cameraParameters= cameraParameters
oh.displayFieldDirs1and2(limitStateLabel=lsd.normalStressesResistance.label,argument=argument,setToDisplay=setDisp,component=None,fileName=None,defFScale=0.0,rgMinMax=rgMinMax)




