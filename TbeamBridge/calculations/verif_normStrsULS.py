# -*- coding: utf-8 -*-


import os

#Project directory structure
execfile("../project_directories.py")

#RC sections definition.
execfile("../sectionsDef.py")



lsd.LimitStateData.internal_forces_results_directory= '../'+internal_forces_results_directory
lsd.LimitStateData.check_results_directory= '../'+check_results_directory

#Information about element sections.
sectionNamesForEveryElement= ElementSectionMap.loadShellElementSectionMap()

limitStateLabel= lsd.normalStressesResistance.label
lsd.normalStressesResistance.controller= ns.BiaxialBendingNormalStressController(limitStateLabel)
meanFCs= lsd.normalStressesResistance.check(sections,sectionNamesForEveryElement)



