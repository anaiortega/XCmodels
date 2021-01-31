# -*- coding: utf-8 -*-


from materials.sia262 import SIA262_limit_state_checking

import os
#Project directory structure
exec(open("../env_config.py").read()))

exec(open("../sectionsDef.py").read()))
lsd.LimitStateData.envConfig= cfg

#Information about element sections.
sectionNamesForEveryElement= ElementSectionMap.loadShellElementSectionMap()

limitStateLabel= lsd.fatigueResistance.label
lsd.fatigueResistance.controller= SIA262_limit_state_checking.FatigueController(limitStateLabel)
lsd.fatigueResistance.check(sections,sectionNamesForEveryElement)


