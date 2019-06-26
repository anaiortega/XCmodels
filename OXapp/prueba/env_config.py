# -*- coding: utf-8 -*-
from postprocess.config import default_config

#home= '/home/ana/projects/XCmodels/'
home= '/home/ana/projects/XCmodels/OXapp/'

# Default configuration of environment variables.
cfg=default_config.envConfig(language='en',intForcPath= home + 'prueba/results/internalForces/',verifPath= home + 'prueba/results/verifications/',annexPath= home + 'prueba/annex/',grWidth='120mm')
