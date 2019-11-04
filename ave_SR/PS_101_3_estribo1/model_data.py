# -*- coding: utf-8 -*-

import os
import xc_base
import geom
import xc
import math

workingDirectory= default_config.findWorkingDirectory()+'/'
execfile(workingDirectory+'env_config.py')

execfile('../basic_data.py')
execfile('../basic_geom.py')
execfile('../../PSs_estribos/model_constr.py')
