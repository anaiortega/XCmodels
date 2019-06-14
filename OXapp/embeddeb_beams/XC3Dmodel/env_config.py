# -*- coding: utf-8 -*-
from postprocess.config import default_config

#home= '/home/ana/projects/XCmodels/'
home= '/home/ana/20190610_1416_XC3Dmode/'

# Default configuration of environment variables.
cfg=default_config.envConfig(language='en',intForcPath= home + 'XC3Dmodel/results/internalForces/',verifPath= home + 'XC3Dmodel/results/verifications/',annexPath= home + 'XC3Dmodel/annex/',grWidth='120mm')
