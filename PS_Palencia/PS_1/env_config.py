# -*- coding: utf-8 -*-
from postprocess.config import default_config

home= '/home/ana/projects/XCmodels/PS_Palencia/PS_1/'

# Default configuration of environment variables.
cfg=default_config.envConfig(language='en',intForcPath= home + 'results/internalForces/',verifPath= home + 'results/verifications/',annexPath= home + 'annex/',grWidth='120mm')
