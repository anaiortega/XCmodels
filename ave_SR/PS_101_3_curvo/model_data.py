# -*- coding: utf-8 -*-
from __future__ import division

import os
import geom
import xc
import math
from model import predefined_spaces
from model.geometry import grid_model as gm


workingDirectory= default_config.findWorkingDirectory()+'/'
exec(open(workingDirectory+'env_config.py').read())

exec(open('../basic_data.py').read())
exec(open('../basic_geom.py').read())
exec(open('../../PSs/model_constr.py').read())
