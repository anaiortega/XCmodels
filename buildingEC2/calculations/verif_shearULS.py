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
limitStateLabel= lsd.shearResistance.label
lsd.shearResistance.controller= SIA262_limit_state_checking.ShearController(limitStateLabel)
lsd.shearResistance.check(sections,sectionNamesForEveryElement)




