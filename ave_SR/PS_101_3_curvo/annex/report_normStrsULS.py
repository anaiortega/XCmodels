# -*- coding: utf-8 -*-
from postprocess.control_vars import *
from postprocess import limit_state_data as lsd
from postprocess.reports import graphical_reports

modelDataInputFile="../model_data.py" #data for FE model generation
exec(open(modelDataInputFile).read())

#Load properties to display:
fName= cfg.projectDirTree.getVerifNormStrFile()
exec(open(fName).read())
exec(open('../../PSs/captionTexts.py').read())

pathGrph='res_PS101_curvo/graphics/normStrsULS/'   #directory to place the figures
                                        #(do not use ./text/....)'

limitStateLabel= lsd.normalStressesResistance.label
print limitStateLabel


# Ordered list of sets (defined in model_data.py as instances of
# utils_display.setToDisplay) to be included in the report
setsShEl=[losSupV2,losInfV2,voladzCentV2,voladzExtrV2,losSupRP1,losInfRP1,voladzCentRP1,voladzExtrRP1]

# Ordered list of arguments to be included in the report
# Possible arguments: 'CF', 'N', 'My', 'Mz'
#argsShEl= ['CF','N', 'My', 'Mz'] 
argsShEl= ['CF','N', 'My'] 

# Ordered list of lists [set of beam elements, view to represent this set] to
# be included in the report. 
# The sets are defined in model_data.py as instances of
# utils_display.setToDisplay and the possible views are: 'XYZPos','XNeg','XPos',
# 'YNeg','YPos','ZNeg','ZPos'  (defaults to 'XYZPos')
#setsBmElView=[[beamX,'XYZPos']]
setsBmElView=[[pilasInf,'XYZPos'],[pilasSup,'XYZPos'],[riostrEstr1,'XYZPos']]
# Ordered list of lists [arguments, scale to represent the argument] to be
# included in the report for beam elements
# Possible arguments: 'CF', 'N', 'My', 'Mz'
#argsBmElScale=[['CF',1],['My',1]]
argsBmElScale=[['CF',1],['N',0.001],['My',0.01],['Mz',0.01]]
texReportFile='res_PS101_curvo/report_normStrsULS.tex'  #laTex file where to include the graphics 
cfg.grWidth='110mm'   #width of the graphics for the tex file

graphical_reports.checksReports(limitStateLabel=limitStateLabel,setsShEl=setsShEl,argsShEl=argsShEl,capTexts= cfg.capTexts,pathGr=pathGrph,texReportFile=texReportFile,grWdt= cfg.grWidth,setsBmElView=setsBmElView,argsBmElScale=argsBmElScale)

