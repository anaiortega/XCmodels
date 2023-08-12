# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function

from materials.astm_aisc import ASTM_materials


# Bolted plate
boltArray= ASTM_materials.BoltArray(bolt, nRows= nbolt_rows, nCols= nbolt_columns)
boltedPlate= ASTM_materials.BoltedPlate(boltArray, thickness= bltPlate_thck, steelType= bltPlate_steel, doublePlate= bltPlate_double)
