# -*- coding: utf-8 -*-

execfile('../model_data.py')
execfile('../captionTexts.py')

#  partToDisplay: XC set of elements to be displayed
#  caption:  text to write in the graphic
#  viewNm:   name of the view to use
#            predefined view names: 'XYZPos','XYZNeg','XNeg','XPos','YNeg','YPos',
#            'ZNeg','ZPos'  (defaults to 'XYZPos')

model.displayMesh(partToDisplay=xcTotalSet.elSet,caption=xcTotalSet.genDescr.capitalize() + ', '+ capTexts['FEmesh'],viewNm='XPos')
