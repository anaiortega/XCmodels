# -*- coding: utf-8 -*-
from postprocess import limit_state_data as lsd
from materials.ec3 import EC3_limit_state_checking as EC3lscheck
from postprocess.config import default_config

#Verification of normal-stresses ULS for structural steel

workingDirectory= default_config.findWorkingDirectory()+'/'
exec(open(workingDirectory+'model_gen.py').read()) #FE model generation
lsd.LimitStateData.envConfig= cfg #configuration defined in script
                                  #env_config.py

#Steel beams definition
exec(open(workingDirectory+'steel_beams_def.py').read())

setCalc=beamXsteel+columnZsteel
# variables that control the output of the checking (setCalc,
# appendToResFile .py [defaults to 'N'], listFile .tex [defaults to 'N']
outCfg= lsd.VerifOutVars(setCalc=setCalc,appendToResFile='Y',listFile='N',calcMeanCF='Y')

limitState=lsd.normalStressesResistance
limitState.controller= EC3lscheck.BiaxialBendingNormalStressController(limitState.label)
mean=limitState.runChecking(outCfg)


