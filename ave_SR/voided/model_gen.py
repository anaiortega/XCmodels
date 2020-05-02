# -*- coding: utf-8 -*-
from __future__ import division
from postprocess.config import default_config

import os
import xc_base
import geom
import xc
import math
from postprocess import output_styles as outSty
from postprocess import output_handler as outHndl

workingDirectory= default_config.findWorkingDirectory()+'/'
execfile(workingDirectory+'env_config.py')

execfile(workingDirectory+'basic_data.py')
execfile(workingDirectory+'basic_geom.py')
if abutment.lower()[0]=='y':
    execfile(workingDirectory+'data_abutment.py')
execfile(workingDirectory+'../../generic_bridges/voided_slab_bridge/model_gen.py')
execfile(workingDirectory+'../../generic_bridges/model_piers/model_gen.py')
if abutment.lower()[0]=='y':
    execfile(path_model_abutment+'model_gen_abutment.py')
#Definition of sets
execfile(workingDirectory+'sets_def.py')
if pile_found.lower()[0]=='y':
    execfile(workingDirectory+'data_foundation.py')

#                       ***BOUNDARY CONDITIONS***
execfile(workingDirectory+'bound_cond.py')
#                       ***ACTIONS***
execfile(path_loads_def+'loads_def.py')                           
execfile(path_loads_def+'loads_def_thermal_gradient_voided.py')                           
