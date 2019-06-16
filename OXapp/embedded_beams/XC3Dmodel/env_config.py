# -*- coding: utf-8 -*-
from postprocess.config import default_config

#home= '/home/ana/projects/XCmodels/'
home= '/home/ana/projects/XCmodels/OXapp/embeddeb_beams/'

# Default configuration of environment variables.
cfg=default_config.envConfig(language='en',intForcPath= home + 'XC3Dmodel/results/internalForces/',verifPath= home + 'XC3Dmodel/results/verifications/',annexPath= home + 'XC3Dmodel/annex/',grWidth='120mm')
