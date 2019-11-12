# -*- coding: utf-8 -*-
from postprocess.control_vars import *
from postprocess.reports import graphical_reports

model_path="../"
#Project directory structure
execfile(model_path+'env_config.py')

modelDataInputFile=model_path+"model_data.py" #data for FE model generation
execfile(modelDataInputFile)

#Load properties to display:
preprocessor= model.getPreprocessor()
fName= cfg.projectDirTree.getVerifFatigueFile()
execfile(fName)
execfile('../captionTexts.py')

pathGrph= cfg.projectDirTree.getReportFatigueGrPath()   #directory to place the figures
                                        #(do not use ./text/....)'

limitStateLabel= lsd.fatigueResistance.label


# Ordered list of sets (defined in model_data.py as instances of
# utils_display.setToDisplay) to be included in the report
setsToReport=[deckSet,foundSet]
# Ordered list of arguments to be included in the report
#Possible arguments: 'getAbsSteelStressIncrement',  'concreteBendingCF',  'concreteLimitStress',  'shearLimit' , 'concreteShearCF', 'Mu',  'Vu'
argsToReport= ['getAbsSteelStressIncrement','concreteBendingCF','concreteShearCF']
texReportFile= cfg.projectDirTree.getReportFatigueFile()  #laTex file where to include the graphics 
cfg.grWidth='100mm'   #width of the graphics for the tex file

graphical_reports.checksReports(limitStateLabel=limitStateLabel,setsToReport=setsToReport,argsToReport=argsToReport,capTexts=fatg_capTexts,pathGr=pathGrph,texReportFile=texReportFile,grWdt= cfg.grWidth)

