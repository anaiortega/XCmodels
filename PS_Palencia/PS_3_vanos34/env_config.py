# -*- coding: utf-8 -*-
from postprocess.config import default_config
abutment='Y' #if abutment is modelled 'Y'

home= '/home/ana/projects/XCmodels/PS_Palencia/'
path_model_slab_bridge='/home/ana/projects/XCmodels/generic_bridges/model_slab_bridge/'
path_loads_def='/home/ana/projects/XCmodels/generic_bridges/loads_bridge_2_notional_lanes/'
path_gen_results='/home/ana/projects/XCmodels/generic_bridges/gen_results/'
if abutment.lower()[0]=='y':
    path_model_abutment='/home/ana/projects/XCmodels/generic_bridges/model_abutment/'

# Default configuration of environment variables.
cfg=default_config.envConfig(language='en',intForcPath= home + 'PS_3_vanos34/results/internalForces/',verifPath= home + 'PS_3_vanos34/results/verifications/',annexPath= home + 'PS_3_vanos34/annex/',grWidth='120mm')

def redondea(lista,decimales):
    retval=[]
    for i in lista:
        retval.append(round(i,decimales))
    return retval
