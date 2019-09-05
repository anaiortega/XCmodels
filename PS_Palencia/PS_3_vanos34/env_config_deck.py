# -*- coding: utf-8 -*-
from postprocess.config import default_config


home= '/home/ana/projects/XCmodels/PS_Palencia/PS_3_vanos34/'
 
# Default configuration of environment variables.
cfg=default_config.envConfig(language='en',intForcPath= home + 'results_deck/internalForces/',verifPath= home + 'results_deck/verifications/',annexPath= home + 'annex_deck/',grWidth='120mm')

