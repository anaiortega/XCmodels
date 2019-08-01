# -*- coding: utf-8 -*-
from postprocess.config import default_config

home= '/home/ana/projects/XCmodels/PS_Palencia/'

# Default configuration of environment variables.
cfg=default_config.envConfig(language='en',intForcPath= home + 'PS_3/results/internalForces/',verifPath= home + 'PS_3/results/verifications/',annexPath= home + 'PS_3/annex/',grWidth='120mm')
