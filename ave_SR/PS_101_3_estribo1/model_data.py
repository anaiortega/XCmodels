# -*- coding: utf-8 -*-

import os
import geom
import xc
import math

workingDirectory= default_config.findWorkingDirectory()+'/'
exec(open(workingDirectory+'env_config.py').read())

exec(open('../basic_data.py').read())
exec(open('../basic_geom.py').read())
exec(open('../../PSs_estribos/model_constr.py').read())
