
execfile('acciones/IAPF/trenes_reales_av_xcm.py')
execfile('oscilacion_viga_biapoyada_xcm.py')

L= 15
EI= 7694081e3
u= 26.54e-3
rho= 15000
P= -100e3
amortig= 2/100} # Amortiguamiento

w1= sqr(PI())*sqrt(EI/rho/(L^4))
T1= 2*PI/w1
f1= 1/T1
M1= rho*L/2
uCentroP= P*L^3/48/EI # Flecha en el centro de vano para la carga P.
deltaCentro=  # Flecha en el centro de vano para la carga P.


vIni= 100/3.6
vFin= 370/3.6

# 
fDinamica= flechaDinamicaMinimaCargaAisladaRangoVel(P,rho,L,w1,amortig,L/2,0,5,vIni,vFin)
print("fDinMin= ",fDinamica,"\n")
acel= aceleracionExtremaCargaAisladaRangoVel(P,rho,L,w1,amortig,L/2,0,5,vIni,vFin)
print("acel= ",acel," m/s2\n")
fDinTren= flechaDinamicaMinimaTren(cargasTrenICE2,rho,L,w1,amortig,160/3.6,L/2)
print("fDinTren= ",fDinTren," m\n")
\nuevo_archivo_salida["ley"]{"ley.dat"}
fDinTren= flechaDinamicaMinimaTrenRangoVel(cargasTrenICE2,rho,L,w1,amortig,L/2,155/3.6,325/3.6,"ley")
cierra_archivo_salida("ley")
print("fDinTren= ",fDinTren," m\n")
\nuevo_archivo_salida["ley"]{"ley.dat"}
aExtrema= aceleracionExtremaTrenRangoVel(cargasTrenICE2,rho,L,w1,amortig,L/2,155/3.6,325/3.6,"ley")
cierra_archivo_salida("ley")
print("aExtrema= ",aExtrema," m/s2\n")

quit()

\nuevo_archivo_salida["ley"]{"ley.dat"}
\for
    inicio(v=vIni) continua(v<vFin) incremento(v=v+incV)
    \bucle
            fDinamica= flechaDinamicaMinimaCargaAislada(P,rho,L,w1,amortig,v,L/2,0,5)
        \print["ley"]{v," ",-fDinamica,"\n"}
cierra_archivo_salida("ley")

print("EI= ",EI/1e3,"kN m2\n")
print("rho= ",rho,"\n")
print("w1= ",w1/PI,"*pi rad/s\n")
print("T1= ",T1," s\n")
print("f1= ",f1," Hz\n")
print("uCentroP= ",uCentroP*1e3," mm\n")

