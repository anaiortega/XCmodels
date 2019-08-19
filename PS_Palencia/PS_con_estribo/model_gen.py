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

fullProjPath='/home/ana/projects/XCmodels/PS_Palencia/PS_con_estribo/'
execfile(fullProjPath+'env_config.py')

execfile(fullProjPath+'data_deck_piers.py')
if abutment.lower()[0]=='y':
    execfile(fullProjPath+'data_abutment.py')
execfile(path_model_slab_bridge+'model_gen.py')

if abutment.lower()[0]=='y':
    execfile(path_model_abutment+'model_gen_abutment.py')
#Definition of sets
execfile(fullProjPath+'sets_def.py')

#                       ***BOUNDARY CONDITIONS***
execfile(fullProjPath+'bound_cond.py')
        
#                       ***ACTIONS***
execfile(path_loads_def+'loads_def.py')                           

setsTablPilas=[riostrEstr1,riostrEstr2,losa,cartabInt,cartabExt,voladzInt,voladzExt,pilasBarlov]
if abutment.lower()[0]=='y':
    allsets=setsTablPilas+setsEstribo
else:
    allsets=setsTablPilas
    
if pilasSotav:
    allsets.append(pilasSotav)
for s in allsets:
    s.fillDownwards()
    
overallSet=prep.getSets.defSet('overallSet')
sets.append_sets(overallSet,allsets)
overallSet.description='overall set'
