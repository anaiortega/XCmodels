# -*- coding: utf-8 -*-
from __future__ import division

execfile("model_data.py")

from import_export.sciaXML.scia_loads import LoadContainer as lc
from import_export.sciaXML import sXMLMesh as sxml
from import_export.sciaXML import sXMLBlockTopology as sxmlBlocks
from import_export import MeshEntities as me
from import_export import BlockTopologyEntities as bte
from import_export import NeutralMeshDescription as nmd
from import_export import NeutralLoadDescription as nld

preprocessor= FEcase.getPreprocessor
total= preprocessor.getSets.getSet("total")
shellElements= preprocessor.getSets.defSet("shellElements")
for e in total.elements:
  dim= e.getDimension
  if(dim==2): #shell element
    shellElements.elements.append(e)
shellElements.fillDownwards()

beton= me.MaterialRecord('béton','C35/45',1e-5,2500,EcDeck,cpoish,EcDeck/(2*(1+cpoish)),1e-3,0.0,0.0)

#Finite element mesh.
mesh= me.MeshData()
mesh.name= 'PI67'
mesh.materials.append(beton)
mesh.readFromXCSet(shellElements)

permanentLoadCaseNames= ['G']
loadContainer= lc.LoadContainer()
loadContainer.readFromXC(preprocessor,permanentLoadCaseNames,combContainer)

outputPath= './xml_scia/'

xmlMesh= sxml.SXMLMesh("http://www.scia.cz", mesh,loadContainer)
xmlMesh.writeXMLFile(outputPath)
xmlMesh.indent()

#Block topology
blocks= bte.BlockData()
blocks.name= 'PI67_blocks'
blocks.materials.append(beton)
blocks.readFromXCSet(total)

freeLoadContainer= lc.FreeLoadContainer()
freeLoadContainer.readFromXC(preprocessor,permanentLoadCaseNames,combContainer)

xmlBlocks= sxmlBlocks.SXMLBlockTopology("http://www.scia.cz", blocks,freeLoadContainer)
xmlBlocks.writeXMLFile(outputPath)
xmlBlocks.indent()
