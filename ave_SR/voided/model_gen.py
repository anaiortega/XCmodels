# -*- coding: utf-8 -*-
from __future__ import division
from postprocess.config import default_config

import os
import xc_base
import geom
import xc
import math

workingDirectory= default_config.findWorkingDirectory()+'/'
execfile(workingDirectory+'env_config.py')

execfile(workingDirectory+'basic_data.py')
execfile(workingDirectory+'basic_geom.py')
execfile(workingDirectory+'../../generic_bridges/voided_slab_bridge/model_gen.py')
execfile(workingDirectory+'../../generic_bridges/model_piers/model_gen.py')
execfile(workingDirectory+'sets_def.py')
if pile_found.lower()[0]=='y':
    execfile('../data_foundation.py')

#                       ***BOUNDARY CONDITIONS***
execfile(workingDirectory+'bound_cond.py')
