# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os

import xc_base
import geom
import xc

from import_export import NeutralMeshDescription


xcImportExportData= NeutralMeshDescription.XCImportExportData()
xcImportExportData.mainDATFile= "MeshPGE.dat"
#xcImportExportData.groupDATFiles= ["AppuiAigleCoteRive.dat", "AppuiAigleCoteTerr.dat", "AppuiAigleLatIntCT.dat", "AppuiAigleLatInt.dat", "AppuiLeysinCoteRive.dat", "AppuiLeysinCT.dat", "AppuiLeysinLatExtCA.dat", "AppuiLeysinLatExtCT.dat", "AppuiLeysinLatInt.dat", "Arc0.dat", "ArcPileAigle.dat", "ArcPileLeysin.dat", "Dalle.dat", "MurAigle.dat", "MurAigleLat.dat", "MurLeysin.dat", "Parapet.dat", "PileAigleCoteTerr.dat", "PileAigleLatIntCT.dat", "PileAigleLatInt.dat", "PileiLeysinLatInt.dat", "PileLeysinCoteTerr.dat", "PileLeysinLatExtCA.dat", "PileLeysinLatExtCT.dat", "PiloAigleCoteRive.dat", "PorteAFaux.dat", "SemelleAigle.dat", "SemelleLeysin.dat", "TympanExt.dat", "TympanInt.dat", "ArcAigle.dat", "ArcLeysin.dat", "DalleAigle.dat", "DalleLeysin.dat", "PileAigleBottom.dat", "PileAigleTop.dat", "PileLeysinBottom.dat", "PileLeysinTop.dat", "PileLeysinCoteRive.dat"]
xcImportExportData.groupDATFiles= ["PileLeysinCoteRive.dat"]
xcImportExportData.cellConversion[204]= "quad4n"
xcImportExportData.cellConversion[203]= "tri31"

xcImportExportData.readDATFiles()


xcImportExportData.problemName= "MeshPGE"
xcImportExportData.xcFileName= "pp.py"
xcImportExportData.writeToXCFile()
  
