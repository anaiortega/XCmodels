

execfile('../model_gen.py') #FE model generation

print 'number of points: ', preprocessor.getMultiBlockTopology.getPoints.size
print 'number of column lines: ', columns.getLines.size
print 'number of beam lines: ', beams.getLines.size
print 'number of beam elements: ', beams.getElements.size

attachedBeamLines.fillDownwards()
attachedBeamLines.description='attached beam lines'
attachedBeamLines.color=cfg.colors['green01']

for l in attachedBeamLines.getLines:
    print 'length: ', l.getLength(), ' first node, tag: ', l.firstNode.tag, ' number of connected elements: ', l.firstNode.getNumberOfConnectedElements(), ' number of connected constraints: ', l.firstNode.getNumberOfConnectedConstraints(), 'last node tag: ', l.lastNode.tag, ' number of connected elements: ', l.lastNode.getNumberOfConnectedElements(), ' number of connected constraints: ', l.firstNode.getNumberOfConnectedConstraints()


from postprocess.xcVtk.CAD_model import vtk_CAD_graphic
defDisplay= vtk_CAD_graphic.RecordDefDisplayCAD()
setToDisplay= attachedBeamLines+columns #beams+columns # columns # beams, slabs_H, slabs_L, stag2Set
defDisplay.displayBlocks(xcSet= setToDisplay,fName= None,caption= 'Model grid')



