# -*- coding: utf-8 -*-
from postprocess.control_vars import *
from postprocess import limit_state_data as lsd
from postprocess.xcVtk import vtk_graphic_base
from postprocess import output_handler
from postprocess import RC_material_distribution


execfile('xc_model_data.py') #data for FE model generation


#Load properties to display:
execfile(cfg.projectDirTree.getVerifNormStrFile())
execfile('./captionTexts.py')
#Elements with an assigned section.
reinfConcreteSectionDistribution= RC_material_distribution.loadRCMaterialDistribution()
elementsWithSection= reinfConcreteSectionDistribution.getElementSet(preprocessor)

limitStateLabel= lsd.normalStressesResistance.label

#Possible arguments: 'CF', 'N', 'My', 'Mz'
argument= 'My'
setDisp= elementsWithSection
#setDisp= setDock 
#setDisp= setParapet


# if("FCCP" in attributeName):
#   extrapolate_elem_attr.flatten_attribute(xcSet.elements,attributeName,1,2)

oh= output_handler.OutputHandler(modelSpace)
#oh.outputStyle.cameraParameters= cameraParameters
oh.displayFieldDirs1and2(limitStateLabel=limitStateLabel,argument= argument,component= None, setToDisplay= setDisp,fileName= None)


