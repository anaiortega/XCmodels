# -*- coding: utf-8 -*-
from postprocess.config import default_config

#home= '/home/ana/projects/XCmodels/'
#home= '/home/ana/projects/XCmodels/OXapp/embedded_beams/'
#home= '/home/ana/projects/XCmodels/OXapp/embedded_beams/'
home= '/home/luis/Documents/XCmodels/OXapp/embedded_beams/'

# Default configuration of environment variables.
cfg=default_config.envConfig(language='en',intForcPath= home + 'model_precast_layout/results/internalForces/',verifPath= home + 'model_precast_layout/results/verifications/',annexPath= home + 'model_precast_layout/annex/',grWidth='\linewidth')
