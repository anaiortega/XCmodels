# -*- coding: utf-8 -*-
from __future__ import division
#Abutment geometry
cantoZap=1.5
espCoronAlet=0.4
espMurEstr=1.35
anchoEstr=anchoTot
hMuri=8.4  #altura del muro del estribo en su extremo izquierdo
hMurd=9.25 #altura del muro del estribo en su extremo derecho
hMuret=1.35
Lpunt=1.8+0.5*espMurEstr
Lzap=7.4+0.5*espMurEstr
Lvoladzi=0
Hminvoladzi=0
Hmaxvoladzi=0
Lvoladzd=5.0
Hminvoladzd=0.5
Hmaxvoladzd=0.5+3.3
pendMurAlet=1/12.  #H:V
excNeop=espMurEstr/2.+0.5 #excentricidad de los aparatos de apoyo respecto al plano medio del muro

#ángulo que forman muros laterales y aletas con el plano ortogonal al muro del
#estribo
angMuri=-30
angMurd=30

eSizeAbut= 0.4     #length of elements

#Loads
# K30: roca blanda o alterada 100 kg/cm3 
K30=1000e6        #(N/m3)
Kcuadr=(K30*0.3)/Lzap #suelo cohesivo Lzap en [m]
Kcuadr=K30*((Lzap+0.3)/2./Lzap)**2 #suelo arenoso Lzap en [m]
Krectang=2/3.*Kcuadr*(1+Lzap/(2*anchoEstr)) # Lzap y anchoEstr en [m]
Kbalasto=Krectang                  #coef. balasto (N/m3)
# empuje del terreno
fi_terr=30                            #ángulo de rozamiento interno
K0=1-math.sin(math.radians(fi_terr))  #coeficiente de empuje al reposo
densrell=2e3                  #densidad del relleno (kg/m3)
zGround=0
qunifTerr=10e3 #carga uniforme sobre el terreno [N/m2]
