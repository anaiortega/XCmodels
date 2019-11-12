# -*- coding: utf-8 -*-
from postprocess.control_vars import *
from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import vtk_FE_graphic
from postprocess.xcVtk.diagrams import control_var_diagram as cvd
from postprocess import limit_state_data as lsd

model_path="./"
#Project directory structure
execfile(model_path+'env_config.py')

modelDataInputFile=model_path+"fe_model.py" #data for FE model generation
execfile(modelDataInputFile)


#Load properties to display:
fName=  cfg.projectDirTree.getVerifShearFile()
execfile(fName)
execfile(model_path+'/captionTexts.py')


limitStateLabel= lsd.shearResistance.label


#Possible arguments: 'CF', 'N', 'My', 'Mz', 'Mu', 'Vy', 'Vz', 'theta', 'Vcu', 'Vsu', 'Vu'
shearFactor= 1.14 #Voir note de calcul.
argument= 'Vy'#'CF' #'Vu'
setDispRes= deckSet #deckSet #parapetSet #bridgeSectionSet   #set of linear elements to which display results 

#CF= -0.5
#Vy= 0.01
diagram= cvd.ControlVarDiagram(scaleFactor= -0.005,fUnitConv= shearFactor,sets=[setDispRes],attributeName= limitStateLabel,component= argument)
diagram.addDiagram()


defDisplay= vtk_FE_graphic.RecordDefDisplayEF()
#predefined view names: 'XYZPos','XNeg','XPos','YNeg','YPos',
 #                        'ZNeg','ZPos'  (defaults to 'XYZPos')

defDisplay.cameraParameters= vtk_graphic_base.CameraParameters('ZPos') #Point of view.
defDisplay.setupGrid(setDispRes)

defDisplay.defineMeshScene(None)
defDisplay.appendDiagram(diagram) #Append diagram to the scene.

#execfile('draw_supports.py')
#defDisplay.renderer.AddActor(supportsActor)

caption= capTexts[limitStateLabel] + ', ' + capTexts[argument] + '. '+ setDispRes.genDescr.capitalize() + ', ' + setDispRes.sectDescr[1]
defDisplay.displayScene(caption)



