# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function

from import_export import DxfReader
from import_export import NeutralMeshDescription as nmd

layerNamesToImport= ['Mur.*']

def getRelativeCoo(pt):
  return [pt[0],pt[1],pt[2]] #No modification.

dxfImport= DxfReader.DXFImport("dxf_model.dxf",layerNamesToImport,getRelativeCoo, threshold= 0.1,importLines= False, tolerance= .25)

#Block topology
blocks= dxfImport.exportBlockTopology('test')

fileName= 'xc_model_blocks'
ieData= nmd.XCImportExportData()
ieData.outputFileName= fileName
ieData.problemName= 'test'
ieData.blockData= blocks

ieData.writeToXCFile()
