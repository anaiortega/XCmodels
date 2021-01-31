# -*- coding: utf-8 -*-
from postprocess.control_vars import *
from postprocess import limit_state_data as lsd
from postprocess.xcVtk import vtk_graphic_base
from postprocess import output_handler

exec(open("../model_gen.py").read())) #FE model generation

#Load properties to display:
exec(open(cfg.projectDirTree.getVerifShearFile()).read()))


#  Config
argument= 'CF'       #Possible arguments: 'CF', 'N', 'My', 'Mz', 'Mu', 'Vy',
                     #'Vz', 'theta', 'Vcu', 'Vsu', 'Vu'
setDisp= decks

rgMinMax=(0,1.0)     #truncate values to be included in the range
                     #(if None -> don't truncate)
#  End config
oh= output_handler.OutputHandler(modelSpace)
oh.displayFieldDirs1and2(limitStateLabel=lsd.shearResistance.label,argument=argument,setToDisplay= setDisp,component=None,fileName=None, defFScale=0.0,rgMinMax=rgMinMax)





