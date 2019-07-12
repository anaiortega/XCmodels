# -*- coding: utf-8 -*-

import math
import vtk
import xc_base
import geom
import xc
from solution import predefined_solutions
from model import predefined_spaces
from materials import typical_materials
from materials.ec3 import EC3_materials

from materials.sections import structural_steel as steel
from actions import load_cases as lcm
from actions import combinations as combs


# Problem type
mainBeam= xc.FEProblem()
mainBeam.title= 'Warehouse main beams'
preprocessor= mainBeam.getPreprocessor   
nodos= preprocessor.getNodeHandler
modelSpace= predefined_spaces.StructuralMechanics2D(nodos)
