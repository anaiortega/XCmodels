# -*- coding: utf-8 -*-
from postprocess.config import default_config

#home= '/home/ana/projects/XCmodels/'
home= '/home/ana/projects/XCmodels/OXapp/'

# Default configuration of environment variables.
cfg=default_config.envConfig(language='en',intForcPath= home + 'emb_lintel/results/internalForces/',verifPath= home + 'emb_lintel/results/verifications/',annexPath= home + 'emb_lintel/annex/',grWidth='120mm')
