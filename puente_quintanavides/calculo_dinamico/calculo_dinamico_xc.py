
exec(open('acciones/IAPF/trenes_reales_av_xcm.py').read())
exec(open('oscilacion_viga_biapoyada_xcm.py').read())

L= 39.2
EI= 7.69879e+11
f= 26.54e-3
rho= 12713.38e3/L
P= -100e3
amortig= 2/100} # Amortiguamiento

w1= sqr(PI())*sqrt(EI/rho/(L^4))
T1= 2*PI/w1
f1= 1/T1


print("EI= ",EI/1e3,"kN m2\n")
print("rho= ",rho,"\n")
print("w1= ",w1/PI,"*pi rad/s\n")
print("T1= ",T1," s\n")
print("f1= ",f1," Hz\n")
M1= rho*L/2
uCentroP= P*L^3/48/EI} # Flecha en el centro de vano para la carga P.
deltaCentro= } # Flecha en el centro de vano para la carga P.


vProy= 270/3.6
vIni= 100/3.6
vFin= 1.2*vProy

\nuevo_archivo_salida["fMaxima"]{"fMaximaICE2.dat"}
fDinTren= flechaDinamicaMinimaTrenRangoVel(cargasTrenICE2,rho,L,w1,amortig,L/2,vIni,vFin,"fMaxima")
cierra_archivo_salida("fMaxima")
print("fDinTren= ",fDinTren," m\n")
os.system("cp fMaximaTalgoICE2.dat fMaxima.dat")
os.system("./genGraficoVel")
os.system("rm fMaxima.dat")
os.system("mv output.eps fMaximaICE2.eps")

\nuevo_archivo_salida["aMaxima"]{"aMaximaICE2.dat"}
aExtrema= aceleracionExtremaTrenRangoVel(cargasTrenICE2,rho,L,w1,amortig,L/2,vIni,vFin,"aMaxima")
cierra_archivo_salida("aMaxima")
print("aExtrema= ",aExtrema," m/s2\n")
os.system("cp aMaximaICE2.dat aMaxima.dat")
os.system("./genGraficoAcel")
os.system("rm aMaxima.dat")
os.system("mv output.eps aExtremaICE2.eps")


\nuevo_archivo_salida["fMaxima"]{"fMaximaTalgo350.dat"}
fDinTren= flechaDinamicaMinimaTrenRangoVel(cargasTrenTalgo350,rho,L,w1,amortig,L/2,vIni,vFin,"fMaxima")
cierra_archivo_salida("fMaxima")
print("fDinTren= ",fDinTren," m\n")
os.system("cp fMaximaTalgo350.dat fMaxima.dat")
os.system("./genGraficoVel")
os.system("rm fMaxima.dat")
os.system("mv output.eps fMaximaTalgo350.eps")

\nuevo_archivo_salida["aMaxima"]{"aMaximaTalgo350.dat"}
aExtrema= aceleracionExtremaTrenRangoVel(cargasTrenTalgo350,rho,L,w1,amortig,L/2,vIni,vFin,"aMaxima")
cierra_archivo_salida("aMaxima")
os.system("cp aMaximaTalgo350.dat aMaxima.dat")
print("aExtrema= ",aExtrema," m/s2\n")
os.system("./genGraficoAcel")
os.system("rm aMaxima.dat")
os.system("mv output.eps aExtremaTalgo350.eps")
