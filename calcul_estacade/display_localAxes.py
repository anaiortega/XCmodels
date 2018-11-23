# -*- coding: utf-8 -*-

execfile('./model_data.py')
execfile('./captionTexts.py')

from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import vtk_FE_graphic
from postprocess.xcVtk import local_axes_vector_field as lavf
import vtk

def display_local_axes(setToDisplay=None,vectorScale=1.0,viewDef= vtk_graphic_base.CameraParameters('XYZPos'),caption= '',fileName=None):
    '''vector field display of the loads applied to the chosen set of elements in the load case passed as parameter
    
    :param setToDisplay:   set of elements to be displayed (defaults to total set)
    :param vectorScale:    factor to apply to the vectors length in the representation
    :param viewDef:        camera parameters.
    :param fileName:       full name of the graphic file to generate. Defaults to `None`, in this case it returns a console output graphic.
    :param caption:        text to display in the graphic 
    '''
    defDisplay= vtk_FE_graphic.RecordDefDisplayEF()
    defDisplay.setupGrid(setToDisplay)
    vField=lavf.LocalAxesVectorField(setToDisplay.name+'_localAxes',vectorScale)
    vField.dumpLocalAxes(setToDisplay)
    defDisplay.viewDef= viewDef
    defDisplay.defineMeshScene(None) 
    vField.addToDisplay(defDisplay)
    defDisplay.displayScene(caption,fileName)
    return defDisplay

display_local_axes(setToDisplay=setParapet,vectorScale=0.3,viewDef= vtk_graphic_base.CameraParameters('XYZPos',2.0),caption= setParapet.genDescr.capitalize() + ', '+ capTexts['LocalAxes'],fileName=None)
#display_local_axes(setToDisplay=beamsSet,vectorScale=0.3,vtk_graphic_base.CameraParameters('XYZPos'),caption=deckSet.genDescr.capitalize() + ', '+ capTexts['LocalAxes'],fileName=None)


