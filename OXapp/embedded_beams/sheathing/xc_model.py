# -*- coding: utf-8 -*-

import xc_base
import geom
import xc
from solution import predefined_solutions

# Problem type
sheathinginBeam= xc.FEProblem()
sheatingBeam.title= 'Sheating design'
preprocessor= sheatingBeam.getPreprocessor   
nodes= preprocessor.getNodeHandler
modelSpace= predefined_spaces.StructuralMechanics2D(nodos)
