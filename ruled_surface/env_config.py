# -*- coding: utf-8 -*-
from postprocess.config import default_config

#home= '/home/ana/projects/XCmodels/'
home= '/home/ana/projects/XCmodels/'

# Default configuration of environment variables.
cfg=default_config.envConfig(language='en',intForcPath= home + 'ruled_surface/results/internalForces/',verifPath= home + 'ruled_surface/results/verifications/',annexPath= home + 'ruled_surface/annex/',grWidth='120mm')
