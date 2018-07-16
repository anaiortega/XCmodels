# -*- coding: utf-8 -*-

from actions.wind import windSIA261

# Wind according to SIA 261
z= 10 # Height over ground.
catTerrain= "II" #Table 4 page 31 SIA 261.
qp0= 0.9e3 #Annexe E page 117 SIA 261:2014 (116 in the PDF file).

ch= windSIA261.Ch(z,catTerrain)
qp= windSIA261.qp(qp0,z,catTerrain)

print "ch= ", ch
print "Dynamic pressure qp= ", qp/1e3, "kN"
