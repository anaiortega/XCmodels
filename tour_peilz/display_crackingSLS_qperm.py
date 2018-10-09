# -*- coding: utf-8 -*-

from postprocess.control_vars import *
from postprocess import limit_state_data as lsd
from postprocess.xcVtk.FE_model import vtk_display_limit_state as dls
from postprocess import RC_material_distribution

execfile('xc_model_data.py') #data for FE model generation


#Load properties to display:
execfile('./results/verifications/verifRsl_crackingSLS_qperm.py')
execfile('./captionTexts.py')
#Elements with an assigned section.
reinfConcreteSectionDistribution= RC_material_distribution.loadRCMaterialDistribution()
elementsWithSection= reinfConcreteSectionDistribution.getElementSet(preprocessor)

limitStateLabel= lsd.quasiPermanentLoadsCrackControl.label
argument= 'getMaxSteelStress'
#argument= 'crackControlVarsNeg.steelStress'

setDisp= elementsWithSection

dls.displayFieldDirs1and2(limitStateLabel,argument,setDisp,None,1.0,None,capTexts)