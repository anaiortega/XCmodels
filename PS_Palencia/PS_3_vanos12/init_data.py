# -*- coding: utf-8 -*-

fullProjPath='/home/ana/projects/XCmodels/PS_Palencia/PS_3_vanos12/'

abutment='Y' #if abutment is modelled 'Y'
pile_found='Y'

path_model_slab_bridge='/home/ana/projects/XCmodels/generic_bridges/model_slab_bridge/'
path_loads_def='/home/ana/projects/XCmodels/generic_bridges/loads_bridge_2_notional_lanes/'
path_gen_results='/home/ana/projects/XCmodels/generic_bridges/gen_results/'
if abutment.lower()[0]=='y':
    path_model_abutment='/home/ana/projects/XCmodels/generic_bridges/model_abutment/'
    path_loads_abutment='/home/ana/projects/XCmodels/generic_bridges/loads_abutment/'
if pile_found.lower()[0]=='y':
     path_foundation='/home/ana/projects/XCmodels/generic_bridges/model_foundation/'

def redondea(lista,decimales):
    retval=[]
    for i in lista:
        retval.append(round(i,decimales))
    return retval
