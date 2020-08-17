# -*- coding: utf-8
# Definición del puente.

'''
execfile('modelo/puntos_xcm.py')
execfile('modelo/fija_nodo_6gdl_xcm.py')
execfile('modelo/rigid_beam_xcm.py')
execfile('modelo/cargas_elem_xcm.py')
execfile('modelo/cargas_nodo_xcm.py')
execfile('vtk/displayVtk.lcmm')
execfile('vtk/malla_cad/vtk_define_malla_cad_xcm.py')
execfile('vtk/malla_ef/vtk_define_malla_elementos_xcm.py')
execfile('vtk/vtk_cargas_xcm.py')
execfile('vtk/utilsVtk.lcmm')
execfile('solucion/solucion_xci.py')
execfile('materiales/ehe/auxEHE_xcm.py')
execfile('materiales/ehe/relajacion_acero_xcm.py')
execfile('materiales/ehe/retraccion_fluencia_xcm.py')
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

from model import predefined_spaces

FEcase= xc.FEProblem()
FEcase.title= 'Puente Arroyo del Molino'
# Problem type
preprocessor=FEcase.getPreprocessor
nodes= preprocessor.getNodeHandler
modelSpace= predefined_spaces.StructuralMechanics3D(nodes) 

xcTotalSet= preprocessor.getSets.getSet('total')

execfile('datos_base_xci.py')


execfile('modelo/geom_tablero_xci.py')
execfile('modelo/sets_tablero_xci.py')
execfile('modelo/materiales_xci.py')
execfile('modelo/genera_malla_viga_xci.py')
execfile('modelo/conds_contorno_xci.py')
LTot= (LTramo0+LTramo1+LTramo2)*2.0+LTramo3
execfile('modelo/sets_pretensado_xci.py')
execfile('modelo/genera_malla_tendones_xci.py')
execfile('acciones/define_casos_carga_xci.py')
execfile('acciones/parametros_carga_xci.py')
execfile('acciones/carga_viga_xci.py')
execfile('modelo/genera_malla_losa_sup_xci.py')
execfile('acciones/sets_def_cargas_xci.py')
execfile('acciones/cargas_puente_xci.py')
execfile('modelo/sets_listados_xci.py')


