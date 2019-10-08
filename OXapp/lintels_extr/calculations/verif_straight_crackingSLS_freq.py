# -*- coding: utf-8 -*-
from postprocess.config import output_config as oc
from solution import predefined_solutions
from postprocess import limit_state_data as lsd
from postprocess import RC_material_distribution
from materials.ehe import EHE_limit_state_checking as lschck
#from materials.ec2 import EC2_limit_state_checking

execfile("../model_gen.py") #FE model generation

# variables that control the output of the checking (setCalc,
# appendToResFile .py [defaults to 'N'], listFile .tex [defaults to 'N']
outCfg=oc.verifOutVars(setCalc=beamX,appendToResFile='N',listFile='N')

#Reinforced concrete sections on each element.
#reinfConcreteSections=RC_material_distribution.RCMaterialDistribution()
reinfConcreteSections=RC_material_distribution.loadRCMaterialDistribution()
reinfConcreteSections.mapSectionsFileName='./mapSectionsReinforcementTenStiff.pkl'
#Checking material for limit state.
limitStateLabel= lsd.freqLoadsCrackControl.label
lsd.freqLoadsCrackControl.controller= lschck.CrackStraightController(limitStateLabel= lsd.freqLoadsCrackControl.label)
lsd.freqLoadsCrackControl.controller.analysisToPerform=predefined_solutions.simple_static_modified_newton
meanFCs= lsd.freqLoadsCrackControl.check(reinfConcreteSections,outCf)


