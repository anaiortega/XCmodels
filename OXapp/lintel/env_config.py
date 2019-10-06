# -*- coding: utf-8 -*-
from postprocess.config import default_config

#home= '/home/ana/projects/XCmodels/'
home= '/home/ana/projects/XCmodels/OXapp/'

# Default configuration of environment variables.
cfg=default_config.envConfig(language='en',intForcPath= home + 'lintel/results/internalForces/',verifPath= home + 'lintel/results/verifications/',annexPath= home + 'lintel/annex/',grWidth='120mm')
