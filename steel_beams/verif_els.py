# -*- coding: utf-8 -*-

execfile('model_data.py')
from postprocess import recorders

#Assigns span value to allow deflection verification.
span= 15.697
for n in setTotal.nodes:
  n.setProp('span',span)
recorder= recorders.installNodeDisplacementRecorder("node_prop_recorder",setTotal.nodes)

def resultComb(prb,nmbComb):
  preprocessor.resetLoadCase()
  preprocessor.getLoadHandler.getLoadCombinations.addToDomain(nmbComb)
  #Solución
  solution= predefined_solutions.SolutionProcedure()
  analysis= solution.simpleStaticLinear(prb)
  result= analysis.analyze(1)
  preprocessor.getLoadHandler.getLoadCombinations.removeFromDomain(nmbComb)

combContainer.dumpCombinations(preprocessor)
resultComb(mainBeam,'ELS00')
#resultComb(mainBeam,'ELS01')

dispMax= -1
combDispMax= ""
fmax= 0
for n in setTotal.nodes:
  dm= n.getProp("dispMax")
  f= dm/n.getProp('span')
  n.setProp('f',f)
  if(dispMax<dm):
    x= n.getCoo[0]
    dispMax= dm
    fmax= dispMax/n.getProp('span')
    combDispMax= n.getProp("CombDispMax")
  #print "tag= ", n.tag, " CombVMax= ", n.getProp("CombVMax"), " VMax= ", n.getProp("VMax"), " CombVMin= ", n.getProp("CombVMin"),  " VMin= ", n.getProp("VMin")

print 'x= ', x, 'disMax=', dispMax*1000, 'mm', 'combDispMax=', combDispMax, 'f= L/', 1.0/fmax

import vtk
from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import vtk_FE_graphic
from postprocess.xcVtk import node_property_diagram as npd

defGrid= vtk_graphic_base.RecordDefGrid()
defGrid.nmbSet= "total"

diagram= npd.NodePropertyDiagram(-0.1,1e3,[setTotal],"dispMax")
#diagram= npd.NodePropertyDiagram(1000,1,[setTotal],"f")
#diagram= npd.NodePropertyDiagram(-0.02,1e-3,[total],"Qy")
diagram.addDiagram()

defDisplay= vtk_FE_graphic.RecordDefDisplayEF()
defDisplay.cameraParameters= vtk_graphic_base.CameraParameters('YPos')
defDisplay.setupGrid(preprocessor.getSets.getSet('total'))
defDisplay.defineMeshScene(None)
defDisplay.appendDiagram(diagram) #Append diagram to the scene.

# execfile('draw_supports.py')
# defDisplay.renderer.AddActor(supportsActor)

defDisplay.displayScene()
