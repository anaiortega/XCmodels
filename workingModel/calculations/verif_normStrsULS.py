# -*- coding: utf-8 -*-
from postprocess import limit_state_data as lsd
from postprocess import RC_material_distribution
from materials.sia262 import SIA262_limit_state_checking as lscheck

#Results directories
execfile("../model_gen.py") #FE model generation

#Reinforced concrete sections on each element.
#reinfConcreteSections=RC_material_distribution.RCMaterialDistribution()
#reinfConcreteSections.mapSectionsFileName='./mapSectionsReinforcement.pkl'
reinfConcreteSections= RC_material_distribution.loadRCMaterialDistribution()

setCalc=overallSet  #set of elements for which to perform the checking

limitStateLabel= lsd.normalStressesResistance.label
lsd.normalStressesResistance.controller= lscheck.BiaxialBendingNormalStressController(limitStateLabel)
meanFCs= lsd.normalStressesResistance.check(reinfConcreteSections,setCalc=setCalc)



