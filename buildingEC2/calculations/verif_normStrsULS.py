# -*- coding: utf-8 -*-


import os

#Project directory structure
exec(open("../env_config.py").read()))

#RC sections definition.
exec(open("../sectionsDef.py").read()))



lsd.LimitStateData.envConfig= cfg

#Information about element sections.
sectionNamesForEveryElement= ElementSectionMap.loadShellElementSectionMap()

limitStateLabel= lsd.normalStressesResistance.label
lsd.normalStressesResistance.controller= ns.BiaxialBendingNormalStressController(limitStateLabel)
lsd.normalStressesResistance.check(sections,sectionNamesForEveryElement)



