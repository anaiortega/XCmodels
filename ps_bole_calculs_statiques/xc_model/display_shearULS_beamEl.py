# -*- coding: utf-8 -*-
from postprocess.control_vars import *
from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import vtk_FE_graphic
from postprocess.xcVtk.diagrams import control_var_diagram as cvd
from postprocess import limit_state_data as lsd

model_path="./"
#Project directory structure
exec(open(model_path+'env_config.py').read()))

modelDataInputFile=model_path+"fe_model.py" #data for FE model generation
exec(open(modelDataInputFile).read()))


#Load properties to display:
fName=  cfg.projectDirTree.getVerifShearFile()
exec(open(fName).read()))
exec(open(model_path+'/captionTexts.py').read()))


limitStateLabel= lsd.shearResistance.label


#Possible arguments: 'CF', 'N', 'My', 'Mz', 'Mu', 'Vy', 'Vz', 'theta', 'Vcu', 'Vsu', 'Vu'
shearFactor= 1.14 #Voir note de calcul.
argument= 'Vy'#'CF' #'Vu'
setDispRes= deckSet #deckSet #parapetSet #bridgeSectionSet   #set of linear elements to which display results 

#CF= -0.5
#Vy= 0.01
diagram= cvd.ControlVarDiagram(scaleFactor= -0.005,fUnitConv= shearFactor,sets=[setDispRes],attributeName= limitStateLabel,component= argument)
diagram.addDiagram()


displaySettings= vtk_FE_graphic.DisplaySettingsFE()
#predefined view names: 'XYZPos','XNeg','XPos','YNeg','YPos',
 #                        'ZNeg','ZPos'  (defaults to 'XYZPos')

displaySettings.cameraParameters= vtk_graphic_base.CameraParameters('ZPos') #Point of view.
displaySettings.setupGrid(setDispRes)

displaySettings.defineMeshScene(None)
displaySettings.appendDiagram(diagram) #Append diagram to the scene.

#exec(open('draw_supports.py').read()))
#displaySettings.renderer.AddActor(supportsActor)

caption= capTexts[limitStateLabel] + ', ' + capTexts[argument] + '. '+ setDispRes.genDescr.capitalize() + ', ' + setDispRes.sectDescr[1]
displaySettings.displayScene(caption)



