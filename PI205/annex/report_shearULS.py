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
fName= cfg.projectDirTree.getVerifShearFile()
execfile(fName)
execfile('../captionTexts.py')

pathGrph= cfg.projectDirTree.getReportShearGrPath()   #directory to place the figures
                                        #(do not use ./text/....)'

limitStateLabel= lsd.shearResistance.label


# Ordered list of sets (defined in model_data.py as instances of
# utils_display.setToDisplay) to be included in the report
setsShEl=[deckSet,wallsSet,foundationSet]
# Ordered list of arguments to be included in the report
# Possible arguments: 'CF', 'N', 'My', 'Mz', 'Mu', 'Vy', 'Vz', 'theta', 'Vcu', 'Vsu', 'Vu'
argsShEl= ['CF'] 
texReportFile= cfg.projectDirTree.getReportShearFile()  #laTex file where to include the graphics 
cfg.grWidth='100mm'   #width of the graphics for the tex file

graphical_reports.checksReports(limitStateLabel=limitStateLabel,setsShEl=setsShEl,argsShEl=argsShEl,capTexts=capTexts,pathGr=pathGrph,texReportFile=texReportFile,grWdt= cfg.grWidth)

