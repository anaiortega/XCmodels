import Draft
# Auxiliary entities
# points=[FreeCAD.Vector(39673.4458128,13496.4310982,0.0),FreeCAD.Vector(39673.6458128,13496.6310982,0.0),FreeCAD.Vector(39678.2459759,13496.4996649,0.0),FreeCAD.Vector(39678.4459759,13496.2996649,0.0),FreeCAD.Vector(39678.4459759,13494.4996649,0.0),FreeCAD.Vector(39678.0726975,13492.0230219,0.0),FreeCAD.Vector(39675.6458128,13492.3888007,0.0),FreeCAD.Vector(39675.4458128,13492.1888007,0.0),FreeCAD.Vector(39675.4458128,13491.6810982,0.0),FreeCAD.Vector(39673.9458128,13491.1310982,0.0),FreeCAD.Vector(39673.4458128,13491.6310982,0.0)]

# left_curb=Draft.makeWire(points,closed=True,face=True,support=None).Shape

# points=[FreeCAD.Vector(39678.4459759,13494.4996649,0.0),FreeCAD.Vector(39691.2242129,13492.5737355,0.0),FreeCAD.Vector(39690.8509345,13490.0970924,0.0),FreeCAD.Vector(39678.0726975,13492.0230219,0.0)]
# left_slab= Draft.makeWire(points,closed=True,face=True,support=None).Shape

# points=[FreeCAD.Vector(39691.2242129,13492.5737355,0.0),FreeCAD.Vector(39754.7457399,13490.6646336,0.0),FreeCAD.Vector(39754.6701658,13488.1664768,0.0),FreeCAD.Vector(39690.9609692,13490.0805081,0.0)]
# right_slab=Draft.makeWire(points,closed=True,face=True,support=None).Shape

# points=[FreeCAD.Vector(39754.7457399,13490.6646336,0.0),FreeCAD.Vector(39754.9456496,13490.8586254,0.0),FreeCAD.Vector(39754.9456496,13493.5853605,0.0),FreeCAD.Vector(39755.145568,13493.7910725,0.0),FreeCAD.Vector(39759.7458128,13493.9225081,0.0),FreeCAD.Vector(39759.9458128,13493.7225081,0.0),FreeCAD.Vector(39759.9458128,13488.5225081,0.0),FreeCAD.Vector(39759.4458128,13488.0225081,0.0),FreeCAD.Vector(39757.9458128,13488.5225081,0.0),FreeCAD.Vector(39757.4458128,13488.0825081,0.0),FreeCAD.Vector(39754.6701658,13488.1664768,0.0)]
# right_curb=Draft.makeWire(points,closed=True,face=True,support=None).Shape


# area_left_curb=left_curb.Area
# area_right_curb=right_curb.Area

# area_each_block=(area_left_curb+left_slab.Area+right_slab.Area+area_right_curb)/6.0

# offset_left_curb=(area_each_block-area_left_curb)/2.5

# offset_right_curb=(area_each_block-area_right_curb)/2.5

# offset_each_block=area_each_block/2.5


points=[FreeCAD.Vector(39673.4458128,13491.6310982,0.0),FreeCAD.Vector(39673.4458128,13496.4310982,0.0),FreeCAD.Vector(39673.6458128,13496.6310982,0.0),FreeCAD.Vector(39678.2459759,13496.4996649,0.0),FreeCAD.Vector(39678.4459759,13496.2996649,0.0),FreeCAD.Vector(39678.4459759,13494.4996649,0.0),FreeCAD.Vector(39685.4077217,13493.450394,0.0),FreeCAD.Vector(39685.0344433,13490.973751,0.0),FreeCAD.Vector(39675.6458128,13492.3888007,0.0),FreeCAD.Vector(39675.4458128,13492.1888007,0.0),FreeCAD.Vector(39675.4458128,13491.6810982,0.0),FreeCAD.Vector(39673.9458128,13491.1310982,0.0)]
block1=Draft.makeWire(points,closed=True,face=True,support=None).Shape

points=[FreeCAD.Vector(39685.4077217,13493.450394,0.0),FreeCAD.Vector(39691.2242129,13492.5737355,0.0),FreeCAD.Vector(39701.4413059,13492.2771972,0.0),FreeCAD.Vector(39701.3657318,13489.7790404,0.0),FreeCAD.Vector(39690.9609692,13490.0805081,0.0),FreeCAD.Vector(39685.0344433,13490.973751,0.0)]
block2=Draft.makeWire(points,closed=True,face=True,support=None).Shape

points=[FreeCAD.Vector(39701.4413059,13492.2771972,0.0),FreeCAD.Vector(39717.6522536,13491.7867842,0.0),FreeCAD.Vector(39717.5766795,13489.2886274,0.0),FreeCAD.Vector(39701.3657318,13489.7790404,0.0)]
block3=Draft.makeWire(points,closed=True,face=True,support=None).Shape

points=[FreeCAD.Vector(39717.6522536,13491.7867842,0.0),FreeCAD.Vector(39733.8632014,13491.2963713,0.0),FreeCAD.Vector(39733.7876273,13488.7982145,0.0),FreeCAD.Vector(39717.5766795,13489.2886274,0.0)]
block4=Draft.makeWire(points,closed=True,face=True,support=None).Shape

points=[FreeCAD.Vector(39733.8632014,13491.2963713,0.0),FreeCAD.Vector(39750.0741491,13490.8059584,0.0),FreeCAD.Vector(39749.998575,13488.3078016,0.0),FreeCAD.Vector(39733.7876273,13488.7982145,0.0)]
block5=Draft.makeWire(points,closed=True,face=True,support=None).Shape

points=[FreeCAD.Vector(39750.0741491,13490.8059584,0.0),FreeCAD.Vector(39754.7457399,13490.6646336,0.0),FreeCAD.Vector(39754.9456496,13490.8586254,0.0),FreeCAD.Vector(39754.9531288,13493.1777358,0.0),FreeCAD.Vector(39754.9456496,13493.5853605,0.0),FreeCAD.Vector(39755.145568,13493.7910725,0.0),FreeCAD.Vector(39759.7458128,13493.9225081,0.0),FreeCAD.Vector(39759.9458128,13493.7225081,0.0),FreeCAD.Vector(39759.9458128,13488.5225081,0.0),FreeCAD.Vector(39759.4458128,13488.0225081,0.0),FreeCAD.Vector(39757.9458128,13488.5225081,0.0),FreeCAD.Vector(39757.4458128,13488.0825081,0.0),FreeCAD.Vector(39749.998575,13488.3078016,0.0)]
block6=Draft.makeWire(points,closed=True,face=True,support=None).Shape

com_block1=Draft.makePoint(block1.CenterOfMass)
com_block2=Draft.makePoint(block2.CenterOfMass)
com_block3=Draft.makePoint(block3.CenterOfMass)
com_block4=Draft.makePoint(block4.CenterOfMass)
com_block5=Draft.makePoint(block5.CenterOfMass)
com_block6=Draft.makePoint(block6.CenterOfMass)
(39757.4-com_block6.X.Value)/10.
(39757.4-com_block5.X.Value)/10.
(39757.4-com_block4.X.Value)/10.
(39757.4-com_block3.X.Value)/10.
(39757.4-com_block2.X.Value)/10.
(39757.4-com_block1.X.Value)/10.
