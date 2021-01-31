# -*- coding: utf-8 -*-

exec(open('../model_data.py').read()))
exec(open('../captionTexts.py').read()))

#  partToDisplay: XC set of elements to be displayed
#  caption:  text to write in the graphic

model.displayMesh(partToDisplay=xcTotalSet.elSet,caption=xcTotalSet.genDescr.capitalize() + ', '+ capTexts['FEmesh'])
