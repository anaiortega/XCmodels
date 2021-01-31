# -*- coding: utf-8 -*-

import os

#Project directory structure
exec(open("../env_config.py").read()))

from postprocess import limit_state_data as lsd
from postprocess import RC_material_distribution

#from materials.sia262 import SIA262_limit_state_checking
from materials.ehe import EHE_limit_state_checking
from solution import predefined_solutions

lsd.LimitStateData.envConfig= cfg

#Reinforced concrete sections on each element.
reinfConcreteSections= RC_material_distribution.loadRCMaterialDistribution()

#Checking material for shear limit state according to SIA262
#from materials.sia262 import SIA262_limit_state_checking
#limitStateLabel= lsd.shearResistance.label
#lsd.shearResistance.controller= SIA262_limit_state_checking.ShearController(limitStateLabel)
#lsd.shearResistance.check(reinfConcreteSections)

#Checking material for shear limit state according to EHE08
lsd.shearResistance.controller= EHE_limit_state_checking.ShearController(limitStateLabel= lsd.shearResistance.label)
#lsd.shearResistance.controller.solutionProcedureType= predefined_solutions.PlainNewtonRaphson
#(FEcheckedModel,meanFCs)= reinfConcreteSections.runChecking(lsd.shearResistance,outputFileName='/tmp/resVerif', matDiagType="d",threeDim= True)  
lsd.shearResistance.check(reinfConcreteSections)




