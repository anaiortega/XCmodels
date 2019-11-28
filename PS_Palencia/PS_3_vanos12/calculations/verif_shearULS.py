# -*- coding: utf-8 -*-
from postprocess import limit_state_data as lsd
from postprocess import RC_material_distribution
from materials.ehe import EHE_limit_state_checking as lschck  #Checking material for shear limit state according to EHE08
#from materials.sia262 import SIA262_limit_state_checking as lschck  #Checking material for shear limit state according to SIA262

execfile("../model_gen.py") #FE model generation
lsd.LimitStateData.envConfig= cfg
#
#choose env_config file:
execfile("../env_config_deck.py")
#execfile("../env_config_abutment.py")
#
from shutil import copyfile
copyfile(cfg.intForcPath+'intForce_ULS_normalStressesResistance.csv', cfg.intForcPath+'intForce_ULS_shearResistance.csv')

#Reinforced concrete sections on each element.
reinfConcreteSections= RC_material_distribution.loadRCMaterialDistribution()
stcalc=setArmados
#stcalc=setArmVol
#stcalc=setArmCart
#stcalc=setArmLosa
#stcalc=setArmPil
#stcalc=sets_arm_losa[3]

#stcalc=setArmadosEstr
#stcalc=setArmMurEstr
#stcalc=setArmZapEstr
#stcalc=aletDerSet

# variables that control the output of the checking (setCalc,
# appendToResFile .py [defaults to 'N'], listFile .tex [defaults to 'N']
outCfg= lsd.VerifOutVars(setCalc=stcalc,appendToResFile='N',listFile='N')

limitStateLabel= lsd.shearResistance.label
lsd.shearResistance.controller= lschck.ShearController(limitStateLabel)
lsd.shearResistance.check(reinfConcreteSections,outCfg)





