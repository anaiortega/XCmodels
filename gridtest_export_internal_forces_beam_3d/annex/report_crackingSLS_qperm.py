# -*- coding: utf-8 -*-
from postprocess.control_vars import *
from postprocess.reports import graphical_reports

model_path="../"
#Project directory structure
execfile(model_path+'project_directories.py')

modelDataInputFile=model_path+"model_data.py" #data for FE model generation
execfile(modelDataInputFile)

#Load properties to display:
preprocessor= model.getPreprocessor()
fName= model_path+check_results_directory+'verifRsl_crackingSLS_qperm.py'
execfile(fName)
execfile('../captionTexts.py')

pathGrph='text/graphics/crackingSLS_qperm/'   #directory to place the figures
                                        #(do not use ./text/....)'

limitStateLabel= lsd.quasiPermanentLoadsCrackControl.label


# Ordered list of sets (defined in model_data.py as instances of
# utils_display.setToDisplay) to be included in the report
setsToReport=[deckSet]
# Ordered list of arguments to be included in the report
# Possible arguments: 'getMaxSteelStress'
argsToReport= ['getMaxSteelStress']
texReportFile='text/report_crackingSLS_qperm.tex'  #laTex file where to include the graphics 
grWidth='120mm'   #width of the graphics for the tex file

graphical_reports.checksReports(limitStateLabel=limitStateLabel,setsToReport=setsToReport,argsToReport=argsToReport,capTexts=capTexts,pathGr=pathGrph,texReportFile=texReportFile,grWdt=grWidth)

