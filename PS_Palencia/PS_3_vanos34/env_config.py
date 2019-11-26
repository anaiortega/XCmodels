# -*- coding: utf-8 -*-
from postprocess.config import default_config

workingDirectory=default_config.findWorkingDirectory()+'/'

abutment='Y' #if abutment is modelled 'Y'
pile_found='Y'

path_model_slab_bridge=workingDirectory + '../../generic_bridges/model_slab_bridge/'
path_model_piers=workingDirectory + '../../generic_bridges/model_piers/'
path_loads_def=workingDirectory + '../../generic_bridges/loads_bridge_2_notional_lanes/'
path_gen_results=workingDirectory + '../../generic_bridges/gen_results/'
if abutment.lower()[0]=='y':
    path_model_abutment=workingDirectory + '../../generic_bridges/model_abutment/'
    path_loads_abutment=workingDirectory + '../../generic_bridges/loads_abutment/'
if pile_found.lower()[0]=='y':
     path_foundation=workingDirectory + '../../generic_bridges/model_foundation/'

