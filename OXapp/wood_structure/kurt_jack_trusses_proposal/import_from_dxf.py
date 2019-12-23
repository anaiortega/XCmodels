# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function

from import_export import DxfReader
from import_export import NeutralMeshDescription as nmd

layerNamesToImport= ['xc_*']

def getRelativeCoo(pt):
  return [pt[0],pt[1],pt[2]] #No modification.

fileName= 'model.dxf'
dxfImport= DxfReader.DXFImport(fileName, layerNamesToImport,getRelativeCoo, importLines= True, polylinesAsSurfaces= False, threshold= 0.001, tolerance= .001)

#Block topology
blocks= dxfImport.exportBlockTopology('test')

fileName= 'xc_model_blocks'
ieData= nmd.XCImportExportData()
ieData.outputFileName= fileName
ieData.problemName= 'FEcase'
ieData.blockData= blocks

ieData.writeToXCFile()
