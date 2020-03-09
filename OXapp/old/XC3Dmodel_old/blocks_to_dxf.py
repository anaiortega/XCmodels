
from import_export import block_topology_entities as bte

execfile('model_gen.py') #FE model generation

columns.name= 'columns'
bdColumns= bte.BlockData()
bdColumns.readFromXCSet(columns)
bdColumns.writeDxfFile('columns.dxf')

beams.name= 'beams'
bdBeams= bte.BlockData()
bdBeams.readFromXCSet(beams)
bdBeams.writeDxfFile('beams.dxf')

slabs.name= 'slabs'
bdSlabs= bte.BlockData()
bdSlabs.readFromXCSet(slabs)
bdSlabs.writeDxfFile('slabs.dxf')

