# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function

import xc_base
import geom
import xc
from model import predefined_spaces
from solution import predefined_solutions
from materials.awc_nds import AWCNDS_materials as mat
from materials.awc_nds import dimensional_lumber
from materials import typical_materials
from materials.sections import section_properties
import plates_model
import check

inchToMeter= 0.0254
psiToPa= 6894.76

# Problem type
doublePlate= xc.FEProblem()
doublePlate.title= 'Sheating design'
preprocessor= doublePlate.getPreprocessor   
nodes= preprocessor.getNodeHandler
modelSpace= predefined_spaces.StructuralMechanics2D(nodes)

studSpacing= 12*inchToMeter
trussSpacing= 12*inchToMeter

# Materials
# Spruce-pine-fir No. 2 
wood= dimensional_lumber.SprucePineFirWood(grade= 'no_2')
#wood= dimensional_lumber.SprucePineFirWood(grade= 'stud')
xc_material= wood.defXCMaterial()
plateSection= mat.DimensionLumber(name= '2x6',b= 5.5*inchToMeter, h= 1.5*inchToMeter, woodMaterial= wood)

# Create model
trussLoad= 25.9e3 # truss_AB_reactions.ods
infSet, supSet, supportedNodes= plates_model.genMesh(modelSpace, plateSection, studSpacing, trussSpacing, trussLoad)

# We add the load case to domain.
preprocessor.getLoadHandler.getLoadPatterns.addToDomain("totalLoad")

# Solution
# Linear static analysis.
analisis= predefined_solutions.simple_static_linear(doublePlate)
result= analisis.analyze(1)

# Checking
check.checkPlates(studSpacing, plateSection, infSet, supSet, supportedNodes)
