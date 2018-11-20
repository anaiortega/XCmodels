# -*- coding: utf-8 -*-

execfile('../model_data.py')
execfile('../captionTexts.py')

#  partToDisplay: XC set of elements to be displayed
#  caption:  text to write in the graphic

model.displayMesh(partToDisplay=xcTotalSet.elSet,caption=xcTotalSet.genDescr.capitalize() + ', '+ capTexts['FEmesh'])
