# -*- coding: utf-8 -*-
from postprocess.config import default_config

#home= '/home/ana/projects/XCmodels/'
#home= '/home/ana/projects/XCmodels/OXapp/embedded_beams/'
home= '/home/ana/projects/XCmodels/OXapp/embedded_beams/'

# Default configuration of environment variables.
cfg=default_config.envConfig(language='en',intForcPath= home + 'XC3Dmodel_updated_loads/results/internalForces/',verifPath= home + 'XC3Dmodel_updated_loads/results/verifications/',annexPath= home + 'XC3Dmodel_updated_loads/annex/',grWidth='\linewidth')
