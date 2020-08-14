'''Devuelve la primera forma modal de la viga biapoyada de
acuerdo con la figura B.5 de la IAPF, siendo:
x: Abcisa para la que se obtiene el valor.
L: Luz entre apoyos de la viga.
  '''
def Fi1X(x,L):
    return(sin(PI*x/L))

'''Devuelve el valor de la amplitud del movimiento de vibración para el primer modo de vibración de
acuerdo con la expresión 3.10 de la tesis titulada «Interacción vehículo-estructura y efectos
de resonancia en puentes isostáticos de ferrocarril para líneas de alta velocidad» de Pedro
Museros Romero, siendo:
P: Carga que produce la oscilación.
m: Masa por unidad de longitud.
L: Luz entre apoyos.
w0: Pulsación correspondiente al modo fundamental.
psi: Amortiguamiento.
V: Velocidad con que se desplaza la carga.
t: Instante de tiempo en el que se calcula la amplitud.
  '''
def amplitudCargaAisladaEnPuente(P,m,L,w0,psi,V,t):
    assert(t<=L/V)
    n0= w0/2/PI()
    K= V/2/n0/L
    WOt= w0*t
    return(2*P/m/L/sqr(w0)/(1-sqr(K))*(sin(K*WOt)-K*exp(-psi*WOt)*sin(WOt)))

'''Devuelve el valor de la derivada primera (velocidad) de la amplitud del movimiento de vibración para el primer modo de vibración de
acuerdo con la expresión 3.10 de la tesis titulada «Interacción vehículo-estructura y efectos
de resonancia en puentes isostáticos de ferrocarril para líneas de alta velocidad» de Pedro
Museros Romero, siendo:
P: Carga que produce la oscilación.
m: Masa por unidad de longitud.
L: Luz entre apoyos.
w0: Pulsación correspondiente al modo fundamental.
psi: Amortiguamiento.
V: Velocidad con que se desplaza la carga.
t: Instante de tiempo en el que se calcula la amplitud.
  '''
def amplitudDotCargaAisladaEnPuente(P,m,L,w0,psi,V,t):
    assert(t<=L/V)
    n0= w0/2/PI()
    K= V/2/n0/L
    return(2*(w0*K*cos(t*w0*K)+psi*w0*exp(-(psi*t*w0))*sin(t*w0)*K-w0*exp(-(psi*t*w0))*cos(t*w0)*K)*P/(m*sqr(w0)*(1-sqr(K))*L))

'''Devuelve el valor de la derivada segunda (aceleración) de la amplitud del movimiento de vibración para el primer modo de vibración de
acuerdo con la expresión 3.10 de la tesis titulada «Interacción vehículo-estructura y efectos
de resonancia en puentes isostáticos de ferrocarril para líneas de alta velocidad» de Pedro
Museros Romero, siendo:
P: Carga que produce la oscilación.
m: Masa por unidad de longitud.
L: Luz entre apoyos.
w0: Pulsación correspondiente al modo fundamental.
psi: Amortiguamiento.
V: Velocidad con que se desplaza la carga.
t: Instante de tiempo en el que se calcula la amplitud.
  '''
def amplitudDotDotCargaAisladaEnPuente(P,m,L,w0,psi,V,t):
    assert(t<=L/V)
    n0= w0/2/PI()
    K= V/2/n0/L
    \return{2*(-w0^2*K^2*sin(t*w0*K)-psi^2*w0^2*exp(-(psi*t*w0))*sin(t*w0)*K+w0^2*exp(-(psi*t*w0))*sin(t*w0)*K+2*psi*w0^2*exp(-(psi*t*w0))*cos(t*w0)*K)*P/(m*sqr(w0)*(1-sqr(K))*L)}

'''Devuelve el valor de la amplitud del movimiento de vibración para el primer modo de vibración de
acuerdo con la expresión 3.11 de la tesis titulada «Interacción vehículo-estructura y efectos
de resonancia en puentes isostáticos de ferrocarril para líneas de alta velocidad» de Pedro
Museros Romero, siendo:
P: Carga que produce la oscilación.
m: Masa por unidad de longitud.
L: Luz entre apoyos.
w0: Pulsación correspondiente al modo fundamental.
psi: Amortiguamiento.
V: Velocidad con que se desplaza la carga.
t: Instante de tiempo en el que se calcula la amplitud.
  '''
def amplitudCargaAisladaTrasPuente(P,m,L,w0,psi,V,t):
    n0= w0/2/PI()
    K= V/2/n0/L
    WOt= w0*t
    t2= t-L/V
    assert(t2>=0.0)
    WOt2= w0*t2
    return(2*P/m/L/sqr(w0)*K/(1-sqr(K))*(exp(-psi*WOt)*sin(WOt)-exp(-psi*WOt2)*sin(WOt2)))

'''Devuelve el valor de la derivada primera de la amplitud (velocidad) del movimiento de vibración para el primer modo de vibración de
acuerdo con la expresión 3.11 de la tesis titulada «Interacción vehículo-estructura y efectos
de resonancia en puentes isostáticos de ferrocarril para líneas de alta velocidad» de Pedro
Museros Romero, siendo:
P: Carga que produce la oscilación.
m: Masa por unidad de longitud.
L: Luz entre apoyos.
w0: Pulsación correspondiente al modo fundamental.
psi: Amortiguamiento.
V: Velocidad con que se desplaza la carga.
t: Instante de tiempo en el que se calcula la amplitud.
  '''
def amplitudDotCargaAisladaTrasPuente(P,m,L,w0,psi,V,t):
    n0= w0/2/PI()
    K= V/2/n0/L
    assert(t>=L/V)
    return(2*K*P*(psi*w0*sin(w0*(t-L/V))*exp(-(psi*w0*(t-L/V)))-w0*cos(w0*(t-L/V))*exp(-(psi*w0*(t-L/V)))-psi*w0*exp(-(psi*t*w0))*sin(t*w0)+w0*exp(-(psi*t*w0))*cos(t*w0))/(m*sqr(w0)*(1-sqr(K))*L))

'''Devuelve el valor de la derivada segunda de la amplitud (aceleración) del movimiento de vibración para el primer modo de vibración de
acuerdo con la expresión 3.11 de la tesis titulada «Interacción vehículo-estructura y efectos
de resonancia en puentes isostáticos de ferrocarril para líneas de alta velocidad» de Pedro
Museros Romero, siendo:
P: Carga que produce la oscilación.
m: Masa por unidad de longitud.
L: Luz entre apoyos.
w0: Pulsación correspondiente al modo fundamental.
psi: Amortiguamiento.
V: Velocidad con que se desplaza la carga.
t: Instante de tiempo en el que se calcula la amplitud.
  '''
def amplitudDotDotCargaAisladaTrasPuente(P,m,L,w0,psi,V,t):
    n0= w0/2/PI()
    K= V/2/n0/L
    assert(t>=L/V)
    \return{2*K*P*(-psi^2*w0^2*sin(w0*(t-L/V))*exp(-(psi*w0*(t-L/V)))+w0^2*sin(w0*(t-L/V))*exp(-(psi*w0*(t-L/V)))+2*psi*w0^2*cos(w0*(t-L/V))*exp(-(psi*w0*(t-L/V)))+psi^2*w0^2*exp(-(psi*t*w0)*sin(t*w0))-w0^2*exp(-(psi*t*w0))*sin(t*w0)-2*psi*w0^2*exp(-(psi*t*w0))*cos(t*w0))/(m*sqr(w0)*(1-sqr(K))*L)}

'''Devuelve el valor de la amplitud del movimiento de vibración para el primer modo de vibración de
acuerdo con las expresiones 3.10 y 3.11 de la tesis titulada «Interacción vehículo-estructura y efectos
de resonancia en puentes isostáticos de ferrocarril para líneas de alta velocidad» de Pedro
Museros Romero, siendo:
P: Carga que produce la oscilación.
m: Masa por unidad de longitud.
L: Luz entre apoyos.
w0: Pulsación correspondiente al modo fundamental.
psi: Amortiguamiento.
V: Velocidad con que se desplaza la carga.
t: Instante de tiempo en el que se calcula la amplitud.
  '''
def amplitudCargaAislada(P,m,L,w0,psi,V,t):
    \if
            cond(t<=0)
        then(return(0))
        \else
          {
            \if
              {
                cond(t<=L/V)
                then(return(amplitudCargaAisladaEnPuente(P,m,L,w0,psi,V,t)))
                else(return(amplitudCargaAisladaTrasPuente(P,m,L,w0,psi,V,t)))
              }
          }

'''Devuelve el valor de la derivada primera de la amplitud (velocidad) del movimiento de vibración
para el primer modo de vibración de acuerdo con las expresiones 3.10 y 3.11 de la tesis
titulada «Interacción vehículo-estructura y efectos de resonancia en puentes isostáticos de
ferrocarril para líneas de alta velocidad» de Pedro Museros Romero, siendo:
P: Carga que produce la oscilación.
m: Masa por unidad de longitud.
L: Luz entre apoyos.
w0: Pulsación correspondiente al modo fundamental.
psi: Amortiguamiento.
V: Velocidad con que se desplaza la carga.
t: Instante de tiempo en el que se calcula la amplitud.
  '''
def amplitudDotCargaAislada(P,m,L,w0,psi,V,t):
    \if
        cond(t<=0)
        then(return(0))
        \else
          {
            \if
              {
                cond(t<=L/V)
                then(return(amplitudDotCargaAisladaEnPuente(P,m,L,w0,psi,V,t)))
                else(return(amplitudDotCargaAisladaTrasPuente(P,m,L,w0,psi,V,t)))
              }
          }

'''Devuelve el valor de la derivada segunda de la amplitud (aceleración) del movimiento de vibración
para el primer modo de vibración de acuerdo con las expresiones 3.10 y 3.11 de la tesis
titulada «Interacción vehículo-estructura y efectos de resonancia en puentes isostáticos de
ferrocarril para líneas de alta velocidad» de Pedro Museros Romero, siendo:
P: Carga que produce la oscilación.
m: Masa por unidad de longitud.
L: Luz entre apoyos.
w0: Pulsación correspondiente al modo fundamental.
psi: Amortiguamiento.
V: Velocidad con que se desplaza la carga.
t: Instante de tiempo en el que se calcula la amplitud.
  '''
def amplitudDotDotCargaAislada(P,m,L,w0,psi,V,t):
    \if
        cond(t<=0)
        then(return(0))
        \else
          {
            \if
              {
                cond(t<=L/V)
                then(return(amplitudDotDotCargaAisladaEnPuente(P,m,L,w0,psi,V,t)))
                else(return(amplitudDotDotCargaAisladaTrasPuente(P,m,L,w0,psi,V,t)))
              }
          }

'''Devuelve el valor de la flecha dinámica para el punto de acisa x, siendo:
P: Carga aislada que produce la oscilación.
m: Masa por unidad de longitud.
L: Luz entre apoyos.
w0: Pulsación correspondiente al modo fundamental.
psi: Amortiguamiento.
V: Velocidad con que se desplaza la carga.
t: Instante de tiempo en el que se calcula la amplitud.
x: Abcisa en la que se calcula la flecha.
  '''
def flechaDinamicaCargaAislada(P,m,L,w0,psi,V,t,x):
    return(Fi1X(x,L)*amplitudCargaAislada(P,m,L,w0,psi,V,t))

'''Devuelve el valor de la aceleración para el punto de acisa x, siendo:
P: Carga aislada que produce la oscilación.
m: Masa por unidad de longitud.
L: Luz entre apoyos.
w0: Pulsación correspondiente al modo fundamental.
psi: Amortiguamiento.
V: Velocidad con que se desplaza la carga.
t: Instante de tiempo en el que se calcula la amplitud.
x: Abcisa en la que se calcula la flecha.
  '''
def aceleracionCargaAislada(P,m,L,w0,psi,V,t,x):
    return(Fi1X(x,L)*amplitudDotDotCargaAislada(P,m,L,w0,psi,V,t))

'''Devuelve el valor mínimo de la flecha dinámica para el punto de acisa x, siendo:
P: Carga que produce la oscilación.
m: Masa por unidad de longitud.
L: Luz entre apoyos.
w0: Pulsación correspondiente al modo fundamental.
psi: Amortiguamiento.
V: Velocidad con que se desplaza la carga.
tIni: Instante inicial.
tFin: Instante final.
x: Abcisa en la que se calcula la flecha.
  '''
def flechaDinamicaMinimaCargaAislada(P,m,L,w0,psi,V,x,tIni,tFin):
    incT= 2*PI/w0/10 # 10 puntos por ciclo (5 puntos en cada semionda)
    instT= 
    fDinMin= 1e12
    fTmp= 
    \for
        inicio(instT=tIni) continua(instT<tFin) incremento(instT=instT+incT)
        \bucle
          {
            fTmp= flechaDinamicaCargaAislada(P,m,L,w0,psi,V,instT,x)
            \if
              {
                cond(fTmp<fDinMin)
                then(fDinMin= fTmp)
              }
          }
    return(fDinMin)

'''Devuelve el valor extremo de la aceleración para el punto de acisa x, siendo:
P: Carga que produce la oscilación.
m: Masa por unidad de longitud.
L: Luz entre apoyos.
w0: Pulsación correspondiente al modo fundamental.
psi: Amortiguamiento.
V: Velocidad con que se desplaza la carga.
tIni: Instante inicial.
tFin: Instante final.
x: Abcisa en la que se calcula la flecha.
  '''
def aceleracionExtremaCargaAislada(P,m,L,w0,psi,V,x,tIni,tFin):
    incT= 2*PI/w0/10 # 10 puntos por ciclo (5 puntos en cada semionda)
    instT= 
    aExtrema= 0
    aTmp= 
    \for
        inicio(instT=tIni) continua(instT<tFin) incremento(instT=instT+incT)
        \bucle
          {
            aTmp= aceleracionCargaAislada(P,m,L,w0,psi,V,instT,x)
            \if
              {
                cond(abs(aTmp)>abs(aExtrema))
                then(aExtrema= aTmp)
              }
          }
    return(aExtrema)

'''Devuelve el valor mínimo de la flecha dinámica para el punto de acisa x, siendo:
P: Carga que produce la oscilación.
m: Masa por unidad de longitud.
L: Luz entre apoyos.
w0: Pulsación correspondiente al modo fundamental.
psi: Amortiguamiento.
V: Velocidad con que se desplaza la carga.
vIni: Instante inicial.
vFin: Instante final.
x: Abcisa en la que se calcula la flecha.
  '''
def flechaDinamicaMinimaCargaAisladaRangoVel(P,m,L,w0,psi,x,tIni,tFin,vIni,vFin):
    incV= 10/3.6
    v= 
    fDinMinR= 1e12
    fTmpR= 
    \for
        inicio(v=vIni) continua(v<vFin) incremento(v=v+incV)
        \bucle
          {
            fTmpR= flechaDinamicaMinimaCargaAislada(P,m,L,w0,psi,v,x,tIni,tFin)
            \if
              {
                cond(fTmpR<fDinMinR)
                then(fDinMinR= fTmpR)
              }
print("v= ",v*3.6," km/h fDin= ",fTmpR," m fDinMin= ",fDinMinR," m\n")
          }
    return(fDinMinR)

'''Devuelve el valor extremo de la aceleración para el punto de acisa x, siendo:
P: Carga que produce la oscilación.
m: Masa por unidad de longitud.
L: Luz entre apoyos.
w0: Pulsación correspondiente al modo fundamental.
psi: Amortiguamiento.
V: Velocidad con que se desplaza la carga.
vIni: Instante inicial.
vFin: Instante final.
x: Abcisa en la que se calcula la aceleración.
  '''
def aceleracionExtremaCargaAisladaRangoVel(P,m,L,w0,psi,x,tIni,tFin,vIni,vFin):
    incV= 10/3.6
    v= 
    aExtremaR= 0
    aTmpR= 
    \for
        inicio(v=vIni) continua(v<vFin) incremento(v=v+incV)
        \bucle
          {
            aTmpR= aceleracionExtremaCargaAislada(P,m,L,w0,psi,v,x,tIni,tFin)
            \if
              {
                cond(abs(aTmpR)>abs(aExtremaR))
                then(aExtremaR= aTmpR)
              }
print("v= ",v*3.6," km/h a= ",aTmpR," m aExtrema= ",aExtremaR," m\n")
          }
    return(aExtremaR)

'''Devuelve el valor de la flecha dinámica para el punto de acisa x, siendo:
ejesTren: Lista con las cargas por eje del tren que produce la oscilación.
m: Masa por unidad de longitud.
L: Luz entre apoyos.
w0: Pulsación correspondiente al modo fundamental.
psi: Amortiguamiento.
V: Velocidad con que se desplaza la carga.
t: Instante de tiempo en el que se calcula la amplitud (el instante t=0 corresponde a la entrada del tren en la viga).
x: Abcisa en la que se calcula la flecha.
  '''
def flechaDinamicaTren(ejesTren,m,L,w0,psi,V,t,x):
    sz= ejesTren.size
    i= 0.0
    retval= 0.0
    xPEje= [0,0]
    tEje= 0.0
    fEje= 0.0
    \for
        inicio(i=0 ) continua(i<sz) incremento(i=i+1)
        \bucle
          {
            xPEje= ejesTren[i]
            tEje= t-xPEje[0]/V # Tiempo "local" para el eje.
            fEje= flechaDinamicaCargaAislada(-xPEje[1],m,L,w0,psi,V,tEje,x) # Flecha para el eje aislado.
            retval= retval+fEje
         }
    return(retval)

'''Devuelve el valor de la aceleración inducida por el paso de un tren:
ejesTren: Lista con las cargas por eje del tren que produce la oscilación.
m: Masa por unidad de longitud.
L: Luz entre apoyos.
w0: Pulsación correspondiente al modo fundamental.
psi: Amortiguamiento.
V: Velocidad con que se desplaza la carga.
t: Instante de tiempo en el que se calcula la amplitud (el instante t=0 corresponde a la entrada del tren en la viga).
x: Abcisa en la que se calcula la flecha.
  '''
def aceleracionInducidaTren(ejesTren,m,L,w0,psi,V,t,x):
    sz= ejesTren.size
    i= 0.0
    retval= 0.0
    xPEje= [0,0]
    tEje= 0.0
    fEje= 0.0
    \for
        inicio(i=0 ) continua(i<sz) incremento(i=i+1)
        \bucle
          {
            xPEje= ejesTren[i]
            tEje= t-xPEje[0]/V # Tiempo "local" para el eje.
            fEje= aceleracionCargaAislada(-xPEje[1],m,L,w0,psi,V,tEje,x) # Flecha para el eje aislado.
            retval= retval+fEje
         }
    return(retval)

'''Devuelve el valor mínimo de la flecha dinámica para el punto de acisa x, siendo:
ejesTren: Lista con las cargas por eje del tren que produce la oscilación.
m: Masa por unidad de longitud.
L: Luz entre apoyos.
w0: Pulsación correspondiente al modo fundamental.
psi: Amortiguamiento.
V: Velocidad con que se desplaza la carga.
tIni: Instante inicial.
tFin: Instante final.
x: Abcisa en la que se calcula la flecha.
  '''
def flechaDinamicaMinimaTren(ejesTren,m,L,w0,psi,V,x):
    numEjes= ejesTren.size
    tIni= 0
    ultEjeTren= ejesTren[numEjes-1]
    longTren= ultEjeTren[0]
    tFin= 1.5*(longTren+L)/V
    incT= 2*PI/w0/10 # 10 puntos por ciclo (5 puntos en cada semionda)
    instT= 
    fDinMin= 1e12
    fTmp= 
    \for
        inicio(instT=tIni) continua(instT<tFin) incremento(instT=instT+incT)
        \bucle
          {
            fTmp= flechaDinamicaTren(ejesTren,m,L,w0,psi,V,instT,x)
            \if
              {
                cond(fTmp<fDinMin)
                then(fDinMin= fTmp)
              }
          }
    return(fDinMin)

'''Devuelve el valor extremo de la aceleración inducida por el tren en el punto de acisa x, siendo:
ejesTren: Lista con las cargas por eje del tren que produce la oscilación.
m: Masa por unidad de longitud.
L: Luz entre apoyos.
w0: Pulsación correspondiente al modo fundamental.
psi: Amortiguamiento.
V: Velocidad con que se desplaza la carga.
tIni: Instante inicial.
tFin: Instante final.
x: Abcisa en la que se calcula la flecha.
  '''
def aceleracionExtremaInducidaTren(ejesTren,m,L,w0,psi,V,x):
    numEjes= ejesTren.size
    tIni= 0
    ultEjeTren= ejesTren[numEjes-1]
    longTren= ultEjeTren[0]
    tFin= 1.5*(longTren+L)/V
    incT= 2*PI/w0/10 # 10 puntos por ciclo (5 puntos en cada semionda)
    instT= 
    aExtrema= 0
    aTmp= 
    \for
        inicio(instT=tIni) continua(instT<tFin) incremento(instT=instT+incT)
        \bucle
          {
            aTmp= aceleracionInducidaTren(ejesTren,m,L,w0,psi,V,instT,x)
            \if
              {
                cond(abs(aTmp)>abs(aExtrema))
                then(aExtrema= aTmp)
              }
          }
    return(aExtrema)

'''Devuelve el valor mínimo de la flecha dinámica para el punto de abcisa x, siendo:
P: Carga que produce la oscilación.
m: Masa por unidad de longitud.
L: Luz entre apoyos.
w0: Pulsación correspondiente al modo fundamental.
psi: Amortiguamiento.
V: Velocidad con que se desplaza la carga.
vIni: Instante inicial.
vFin: Instante final.
x: Abcisa en la que se calcula la flecha.
  '''
def flechaDinamicaMinimaTrenRangoVel(ejesTren,m,L,w0,psi,x,vIni,vFin, fName):
    incV= 10/3.6
    v= 
    fDinMinR= 1e12
    fTmpR= 
    \for
        inicio(v=vIni) continua(v<vFin) incremento(v=v+incV)
        \bucle
          {
            fTmpR= flechaDinamicaMinimaTren(ejesTren,m,L,w0,psi,v,x)
            \if
              {
                cond(fTmpR<fDinMinR)
                then(fDinMinR= fTmpR)
              }
            \print[fName]{v*3.6," ",fTmpR,"\n"}
          }
    return(fDinMinR)

'''Devuelve el valor extremo de la aceleración inducida por el tren para el punto de abcisa x, siendo:
P: Carga que produce la oscilación.
m: Masa por unidad de longitud.
L: Luz entre apoyos.
w0: Pulsación correspondiente al modo fundamental.
psi: Amortiguamiento.
V: Velocidad con que se desplaza la carga.
vIni: Instante inicial.
vFin: Instante final.
x: Abcisa en la que se calcula la flecha.
  '''
def aceleracionExtremaTrenRangoVel(ejesTren,m,L,w0,psi,x,vIni,vFin, fName):
    incV= 10/3.6
    v= 
    aExtremaR= 0
    aTmpR= 
    \for
        inicio(v=vIni) continua(v<vFin) incremento(v=v+incV)
        \bucle
          {
            aTmpR= aceleracionExtremaInducidaTren(ejesTren,m,L,w0,psi,v,x)
            \if
              {
                cond(abs(aTmpR)>abs(aExtremaR))
                then(aExtremaR= aTmpR)
              }
            \print[fName]{v*3.6," ",abs(aTmpR),"\n"}
          }
    return(aExtremaR)
