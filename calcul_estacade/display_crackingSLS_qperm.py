# -*- coding: utf-8 -*-

from postprocess.control_vars import *
from postprocess import limit_state_data as lsd
from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import vtk_FE_graphic
from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import Fields


model_path="./"
#Project directory structure
exec(open(model_path+'env_config.py').read()))

modelDataInputFile=model_path+"model_data.py" #data for FE model generation
exec(open(modelDataInputFile).read()))


#Load properties to display:
fName=  cfg.projectDirTree.getVerifCrackQpermFile()
exec(open(fName).read()))
exec(open('./captionTexts.py').read()))

limitStateLabel= lsd.quasiPermanentLoadsCrackControl.label
displaySettings= vtk_FE_graphic.DisplaySettingsFE()

argument= 'getMaxSteelStress'
#argument= 'crackControlVarsNeg.steelStress'


sets= [setDeck,setDock,setParapet]

for setDisp in sets:
  attributeName= limitStateLabel + 'Sect1'
  field= Fields.getScalarFieldFromControlVar(attributeName,argument,setDisp,None,1.0)
  field.plot(displaySettings,caption= capTexts[limitStateLabel] + ', ' + capTexts[argument] + '. '+ setDisp.genDescr.capitalize() + ', ' + setDisp.sectDescr[0] )
  attributeName= limitStateLabel + 'Sect2'
  field= Fields.getScalarFieldFromControlVar(attributeName,argument,setDisp,None,1.0)
  field.plot(displaySettings,caption= capTexts[limitStateLabel] + ', ' + capTexts[argument] + '. '+ setDisp.genDescr.capitalize() + ', ' + setDisp.sectDescr[1] )

