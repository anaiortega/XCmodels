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


gilamontDock= xc.FEProblem()
execfile('./xc_model_blocks.py')
xcTotalSet= preprocessor.getSets.getSet('total')
