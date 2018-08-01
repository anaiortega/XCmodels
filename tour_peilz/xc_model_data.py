# -*- coding: utf-8 -*-
import math
import xc_base
import geom
import xc
from postprocess import utils_display

#Material definition
from materials import typical_materials
from materials.sia262 import SIA262_materials
from materials.sections import section_properties

#Parts definition
import re

#Mesh definition
from model import predefined_spaces

#Loads
from actions import load_cases as lcm
from actions import combinations as combs

#Solution
from solution import predefined_solutions


tourRamps= xc.FEProblem()
execfile('./xc_model_blocks.py')
xcTotalSet= preprocessor.getSets.getSet('total')

dxfLayerNames= ['roof_01', 'floor_a_middle', 'bulkhead_03', 'middle', 'parapets_01', 'bulkhead_01', 'floor_stairs', 'floor_middle_b', 'side_b', 'side_b_stairs', 'side_a', 'side_a_stairs']

layerSets= {}
for layerName in dxfLayerNames:
    layerSets[layerName]= preprocessor.getSets.defSet(layerName)

for s in xcTotalSet.getSurfaces:
    layerName= s.getProp('labels')[0]
    layerSet= layerSets[layerName]
    layerSet.getSurfaces.append(s)

for key in layerSets:
    layerSets[key].fillDownwards()
    


