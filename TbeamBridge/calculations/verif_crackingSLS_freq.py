# -*- coding: utf-8 -*-

import os

#Project directory structure
execfile("../project_directories.py")

execfile("../sectionsDef.py")

lsd.LimitStateData.internal_forces_results_directory= '../'+internal_forces_results_directory
lsd.LimitStateData.check_results_directory= '../'+check_results_directory

#Information about element sections.
sectionNamesForEveryElement= ElementSectionMap.loadShellElementSectionMap()

#Checking material for limit state.
limitStress= 350e6 #XXX
limitStateLabel= lsd.freqLoadsCrackControl.label
lsd.freqLoadsCrackControl.controller= cc.CrackControlSIA262PlanB(limitStateLabel,limitStress)
meanFCs= lsd.freqLoadsCrackControl.check(sections,sectionNamesForEveryElement)



