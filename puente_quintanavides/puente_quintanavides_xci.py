# -*- coding: utf-8
# Definición del puente.

'''
execfile('solucion/solucion_xci.py')
execfile('listados/listados_reacciones_xcm.py')
execfile('listados/listados_esfuerzos_xcm.py')
execfile('listados/exporta_esfuerzos_xcm.py')
execfile('listados/listados_desplazamientos_xcm.py')
execfile('latex/supertabular.lcmm')
'''

from __future__ import division
from __future__ import print_function

import math
import xc_base
import geom
import xc
import deck_geometry
from model import predefined_spaces
from postprocess import output_handler
from materials import typical_materials
from materials.ehe import EHE_materials
from actions import load_cases as lcm

FEcase= xc.FEProblem()
FEcase.title= 'Puente Arroyo del Molino'
# Problem type
preprocessor=FEcase.getPreprocessor
nodes= preprocessor.getNodeHandler
modelSpace= deck_geometry.DeckGeometry(nodes) 

xcTotalSet= preprocessor.getSets.getSet('total')

execfile('datos_base_xci.py')

modelSpace.defineTablero()
modelSpace.defineSets()
execfile('modelo/materiales_xci.py')


modelSpace.genMesh()
modelSpace.setConstraints()
LTot= modelSpace.getLTot()
modelSpace.defineSetsPretensado()
modelSpace.mallaTendones(areaCordon)

# Loads
execfile('loads.py')

modelSpace.creaSetsListados()

# Graphic stuff.
oh= output_handler.OutputHandler(modelSpace)
oh.displayBlocks()
oh.displayFEMesh()


