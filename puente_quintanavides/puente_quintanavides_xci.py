# -*- coding: utf-8
# Definición del puente.

'''
exec(open('solucion/solucion_xci.py').read())
exec(open('listados/listados_reacciones_xcm.py').read())
exec(open('listados/listados_esfuerzos_xcm.py').read())
exec(open('listados/exporta_esfuerzos_xcm.py').read())
exec(open('listados/listados_desplazamientos_xcm.py').read())
exec(open('latex/supertabular.lcmm').read())
'''

from __future__ import division
from __future__ import print_function

import math
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

exec(open('datos_base_xci.py').read())

modelSpace.defineTablero()
modelSpace.defineSets()
exec(open('modelo/materiales_xci.py').read())


modelSpace.genMesh()
modelSpace.setConstraints()
LTot= modelSpace.getLTot()
modelSpace.defineSetsPretensado()
modelSpace.mallaTendones(areaCordon)

# Loads
exec(open('loads.py').read())

modelSpace.creaSetsListados()

# Graphic stuff.
oh= output_handler.OutputHandler(modelSpace)
oh.displayBlocks()
oh.displayFEMesh()


