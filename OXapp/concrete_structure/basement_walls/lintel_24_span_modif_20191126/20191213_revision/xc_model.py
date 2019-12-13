# -*- coding: utf-8 -*-
import math
import xc_base
import geom
import xc

from model import predefined_spaces
from materials.ehe import EHE_materials

test= xc.FEProblem()
execfile('./xc_model_blocks.py')

xcTotalSet= preprocessor.getSets.getSet('total')

# Problem type
FEcase= xc.FEProblem()
preprocessor=FEcase.getPreprocessor
nodes= preprocessor.getNodeHandler
modelSpace= predefined_spaces.StructuralMechanics3D(nodes) 

# Materials
concrete=EHE_materials.HA30
reinfSteel=EHE_materials.B500S
