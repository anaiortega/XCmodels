# -*- coding: utf-8 -*-

import os

#Project directory structure
execfile("../env_config.py")

execfile("../sectionsDef.py")

lsd.LimitStateData.envConfig= cfg

#Information about element sections.
sectionNamesForEveryElement= ElementSectionMap.loadShellElementSectionMap()

#Checking material for limit state.
limitStress= 350e6 #XXX 
limitStateLabel= lsd.quasiPermanentLoadsCrackControl.label
lsd.quasiPermanentLoadsCrackControl.controller= cc.CrackControlSIA262PlanB(limitStateLabel,limitStress)
lsd.quasiPermanentLoadsCrackControl.check(sections,sectionNamesForEveryElement)

