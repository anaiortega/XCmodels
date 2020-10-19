# -*- coding: utf-8 -*-
from solution import predefined_solutions
from postprocess import limit_state_data as lsd
from postprocess import RC_material_distribution
from materials.ehe import EHE_limit_state_checking as lschck
#from materials.ec2 import EC2_limit_state_checking
from postprocess.config import default_config

# Verificacion of cracking SLS under frequent loads for reinf. concrete
# elements, taking account of tension-stiffening

workingDirectory= default_config.findWorkingDirectory()+'/'
execfile(workingDirectory+'model_gen.py') #FE model generation
lsd.LimitStateData.envConfig= cfg #configuration defined in script
                                  #env_config.py

# variables that control the output of the checking (setCalc,
# appendToResFile .py [defaults to 'N'], listFile .tex [defaults to 'N']
outCfg= lsd.VerifOutVars(setCalc=beamX,appendToResFile='N',listFile='N')

#Reinforced concrete sections on each element.
#reinfConcreteSections=RC_material_distribution.RCMaterialDistribution()
reinfConcreteSections=RC_material_distribution.loadRCMaterialDistribution()
reinfConcreteSections.mapSectionsFileName='./mapSectionsReinforcementTenStiff.pkl'
#Checking material for limit state.
limitStateLabel= lsd.freqLoadsCrackControl.label
lsd.freqLoadsCrackControl.controller= lschck.CrackStraightController(limitStateLabel= lsd.freqLoadsCrackControl.label)
lsd.freqLoadsCrackControl.controller.solutionProcedureType= predefined_solutions.PlainStaticModifiedNewton
meanFCs= lsd.freqLoadsCrackControl.check(reinfConcreteSections,outCf)



