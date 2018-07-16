# -*- coding: utf-8 -*-

execfile('./model_data.py')
execfile('./captionTexts.py')

from postprocess.xcVtk import vtk_grafico_base
from postprocess.xcVtk.FE_model import vtk_FE_graphic
from postprocess.xcVtk import local_axes_vector_field as lavf
import vtk

def displayLocalAxes(setToDisplay=None,vectorScale=1.0,viewNm="XYZPos",hCamFct=1.0,caption= '',fileName=None):
    '''vector field display of the loads applied to the chosen set of elements in the load case passed as parameter
    
    :param setToDisplay:   set of elements to be displayed (defaults to total set)
    :param vectorScale:    factor to apply to the vectors length in the representation
    :param viewNm:         name of the view  that contains the renderer (possible options: "XYZPos", "XPos", "XNeg","YPos", "YNeg", "ZPos", "ZNeg")
    :param hCamFct:     factor that applies to the height of the camera position in order to
                        change perspective of isometric views (defaults to 1). Usual values 0.1 to 10
    :param fileName:       full name of the graphic file to generate. Defaults to `None`, in this case it returns a console output graphic.
    :param caption:        text to display in the graphic 
    '''
    defDisplay= vtk_FE_graphic.RecordDefDisplayEF()
    defDisplay.setupGrid(setToDisplay)
    vField=lavf.LocalAxesVectorField(setToDisplay.name+'_localAxes',vectorScale)
    vField.dumpLocalAxes(setToDisplay)
    defDisplay.viewName= viewNm
    defDisplay.hCamFct=hCamFct
    defDisplay.defineMeshScene(None) 
    vField.addToDisplay(defDisplay)
    defDisplay.displayScene(caption,fileName)
    return defDisplay

displayLocalAxes(setToDisplay=setParapet,vectorScale=0.3,viewNm="XYZPos",hCamFct=2.0,caption= setParapet.genDescr.capitalize() + ', '+ capTexts['LocalAxes'],fileName=None)
#displayLocalAxes(setToDisplay=beamsSet,vectorScale=0.3,viewNm="XYZPos",hCamFct=1.0,caption=deckSet.genDescr.capitalize() + ', '+ capTexts['LocalAxes'],fileName=None)


