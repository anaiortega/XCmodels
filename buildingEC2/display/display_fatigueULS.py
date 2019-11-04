# -*- coding: utf-8 -*-
from postprocess.control_vars import *


model_path="../"
#Project directory structure
execfile(model_path+'project_directories.py')

modelDataInputFile=model_path+"model_data.py" #data for FE model generation
execfile(modelDataInputFile)


#Load properties to display:
preprocessor= model.getPreprocessor()
fName= model_path+check_results_directory+'verifRsl_fatigueULS.py'
execfile(fName)
execfile('../captionTexts.py')


limitStateLabel= lsd.fatigueResistance.label

#Possible arguments: 'getAbsSteelStressIncrement',  'concreteBendingCF',  'concreteLimitStress',  'shearLimit' , 'concreteShearCF', 'Mu',  'Vu'

argument='getAbsSteelStressIncrement'

setDisp= shellElements
oh= output_handler.OutputHandler(modelSpace)
oh.outputStyle.cameraParameters= cameraParameters
oh.displayFieldDirs1and2(limitStateLabel,argument,setToDisplay=setDisp,component=None, fileName= None)



