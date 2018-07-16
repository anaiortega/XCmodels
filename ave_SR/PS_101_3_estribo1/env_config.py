# -*- coding: utf-8 -*-
from postprocess.config import default_config

fullProjPath='/home/ana/projects/XCprojects/ave_SR/PS_101_3_estribo1/'
# Default configuration of environment variables.
cfg=default_config.envConfig(language='sp',intForcPath=fullProjPath+'results/internalForces/',verifPath=fullProjPath+'results/verifications/',annexPath=fullProjPath+'annex/',grWidth='120mm')
