# -*- coding: utf-8 -*-

from actions.snow import snowSIA

h= 500 #Bridge drawings.
h0= h+200.0 #Bex. Annexe D norme SIA-261

# Altitude inférieure à 800 mètres => pas de corniche.

windExposition= "normal"
shapeCoef= 1.0 #Horizontal deck with correction (see 5.3.5).
qkNeige= snowSIA.qkPont(h0,windExposition)

print "qkNeige (SIA-261:2014)= ", qkNeige/1e3, " kN/m2"

