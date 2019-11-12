# -*- coding: utf-8 -*-


import os

#Project directory structure
execfile("../env_config.py")

#RC sections definition.
execfile("../sectionsDef.py")



lsd.LimitStateData.internal_forces_results_directory= cfg.projectDirTree.intForcPath
lsd.LimitStateData.check_results_directory= cfg.projectDirTree.verifPath

#Information about element sections.
sectionNamesForEveryElement= ElementSectionMap.loadShellElementSectionMap()

limitStateLabel= lsd.normalStressesResistance.label
lsd.normalStressesResistance.controller= ns.BiaxialBendingNormalStressController(limitStateLabel)
lsd.normalStressesResistance.check(sections,sectionNamesForEveryElement)



