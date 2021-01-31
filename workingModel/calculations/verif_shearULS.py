# -*- coding: utf-8 -*-
from postprocess import limit_state_data as lsd
from postprocess import RC_material_distribution
from materials.ehe import EHE_limit_state_checking as lschck  #Checking material for shear limit state according to EHE08
#from materials.sia262 import SIA262_limit_state_checking as lschck  #Checking material for shear limit state according to SIA262
from postprocess.config import default_config

# Verificacion of shear ULS for reinf. concrete elements

workingDirectory= default_config.findWorkingDirectory()+'/'
exec(open(workingDirectory+'model_gen.py').read()) #FE model generation
lsd.LimitStateData.envConfig= cfg #configuration defined in script
                                  #env_config.py

#Reinforced concrete sections on each element.
reinfConcreteSections= RC_material_distribution.loadRCMaterialDistribution()

# variables that control the output of the checking (setCalc,
# appendToResFile .py [defaults to 'N'], listFile .tex [defaults to 'N']
outCfg= lsd.VerifOutVars(setCalc=decks,appendToResFile='N',listFile='N')

limitStateLabel= lsd.shearResistance.label
lsd.shearResistance.controller= lschck.ShearController(limitStateLabel)
lsd.shearResistance.check(reinfConcreteSections,outCfg)





