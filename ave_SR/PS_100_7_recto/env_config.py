# -*- coding: utf-8 -*-
from postprocess.config import default_config

fullProjPath='/home/ana/projects/XCmodels/ave_SR/PS_100_7_recto/'
# Default configuration of environment variables.
cfg=default_config.envConfig(language='sp',intForcPath=fullProjPath+'results/internalForces/',verifPath=fullProjPath+'results/verifications/',annexPath=fullProjPath+'annex/',grWidth='120mm')
