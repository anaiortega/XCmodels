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

workingDirectory= default_config.findWorkingDirectory()+'/'
exec(open(workingDirectory+'init_data.py').read())

exec(open(workingDirectory+'data_deck_piers.py').read())
if abutment.lower()[0]=='y':
    exec(open(workingDirectory+'data_abutment.py').read())
exec(open(path_model_slab_bridge+'model_gen.py').read())

if abutment.lower()[0]=='y':
    exec(open(path_model_abutment+'model_gen_abutment.py').read())
#Definition of sets
exec(open(workingDirectory+'sets_def.py').read())

if pile_found.lower()[0]=='y':
    exec(open('../data_foundation.py').read())
#                       ***BOUNDARY CONDITIONS***
exec(open(workingDirectory+'bound_cond.py').read())
        
#                       ***ACTIONS***
exec(open(path_loads_def+'loads_def.py').read())                           
exec(open(path_loads_def+'loads_def_thermal_gradient_slab.py').read())                           
if abutment.lower()[0]=='y':
    exec(open(path_loads_abutment+'loads_def.py').read())

setsTablPilas=[riostrEstr1,riostrEstr2,losa,cartabInt,cartabExt,voladzInt,voladzExt,pilasBarlov]
if abutment.lower()[0]=='y':
    allsets=setsTablPilas+setsEstribo
else:
    allsets=setsTablPilas
    
if pilasSotav:
    allsets.append(pilasSotav)
for s in allsets:
    s.fillDownwards()
if pile_found.lower()[0]=='y':
    allsets.append(ties)
    allsets.append(struts)
    allsets.append(piles)
    
overallSet=prep.getSets.defSet('overallSet')
sets.append_sets(overallSet,allsets)
overallSet.description='overall set'
