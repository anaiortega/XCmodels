# -*- coding: utf-8 -*-
from postprocess.config import default_config

#home= '/home/ana/projects/XCmodels/'
home= '/home/ana/projects/XCmodels/'

# Default configuration of environment variables.
cfg=default_config.envConfig(language='en',intForcPath= home + 'cylind_model/results/internalForces/',verifPath= home + 'cylind_model/results/verifications/',annexPath= home + 'cylind_model/annex/',grWidth='120mm')
