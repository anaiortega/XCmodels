# -*- coding: utf-8 -*-

exec(open('../model_data.py').read()))
from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import vtk_FE_graphic
from postprocess.xcVtk.fields import load_vector_field as lvf
import vtk

    # displayLoad: vector field display of the loads applied to the chosen 
    # set of elements in the load case passed as parameter
    # Parameters:
    #   setToDisplay:   name of the set of elements to be displayed
    #                   (defaults to 'total')
    #   loadCaseNm:     name of the load case to be depicted (defaults to '')
    #   unitsScale:     factor to apply to the results if we want to change
    #                   the units (defaults to 1).
    #   vectorScale:    factor to apply to the vectors length in the 
    #                   representation (defaults to 1).
    #   multByElemArea: boolean value that must be True if we want to 
    #                   represent the total load on each element 
    #                   (=load multiplied by element area) and False if we 
    #                   are going to depict the value of the uniform load 
    #                   per unit area (defaults to False)
    #    viewDef:        camera parameters (position, orientation,...)
    #                   options: "XYZPos", "XPos", "XNeg","YPos", "YNeg",
    #                   "ZPos", "ZNeg") (defaults to "XYZPos")
    #   fileName:       full name of the graphic file to generate. Defaults to 
    #                   None, in this case it returns a console output graphic.
 
model.displayLoad(setToDisplay=None,loadCaseNm='GselfWeight',unitsScale=1e-3,vectorScale=0.1, multByElemArea=False,viewDef= vtk_graphic_base.CameraParameters('XYZPos'),caption= 'G1: Self weigth. [Units: m, kN]')
model.displayLoad(setToDisplay=None,loadCaseNm='GdeadLoad',unitsScale=1e-3,vectorScale=0.1, multByElemArea=False,viewDef= vtk_graphic_base.CameraParameters('XYZPos'),caption= 'G2: Dead load. [Units: m, kN]')
model.displayLoad(setToDisplay=None,loadCaseNm='GearthPress',unitsScale=1e-3,vectorScale=0.025, multByElemArea=False,viewDef= vtk_graphic_base.CameraParameters('XYZPos'),caption= 'G3: Earth pressure. [Units: m, kN]')

model.displayLoad(setToDisplay=None,loadCaseNm='QtrafSit1a',unitsScale=1e-3,vectorScale=0.05, multByElemArea=False,viewDef= vtk_graphic_base.CameraParameters('XYZPos'),caption= 'Q1a: Traffic loads configuration 1a. [Units: m, kN]')
model.displayLoad(setToDisplay=None,loadCaseNm='QtrafSit1b',unitsScale=1e-3,vectorScale=0.05, multByElemArea=False,viewDef= vtk_graphic_base.CameraParameters('XYZPos'),caption= 'Q1b: Traffic loads configuration 1b. [Units: m, kN]')
model.displayLoad(setToDisplay=None,loadCaseNm='QtrafSit2a',unitsScale=1e-3,vectorScale=0.05, multByElemArea=False,viewDef= vtk_graphic_base.CameraParameters('XYZPos'),caption= 'Q2a: Traffic loads configuration 2a. [Units: m, kN]')
model.displayLoad(setToDisplay=None,loadCaseNm='QtrafSit2b',unitsScale=1e-3,vectorScale=0.05, multByElemArea=False,viewDef= vtk_graphic_base.CameraParameters('XYZPos'),caption= 'Q2b: Traffic loads configuration 2b. [Units: m, kN]')

model.displayLoad(setToDisplay=None,loadCaseNm='QtrafExcept',unitsScale=1e-3,vectorScale=0.05, multByElemArea=False,viewDef= vtk_graphic_base.CameraParameters('XYZPos'),caption= 'QExcept: Exceptional transport. [Units: m, kN]')

model.displayLoad(setToDisplay=None,loadCaseNm='QtrafSit1aPoint',unitsScale=1e-3,vectorScale=0.05, multByElemArea=False,viewDef= vtk_graphic_base.CameraParameters('XYZPos'),caption= 'Q1a: Point Traffic loads configuration 1a. [Units: m, kN]')
model.displayLoad(setToDisplay=None,loadCaseNm='QtrafSit1bPoint',unitsScale=1e-3,vectorScale=0.05, multByElemArea=False,viewDef= vtk_graphic_base.CameraParameters('XYZPos'),caption= 'Q1b: Point Traffic loads configuration 1b. [Units: m, kN]')
model.displayLoad(setToDisplay=None,loadCaseNm='QtrafSit2aPoint',unitsScale=1e-3,vectorScale=0.05, multByElemArea=False,viewDef= vtk_graphic_base.CameraParameters('XYZPos'),caption= 'Q2a: Point Traffic loads configuration 2a. [Units: m, kN]')
model.displayLoad(setToDisplay=None,loadCaseNm='QtrafSit2bPoint',unitsScale=1e-3,vectorScale=0.05, multByElemArea=False,viewDef= vtk_graphic_base.CameraParameters('XYZPos'),caption= 'Q2b: Point Traffic loads configuration 2b. [Units: m, kN]')

model.displayLoad(setToDisplay=None,loadCaseNm='QtrafSit1unif',unitsScale=1e-3,vectorScale=0.5, multByElemArea=False,viewDef= vtk_graphic_base.CameraParameters('XYZPos'),caption= 'QU1: Uniform traffic loads configuration 1. [Units: m, kN]')
model.displayLoad(setToDisplay=None,loadCaseNm='QtrafSit2unif',unitsScale=1e-3,vectorScale=0.5, multByElemArea=False,viewDef= vtk_graphic_base.CameraParameters('XYZPos'),caption= 'QU2: Uniform traffic loads configuration 2. [Units: m, kN]')
