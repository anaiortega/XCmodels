# -*- coding: utf-8 -*-


from materials.sia262 import SIA262_limit_state_checking

import os
#Project directory structure
execfile("../env_config.py")

execfile("../sectionsDef.py")
lsd.LimitStateData.envConfig= cfg

#Information about element sections.
sectionNamesForEveryElement= ElementSectionMap.loadShellElementSectionMap()

limitStateLabel= lsd.fatigueResistance.label
lsd.fatigueResistance.controller= SIA262_limit_state_checking.FatigueController(limitStateLabel)
lsd.fatigueResistance.check(sections,sectionNamesForEveryElement)


