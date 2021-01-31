# -*- coding: utf-8 -*-
from postprocess.control_vars import *


model_path="../"
#Project directory structure
exec(open(model_path+'env_config.py').read()))

modelDataInputFile=model_path+"model_data.py" #data for FE model generation
exec(open(modelDataInputFile).read()))


#Load properties to display:
preprocessor= model.getPreprocessor()
fName= cfg.projectDirTree.getVerifNormStrFile()
exec(open(fName).read()))
exec(open('../captionTexts.py').read()))

limitStateLabel= lsd.normalStressesResistance.label

#Possible arguments: 'CF', 'N', 'My', 'Mz'
argument= 'CF'


# if("FCCP" in attributeName):
#   extrapolate_elem_attr.flatten_attribute(xcSet.elements,attributeName,1,2)

#Set of shell elements to display
#setDisp= deckSet
#setDisp= foundSet
setDisp= shellElements
oh= output_handler.OutputHandler(modelSpace)
oh.outputStyle.cameraParameters= cameraParameters
oh.displayFieldDirs1and2(limitStateLabel,argument,setToDisplay=setDisp,component=None, fileName= None)




