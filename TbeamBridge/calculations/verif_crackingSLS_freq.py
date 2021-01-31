# -*- coding: utf-8 -*-

import os

#Project directory structure
exec(open("../env_config.py").read()))

exec(open("../sectionsDef.py").read()))

lsd.LimitStateData.envConfig= cfg

#Information about element sections.
sectionNamesForEveryElement= ElementSectionMap.loadShellElementSectionMap()

#Checking material for limit state.
limitStress= 350e6 #XXX
limitStateLabel= lsd.freqLoadsCrackControl.label
lsd.freqLoadsCrackControl.controller= cc.CrackControlSIA262PlanB(limitStateLabel,limitStress)
lsd.freqLoadsCrackControl.check(sections,sectionNamesForEveryElement)



