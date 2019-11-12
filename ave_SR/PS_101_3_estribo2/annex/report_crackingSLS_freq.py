# -*- coding: utf-8 -*-
from postprocess.control_vars import *
from postprocess import limit_state_data as lsd
from postprocess.reports import graphical_reports

modelDataInputFile="../model_data.py" #data for FE model generation
execfile(modelDataInputFile)

#Load properties to display:
fName= '../results/verifications/verifRsl_crackingSLS_freq.py'
execfile(fName)
execfile('../../PSs/captionTexts.py')

pathGrph='res_PS101_estribo2/graphics/crackingSLS_freq/'   #directory to place the figures
                                        #(do not use ./text/....)'

limitStateLabel= lsd.freqLoadsCrackControl.label


# Ordered list of sets (defined in model_data.py as instances of
# utils_display.setToDisplay) to be included in the report
setsShEl=[zap,murestr,aleti]
# Ordered list of arguments to be included in the report
# Possible arguments: 'getMaxSteelStress', 'getCF'
argsShEl= ['getMaxSteelStress']
# Ordered list of lists [set of beam elements, view to represent this set] to
# be included in the report. 
# The sets are defined in model_data.py as instances of
# utils_display.setToDisplay and the possible views are: 'XYZPos','XNeg','XPos',
# 'YNeg','YPos','ZNeg','ZPos'  (defaults to 'XYZPos')
#setsBmElView=[[beamX,'XYZPos']]
setsBmElView=[]
# Ordered list of lists [arguments, scale to represent the argument] to be
# included in the report for beam elements
# Possible arguments: 'getMaxSteelStress', 'getCF'
#argsBmElScale=[['getCF',1],['getMaxSteelStress',1]]
argsBmElScale=[]

texReportFile='res_PS101_estribo2/report_crackingSLS_freq.tex'  #laTex file where to include the graphics 
cfg.grWidth='110mm'   #width of the graphics for the tex file

graphical_reports.checksReports(limitStateLabel=limitStateLabel,setsShEl=setsShEl,argsShEl=argsShEl,capTexts= cfg.capTexts,pathGr=pathGrph,texReportFile=texReportFile,grWdt= cfg.grWidth,setsBmElView=setsBmElView,argsBmElScale=argsBmElScale)

