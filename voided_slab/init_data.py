# -*- coding: utf-8 -*-
workingDirectory= default_config.findWorkingDirectory()+'/'

abutment='N' #if abutment is modelled 'Y'
pile_found='N'

print('we need to get rid of this kind of local setup.')
path_model_slab_bridge='/home/ana/projects/XCmodels/generic_bridges/model_slab_bridge/'
path_loads_def='/home/ana/projects/XCmodels/generic_bridges/loads_bridge_2_notional_lanes/'
path_gen_results='/home/ana/projects/XCmodels/generic_bridges/gen_results/'
if abutment.lower()[0]=='y':
    path_model_abutment='/home/ana/projects/XCmodels/generic_bridges/model_abutment/'
    path_loads_abutment='/home/ana/projects/XCmodels/generic_bridges/loads_abutment/'
if pile_found.lower()[0]=='y':
     path_foundation='/home/ana/projects/XCmodels/generic_bridges/model_foundation/'

