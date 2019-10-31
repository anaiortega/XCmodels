# -*- coding: utf-8 -*-
from postprocess.config import default_config


home= '/home/ana/projects/XCmodels/'
#home= '/home/luis/Documents/XCmodels/'

# Default configuration of environment variables.
cfg=default_config.envConfig(language='sp',intForcPath= home + 'workingModel/results/internalForces/',verifPath= home + 'workingModel/results/verifications/',annexPath= home + 'workingModel/annex/',grWidth='120mm')
