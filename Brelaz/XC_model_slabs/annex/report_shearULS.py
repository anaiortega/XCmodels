# -*- coding: utf-8 -*-
from postprocess.control_vars import *
from postprocess.reports import graphical_reports
from postprocess import limit_state_data as lsd

model_path="../"

modelDataInputFile=model_path+"model_data.py" #data for FE model generation
execfile(modelDataInputFile)

#Load properties to display:
preprocessor= FEcase.getPreprocessor
execfile(projectDirs.getShearULSFileName())
execfile('../captionTexts.py')

pathGrph= cfg.projectDirTree.getReportShearGrPath()   #directory to place the figures
                                        #(do not use ./text/....)'

limitStateLabel= lsd.shearResistance.label


# Ordered list of sets (defined in model_data.py as instances of
# utils_display.setToDisplay) to be included in the report
setsShEl=[deckSet]
# Ordered list of arguments to be included in the report
# Possible arguments: 'CF', 'N', 'My', 'Mz', 'Mu', 'Vy', 'Vz', 'theta', 'Vcu', 'Vsu', 'Vu'
argsShEl= ['CF','N', 'My', 'Mz','Vu'] 
# Ordered list of lists [set of beam elements, view to represent this set] to
# be included in the report. 
# The sets are defined in model_data.py as instances of
# utils_display.setToDisplay and the possible views are: 'XYZPos','XNeg','XPos',
# 'YNeg','YPos','ZNeg','ZPos'  (defaults to 'XYZPos')
setsBmElView=[[beamXSet,'XYZPos']]
# Ordered list of lists [arguments, scale to represent the argument] to be
# included in the report for beam elements
# Possible arguments: 'CF', 'N', 'My', 'Mz', 'Mu', 'Vy', 'Vz', 'theta', 'Vcu', 'Vsu', 'Vu'
argsBmElScale=[['CF',1],['My',1]]



texReportFile= cfg.projectDirTree.getReportShearFile()  #laTex file where to include the graphics 
cfg.grWidth='120mm'   #width of the graphics for the tex file

graphical_reports.checksReports(limitStateLabel=limitStateLabel,setsShEl=setsShEl,argsShEl=argsShEl,capTexts=capTexts,pathGr=pathGrph,texReportFile=texReportFile,grWdt= cfg.grWidth,setsBmElView=setsBmElView,argsBmElScale=argsBmElScale)

