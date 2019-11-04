# -*- coding: utf-8 -*-
from postprocess.config import default_config


home= '/home/ana/projects/XCmodels/OXapp/embedded_beams/ramp_RCwalls/'
#home= '/home/luis/Documents/XCmodels/OXapp/embedded_beams/rampRC_walls/'

# Default configuration of environment variables.
cfg=default_config.envConfig(language='sp',intForcPath= home + 'results/internalForces/',verifPath= home + 'results/verifications/',annexPath= home + 'annex/',grWidth='120mm')
