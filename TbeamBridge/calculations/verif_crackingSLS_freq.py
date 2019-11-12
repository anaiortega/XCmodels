# -*- coding: utf-8 -*-

import os

#Project directory structure
execfile("../env_config.py")

execfile("../sectionsDef.py")

lsd.LimitStateData.internal_forces_results_directory= cfg.projectDirTree.intForcPath
lsd.LimitStateData.check_results_directory= cfg.projectDirTree.verifPath

#Information about element sections.
sectionNamesForEveryElement= ElementSectionMap.loadShellElementSectionMap()

#Checking material for limit state.
limitStress= 350e6 #XXX
limitStateLabel= lsd.freqLoadsCrackControl.label
lsd.freqLoadsCrackControl.controller= cc.CrackControlSIA262PlanB(limitStateLabel,limitStress)
lsd.freqLoadsCrackControl.check(sections,sectionNamesForEveryElement)



