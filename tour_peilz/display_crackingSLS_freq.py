# -*- coding: utf-8 -*-
from postprocess.control_vars import *
from postprocess import limit_state_data as lsd
from postprocess.xcVtk import vtk_graphic_base
from postprocess import output_handler
from postprocess import RC_material_distribution

execfile('xc_model_data.py') #data for FE model generation


#Load properties to display:
execfile('./results/verifications/verifRsl_crackingSLS_freq.py')
execfile('./captionTexts.py')
#Elements with an assigned section.
reinfConcreteSectionDistribution= RC_material_distribution.loadRCMaterialDistribution()
elementsWithSection= reinfConcreteSectionDistribution.getElementSet(preprocessor)


limitStateLabel= lsd.freqLoadsCrackControl.label
argument= 'getMaxSteelStress'
#argument= 'crackControlVarsNeg.steelStress'

setDisp= elementsWithSection

oh= output_handler.OutputHandler(modelSpace)
oh.outputStyle.cameraParameters= cameraParameters
oh.displayFieldDirs1and2(limitStateLabel,argument,setToDisplay=setDisp,component=None, fileName= None)


