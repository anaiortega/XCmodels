# -*- coding: utf-8 -*-

import os

#Project directory structure
execfile("../env_config.py")

execfile("../sectionsDef.py")

lsd.LimitStateData.envConfig= cfg

#Information about element sections.
sectionNamesForEveryElement= ElementSectionMap.loadShellElementSectionMap()

#Checking material for limit state.
limitStateLabel= lsd.shearResistance.label
lsd.shearResistance.controller= SIA262_limit_state_checking.ShearController(limitStateLabel)
lsd.shearResistance.check(sections,sectionNamesForEveryElement)




