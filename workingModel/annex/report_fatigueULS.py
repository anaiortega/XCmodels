# -*- coding: utf-8 -*-
from postprocess.control_vars import *
from postprocess import limit_state_data as lsd
from postprocess.reports import graphical_reports

exec(open("../model_gen.py").read())) #FE model generation

# Ordered list of sets (defined in model_data.py as instances of
# utils_display.setToDisplay) to be included in the report
setsShEl=[deck,found]
# Ordered list of arguments to be included in the report
#Possible arguments: 'getAbsSteelStressIncrement',  'concreteBendingCF',  'concreteLimitStress',  'shearLimit' , 'concreteShearCF', 'Mu',  'Vu'
argsShEl= ['getAbsSteelStressIncrement','concreteBendingCF','concreteShearCF']
# Ordered list of lists [set of beam elements, view to represent this set] to
# be included in the report. 
# The sets are defined in model_data.py as instances of
# utils_display.setToDisplay and the possible views are: 'XYZPos','XNeg','XPos',
# 'YNeg','YPos','ZNeg','ZPos'  (defaults to 'XYZPos')
setsBmElView=[[beamX,'XYZPos']]
# Ordered list of lists [arguments, scale to represent the argument] to be
# included in the report for beam elements
# Possible arguments: 'getAbsSteelStressIncrement',  'concreteBendingCF',  'concreteLimitStress',  'shearLimit' , 'concreteShearCF', 'Mu',  'Vu'
argsBmElScale=[['Mu',1],['Mu',1]]

#Load properties to display:
exec(open(cfg.projectDirTree.getVerifFatigueFile()).read()))
limitStateLabel= lsd.fatigueResistance.label

graphical_reports.checksReports(limitStateLabel=limitStateLabel,setsShEl=setsShEl,argsShEl=argsShEl,capTexts= cfg.capTexts,pathGr= cfg.reportFatigueGrPath,texReportFile= cfg.reportFatigueFile,grWdt= cfg.grWidth,setsBmElView=setsBmElView,argsBmElScale=argsBmElScale)

