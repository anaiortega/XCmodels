# -*- coding: utf-8 -*-

import os
import geom
import xc
import math
from model import predefined_spaces
from model.geometry import grid_model as gm
from model.mesh import finit_el_model as fem
from model.boundary_cond import spring_bound_cond as sprbc
from model.sets import sets_mng as sets
from materials import typical_materials as tm
from actions import loads
from actions import load_cases as lcases
from actions import combinations as cc
from actions.earth_pressure import earth_pressure as ep
from materials.ehe import EHE_materials
from model.geometry import geom_utils as gut
from postprocess.config import colors
from postprocess.config import sp_captions as cpt

exec(open('../basic_data.py').read())
exec(open('../basic_geom.py').read())
exec(open('../../model_constr.py').read())
