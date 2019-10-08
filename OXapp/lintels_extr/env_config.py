# -*- coding: utf-8 -*-
from postprocess.config import default_config

#home= '/home/ana/projects/XCmodels/'
home= '/home/ana/projects/XCmodels/OXapp/'

# Default configuration of environment variables.
cfg=default_config.envConfig(language='en',intForcPath= home + 'lintels_extr/results/internalForces/',verifPath= home + 'lintels_extr/results/verifications/',annexPath= home + 'lintels_extr/annex/',grWidth='120mm')
