# -*- coding: utf-8 -*-

import geom
import xc
from import_export import neutral_mesh_description as nm
    


prueba= xc.FEProblem()
preprocessor=  prueba.getPreprocessor

xcImportExportData= nm.XCImportExportData()

xcImportExportData.problemName= "mainBeams"
xcImportExportData.dxfLayers= ['model']
xcImportExportData.readDxfFile('model.dxf',preprocessor)
xcImportExportData.xcFileName= 'modele_bielles_tirants_lp.py'
xcImportExportData.writeToXCFile()


