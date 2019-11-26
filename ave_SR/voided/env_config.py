# -*- coding: utf-8 -*-
from postprocess.config import default_config
workingDirectory=default_config.findWorkingDirectory()+'/'

abutment='Y' #if abutment is modelled 'Y'
pile_found='Y'

# Default configuration of environment variables.
cfg=default_config.EnvConfig(language='sp',intForcPath= 'results/internalForces/',verifPath= 'results/verifications/',annexPath= 'annex/',grWidth='120mm')
path_loads_def=workingDirectory + '../../generic_bridges/loads_bridge_2_notional_lanes/'
if abutment.lower()[0]=='y':
    path_model_abutment=workingDirectory + '../../generic_bridges/model_abutment/'
    path_loads_abutment=workingDirectory + '../../generic_bridges/loads_abutment/'
if pile_found.lower()[0]=='y':
     path_foundation=workingDirectory + '../../generic_bridges/model_foundation/'
