# -*- coding: utf-8 -*-
from postprocess.control_vars import *
from postprocess import limit_state_data as lsd
from postprocess.reports import graphical_reports

model_path="../"
#Project directory structure
exec(open(model_path+'env_config.py').read())

modelDataInputFile=model_path+"model_data.py" #data for FE model generation
exec(open(modelDataInputFile).read())

#Load properties to display:
fName= cfg.projectDirTree.getVerifCrackQpermFile()
exec(open(fName).read())


pathGrph='res_a_rasante/graphics/crackingSLS_qperm/'   #directory to place the figures
                                        #(do not use ./text/....)'

limitStateLabel= lsd.quasiPermanentLoadsCrackControl.label


# Ordered list of sets (defined in model_data.py as instances of
# utils_display.setToDisplay) to be included in the report
setsShEl=[losas,hastIzq]
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



texReportFile='res_a_rasante/report_crackingSLS_qperm.tex'  #laTex file where to include the graphics 
cfg.grWidth='110mm'   #width of the graphics for the tex file

graphical_reports.checksReports(limitStateLabel=limitStateLabel,setsShEl=setsShEl,argsShEl=argsShEl,capTexts= cfg.capTexts,pathGr=pathGrph,texReportFile=texReportFile,grWdt= cfg.grWidth,setsBmElView=setsBmElView,argsBmElScale=argsBmElScale)

