# -*- coding: utf-8 -*-


from materials.sia262 import SIA262_limit_state_checking

import os
#Project directory structure
execfile("../project_directories.py")

execfile("../sectionsDef.py")
lsd.LimitStateData.internal_forces_results_directory= '../'+internal_forces_results_directory
lsd.LimitStateData.check_results_directory= '../'+check_results_directory

#Information about element sections.
sectionNamesForEveryElement= ElementSectionMap.loadShellElementSectionMap()

limitStateLabel= lsd.fatigueResistance.label
lsd.fatigueResistance.controller= SIA262_limit_state_checking.FatigueController(limitStateLabel)
lsd.fatigueResistance.check(sections,sectionNamesForEveryElement)


