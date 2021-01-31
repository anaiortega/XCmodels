# -*- coding: utf-8 -*-
from postprocess import limit_state_data as lsd
from materials.ec3 import EC3_limit_state_checking as EC3lscheck
from postprocess.config import default_config

# Verificacion of shear ULS for structural steel

workingDirectory= default_config.findWorkingDirectory()+'/'
exec(open("../model_gen.py").read())) #FE model generation
lsd.LimitStateData.envConfig= cfg

#Steel beams definition
exec(open("../steel_beams_def.py").read())) #configuration defined in script
                                  #env_config.py

setCalc=beamXsteel+columnZsteel
# variables that control the output of the checking (setCalc,
# appendToResFile .py [defaults to 'N'], listFile .tex [defaults to 'N']
outCfg= lsd.VerifOutVars(setCalc=setCalc,appendToResFile='Y',listFile='N',calcMeanCF='Y')

limitState=lsd.shearResistance
limitState.controller= EC3lscheck.ShearController(limitState.label)
a=limitState.runChecking(outCfg)


