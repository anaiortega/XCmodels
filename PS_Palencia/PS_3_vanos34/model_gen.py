# -*- coding: utf-8 -*-
from __future__ import division

import os
import xc_base
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
from model.geometry import geom_utils as gut
from materials.ehe import EHE_materials
#

fullProjPath='/home/ana/projects/XCmodels/PS_Palencia/PS_3_vanos34/'
execfile(fullProjPath+'env_config.py')

execfile(fullProjPath+'data.py')
#                       ****MODEL***
execfile(path_model_slab_bridge+'model_gen.py')
#Definition of sets
execfile(fullProjPath+'sets_def.py')
#                       ***BOUNDARY CONDITIONS***
execfile(fullProjPath+'bound_cond.py')
#                       ***ACTIONS***
execfile(path_loads_def+'loads_def.py')                           


allsets=[riostrEstr1,riostrEstr2,losa,cartabInt,cartabExt,voladzInt,voladzExt,pilasBarlov]
if pilasSotav:
    allsets.append(pilasSotav)
for s in allsets:
    s.fillDownwards()
    
overallSet=prep.getSets.getSet("total")
overallSet.fillDownwards()
