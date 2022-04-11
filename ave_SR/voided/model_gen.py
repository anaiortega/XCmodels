# -*- coding: utf-8 -*-
from __future__ import division
from postprocess.config import default_config

import os
import geom
import xc
import math
from postprocess import output_styles as outSty
from postprocess import output_handler as outHndl

workingDirectory= default_config.findWorkingDirectory()+'/'
exec(open(workingDirectory+'env_config.py').read())

exec(open(workingDirectory+'basic_data.py').read())
exec(open(workingDirectory+'basic_geom.py').read())
if abutment.lower()[0]=='y':
    exec(open(workingDirectory+'data_abutment.py').read())
exec(open(workingDirectory+'../../generic_bridges/voided_slab_bridge/model_gen.py').read())
exec(open(workingDirectory+'../../generic_bridges/model_piers/model_gen.py').read())
if abutment.lower()[0]=='y':
    exec(open(path_model_abutment+'model_gen_abutment.py').read())
#Definition of sets
exec(open(workingDirectory+'sets_def.py').read())
if pile_found.lower()[0]=='y':
    exec(open(workingDirectory+'data_foundation.py').read())

#                       ***BOUNDARY CONDITIONS***
exec(open(workingDirectory+'bound_cond.py').read())
#                       ***ACTIONS***
exec(open(path_loads_def+'loads_def.py').read())                           
exec(open(path_loads_def+'loads_def_thermal_gradient_voided.py').read())                           
