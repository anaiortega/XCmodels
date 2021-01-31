exec(open('fe_model.py').read()))
exec(open('loadStateData.py').read()))

#Graphic output
from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import vtk_FE_graphic
from postprocess.xcVtk import vtk_internal_force_diagram as gde
from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import quick_graphics as qg

lcs= qg.QuickGraphics(deck)
 
#Define the diagram to display:
# scaleFactor, unitConversionFactor, element sets and magnitude to display.
loadCaseToDisplay= ELUT41 #AT202 #ELUT202 #G1
#lcs.displayNodeValueDiagram('uY',setToDisplay= bridgeSectionSet,fConvUnits=1e3,scaleFactor=-0.05,viewDef= vtk_graphic_base.CameraParameters('ZPos'))
lcs.solve(loadCaseName=loadCaseToDisplay.loadCaseName,loadCaseExpr=loadCaseToDisplay.loadCaseExpr)
#lcs.displayIntForcDiag('N',deckSet,1e-3,0.01,'(kN)',vtk_graphic_base.CameraParameters('ZPos'))
lcs.displayIntForcDiag('Mz',deckSet,1e-3,-1.0,'(kN m)',vtk_graphic_base.CameraParameters('ZPos'))
#lcs.displayIntForcDiag('Qy',deckSet,1e-3,-0.05,'(kN)',vtk_graphic_base.CameraParameters('ZPos'))
