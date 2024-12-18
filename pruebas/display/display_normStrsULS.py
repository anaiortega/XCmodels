# -*- coding: utf-8 -*-
from postprocess.control_vars import *
from postprocess import limit_state_data as lsd
from postprocess.xcVtk import vtk_graphic_base
from postprocess import output_handler


#FE model generation
exec(open("../model_gen.py").read())

#Load properties to display:
exec(open(cfg.projectDirTree.getVerifNormStrFile()).read())


#  Config
argument= 'N' #'CF' #Possible arguments: 'CF', 'N', 'My','Mz'

setDisp= foot  #Set of shell elements to be displayed
cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
rgMinMax=(0,1.0)     #truncate values to be included in the range
                     #(if None -> don't truncate)
#  End config 

oh= output_handler.OutputHandler(modelSpace)
oh.outputStyle.cameraParameters= cameraParameters
oh.displayFieldDirs1and2(limitStateLabel=lsd.normalStressesResistance.label,argument=argument,setToDisplay=setDisp,component=None,fileName=None,defFScale=0.0,rgMinMax=rgMinMax)




