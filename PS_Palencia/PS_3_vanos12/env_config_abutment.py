# -*- coding: utf-8 -*-
from postprocess.config import default_config


home= '/home/ana/projects/XCmodels/PS_Palencia/PS_3_vanos12/'
 
# Default configuration of environment variables.
cfg=default_config.envConfig(language='en',intForcPath= home + 'results_abutment/internalForces/',verifPath= home + 'results_abutment/verifications/',annexPath= home + 'annex_abutment/',grWidth='120mm')

