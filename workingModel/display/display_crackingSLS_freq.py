# -*- coding: utf-8 -*-
from postprocess.control_vars import *
from postprocess import limit_state_data as lsd
from postprocess.xcVtk.FE_model import vtk_display_limit_state as dls

#FE model generation
execfile("../model_gen.py")

#Load properties to display:
execfile(cfg.verifCrackFreqFile)

limitStateLabel= lsd.freqLoadsCrackControl.label
#Possible arguments: 'N', 'My','Mz','s_rmax','eps_sm','wk'
argument= 'wk'

setDisp= allShells

dls.displayFieldDirs1and2(limitStateLabel,argument,setDisp,component=None,fUnitConv=1e3,fileName=None,captionTexts=cfg.capTexts,defFScale=0.0)




