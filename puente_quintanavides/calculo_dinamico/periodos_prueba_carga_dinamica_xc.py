
exec(open('acciones/IAPF/trenes_reales_av_xcm.py').read()))
exec(open('oscilacion_viga_biapoyada_xcm.py').read()))

L= 39.2
EI= 7.69879e+11
f= 26.54e-3
rho= 12713.38e3/L
amortig= 2/100} # Amortiguamiento

w1= sqr(PI())*sqrt(EI/rho/(L^4))
T1= 2*PI/w1
f1= 1/T1

print("EI= ",EI/1e3,"kN m2\n")

print("Tablero vacío:\n")
print("rho= ",rho,"\n")
print("w1= ",w1/PI,"*pi rad/s\n")
print("T1= ",T1," s\n")
print("f1= ",f1," Hz\n")

rho2= (12713.38e3+2*117000*9.81)/L

w2= sqr(PI())*sqrt(EI/rho2/(L^4))
T2= 2*PI/w2
f2= 1/T2

print("Tablero cargado:\n")
print("rho2= ",rho2,"\n")
print("w2= ",w2/PI,"*pi rad/s\n")
print("T2= ",T2," s\n")
print("f2= ",f2," Hz\n")
