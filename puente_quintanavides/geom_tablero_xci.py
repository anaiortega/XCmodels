# -*- coding: utf-8
luzVano= 38

abcisaSeccion= 0
LTramo0= 0.60
LTramo1= 8.60
LTramo2= 3.15
LTramo3= 2*7.25

idTramo0= "T0"
idTramo1= "T1"
idTramo2= "T2"
idTramo3= "T3"
idTramo4= "T4"
idTramo5= "T5"
idTramo6= "T6"

puntosA= []
puntosB= []
puntosI1= []
puntosI2= []
puntosI3= []
puntosI4= []
puntosC= []
puntosD= []

tagsCarasVoladizoIzquierdo= []
tagsCarasVoladizoDerecho= []
tagsCarasLosaViaIzquierda= []
tagsCarasLosaViaDerecha= []
tagsCarasAlmaIzquierda= []
tagsCarasAlmaCentral= []
tagsCarasAlmaDerecha= []
tagsCarasLosaInfIzquierda= []
tagsCarasLosaInfDerecha= []
tagsCarasDiafragmaDorsal= []
tagsCarasDiafragmaFrontal= []

# Via 1 carril derecho
yVia1CD= -3.0673
zVia1CD= 1.3917
# Via 1 carril izquierdo
yVia1CI= -1.6324
zVia1CI= 1.4078

# Via 2 carril izquierdo
yVia2CI= 3.0673
zVia2CI= 1.3917
# Via 2 carril derecho
yVia2CD= 1.6324
zVia2CD= 1.4078

# Unión losa superior con alma derecha
yUnionLosaSupAlmaDerecha= -3.6938
zUnionLosaSupAlmaDerecha= 1.3847
# Unión losa superior con alma izquierda
yUnionLosaSupAlmaIzquierda= 3.6938
zUnionLosaSupAlmaIzquierda= 1.3847

# Unión losa inferior con alma derecha
yUnionLosaInfAlmaDerecha= -2.4031
zLosaInf= -1.1710
# Unión losa inferior con alma izquierda
yUnionLosaInfAlmaIzquierda= 2.4031

zUnionLosaSupAlmaCentral= 1.426
zExtremoAlas= 1.3478

angAlma= atan2(yUnionLosaSupAlmaIzquierda-yUnionLosaInfAlmaIzquierda,zUnionLosaSupAlmaIzquierda-zLosaInf)

# Centro de la losa inferior
xCentroLosaInf= LTramo0+LTramo1+LTramo2+LTramo3/2
yCentroLosaInf= 0.0
zCentroLosaInf= zLosaInf

def defineSeccion(abcisa,nmbListaPuntos):
    pnt( geom.Pos3d(abcisa, -7, zExtremoAlas) ) )
    nmbListaPuntos(inserta(last_tag_punto))
    pnt( geom.Pos3d(abcisa, yUnionLosaSupAlmaDerecha, zUnionLosaSupAlmaDerecha) ) )
    nmbListaPuntos(inserta(last_tag_punto))
    pnt( geom.Pos3d(abcisa, yVia1CD, zVia1CD) ) )
    nmbListaPuntos(inserta(last_tag_punto))
    pnt( geom.Pos3d(abcisa, yVia1CI, zVia1CI) ) )
    nmbListaPuntos(inserta(last_tag_punto))
    pnt( geom.Pos3d(abcisa, 0, zUnionLosaSupAlmaCentral) ) )
    nmbListaPuntos(inserta(last_tag_punto))
    pnt( geom.Pos3d(abcisa, yVia2CD, zVia2CD) ) )
    nmbListaPuntos(inserta(last_tag_punto))
    pnt( geom.Pos3d(abcisa, yVia2CI, zVia2CI) ) )
    nmbListaPuntos(inserta(last_tag_punto))
    pnt( geom.Pos3d(abcisa, yUnionLosaSupAlmaIzquierda, zUnionLosaSupAlmaIzquierda) ) )
    nmbListaPuntos(inserta(last_tag_punto))
    pnt( geom.Pos3d(abcisa, 7, zExtremoAlas) ) )
    nmbListaPuntos(inserta(last_tag_punto))
    pnt( geom.Pos3d(abcisa, yUnionLosaInfAlmaDerecha, zLosaInf) ) )
    nmbListaPuntos(inserta(last_tag_punto))
    pnt( geom.Pos3d(abcisa, -1.575, zLosaInf) ) )
    nmbListaPuntos(inserta(last_tag_punto))
    pnt( geom.Pos3d(abcisa, -0.7875, zLosaInf) ) )
    nmbListaPuntos(inserta(last_tag_punto))
    pnt( geom.Pos3d(abcisa, 0, zLosaInf) ) )
    nmbListaPuntos(inserta(last_tag_punto))
    pnt( geom.Pos3d(abcisa, 0.7875, zLosaInf) ) )
    nmbListaPuntos(inserta(last_tag_punto))
    pnt( geom.Pos3d(abcisa, 1.575, zLosaInf) ) )
    nmbListaPuntos(inserta(last_tag_punto))
    pnt( geom.Pos3d(abcisa, yUnionLosaInfAlmaIzquierda, zLosaInf) ) )
    nmbListaPuntos(inserta(last_tag_punto))

ladoElemento= 0.8

def defineTramoTablero(listaPuntos1,listaPuntos2,tramo):
    \sup_cuadrilatera
        def_pnts(listaPuntos1[0],listaPuntos2[0],listaPuntos2[1],listaPuntos1[1])
        elemSizesIJ(ladoElemento,ladoElemento) add_labels(["VOL","IZQ",tramo])
    tagsCarasVoladizoIzquierdo(inserta(last_tag_face))

    sup_cuadrilatera( def_pnts(listaPuntos1[1],listaPuntos2[1],listaPuntos2[2],listaPuntos1[2]) elemSizesIJ(ladoElemento,ladoElemento) add_labels(["VIA","IZQ",tramo]) )
    tagsCarasLosaViaIzquierda(inserta(last_tag_face))
    sup_cuadrilatera( def_pnts(listaPuntos1[2],listaPuntos2[2],listaPuntos2[3],listaPuntos1[3]) elemSizesIJ(ladoElemento,ladoElemento) add_labels(["VIA","IZQ",tramo]) )
    tagsCarasLosaViaIzquierda(inserta(last_tag_face))
    sup_cuadrilatera( def_pnts(listaPuntos1[3],listaPuntos2[3],listaPuntos2[4],listaPuntos1[4]) elemSizesIJ(ladoElemento,ladoElemento) add_labels(["VIA","IZQ",tramo]) )
    tagsCarasLosaViaIzquierda(inserta(last_tag_face))

    sup_cuadrilatera( def_pnts(listaPuntos1[4],listaPuntos2[4],listaPuntos2[5],listaPuntos1[5]) elemSizesIJ(ladoElemento,ladoElemento) add_labels(["VIA","DCH",tramo]) )
    tagsCarasLosaViaDerecha(inserta(last_tag_face))
    sup_cuadrilatera( def_pnts(listaPuntos1[5],listaPuntos2[5],listaPuntos2[6],listaPuntos1[6]) elemSizesIJ(ladoElemento,ladoElemento) add_labels(["VIA","DCH",tramo]) )
    tagsCarasLosaViaDerecha(inserta(last_tag_face))
    sup_cuadrilatera( def_pnts(listaPuntos1[6],listaPuntos2[6],listaPuntos2[7],listaPuntos1[7]) elemSizesIJ(ladoElemento,ladoElemento) add_labels(["VIA","DCH",tramo]) )
    tagsCarasLosaViaDerecha(inserta(last_tag_face))

    sup_cuadrilatera( def_pnts(listaPuntos1[7],listaPuntos2[7],listaPuntos2[8],listaPuntos1[8]) elemSizesIJ(ladoElemento,ladoElemento) add_labels(["VOL","DCH",tramo]) )
    tagsCarasVoladizoDerecho(inserta(last_tag_face))

    sup_cuadrilatera( def_pnts(listaPuntos1[1],listaPuntos2[1],listaPuntos2[9],listaPuntos1[9]) elemSizesIJ(ladoElemento,ladoElemento) add_labels(["ALM","IZQ",tramo]) )
    tagsCarasAlmaIzquierda(inserta(last_tag_face))

    sup_cuadrilatera( def_pnts(listaPuntos1[9],listaPuntos2[9],listaPuntos2[10],listaPuntos1[10]) elemSizesIJ(ladoElemento,ladoElemento) add_labels(["LINF","IZQ",tramo]) )
    tagsCarasLosaInfIzquierda(inserta(last_tag_face))
    sup_cuadrilatera( def_pnts(listaPuntos1[10],listaPuntos2[10],listaPuntos2[11],listaPuntos1[11]) elemSizesIJ(ladoElemento,ladoElemento) add_labels(["LINF","IZQ",tramo]) )
    tagsCarasLosaInfIzquierda(inserta(last_tag_face))
    sup_cuadrilatera( def_pnts(listaPuntos1[11],listaPuntos2[11],listaPuntos2[12],listaPuntos1[12]) elemSizesIJ(ladoElemento,ladoElemento) add_labels(["LINF","IZQ",tramo]) )
    tagsCarasLosaInfIzquierda(inserta(last_tag_face))

    sup_cuadrilatera( def_pnts(listaPuntos1[12],listaPuntos2[12],listaPuntos2[13],listaPuntos1[13]) elemSizesIJ(ladoElemento,ladoElemento) add_labels(["LINF","DCH",tramo]) )
    tagsCarasLosaInfDerecha(inserta(last_tag_face))
    sup_cuadrilatera( def_pnts(listaPuntos1[13],listaPuntos2[13],listaPuntos2[14],listaPuntos1[14]) elemSizesIJ(ladoElemento,ladoElemento) add_labels(["LINF","DCH",tramo]) )
    tagsCarasLosaInfDerecha(inserta(last_tag_face))
    sup_cuadrilatera( def_pnts(listaPuntos1[14],listaPuntos2[14],listaPuntos2[15],listaPuntos1[15]) elemSizesIJ(ladoElemento,ladoElemento) add_labels(["LINF","DCH",tramo]) )
    tagsCarasLosaInfDerecha(inserta(last_tag_face))

    sup_cuadrilatera( def_pnts(listaPuntos1[15],listaPuntos2[15],listaPuntos2[7],listaPuntos1[7]) elemSizesIJ(ladoElemento,ladoElemento) add_labels(["ALM","DCH",tramo]) )
    tagsCarasAlmaDerecha(inserta(last_tag_face))

\mdlr
    \cad
        tag_punto(1)
        abcisaSeccion= 0
        defineSeccion(abcisaSeccion,"puntosA")

        abcisaSeccion= abcisaSeccion+LTramo0
        defineSeccion(abcisaSeccion,"puntosB")

        abcisaSeccion= abcisaSeccion+LTramo1
        defineSeccion(abcisaSeccion,"puntosI1")

        abcisaSeccion= abcisaSeccion+LTramo2
        defineSeccion(abcisaSeccion,"puntosI2")

        abcisaSeccion= abcisaSeccion+LTramo3
        defineSeccion(abcisaSeccion,"puntosI3")

        abcisaSeccion= abcisaSeccion+LTramo2
        defineSeccion(abcisaSeccion,"puntosI4")

        abcisaSeccion= abcisaSeccion+LTramo1
        defineSeccion(abcisaSeccion,"puntosC")


        abcisaSeccion= abcisaSeccion+LTramo0
        defineSeccion(abcisaSeccion,"puntosD")


        \defineTramoTablero(puntosA,puntosB,idTramo0)
        \defineTramoTablero(puntosB,puntosI1,idTramo1)
        \defineTramoTablero(puntosI1,puntosI2,idTramo2)
        \defineTramoTablero(puntosI2,puntosI3,idTramo3)
        \defineTramoTablero(puntosI3,puntosI4,idTramo4)
        \defineTramoTablero(puntosI4,puntosC,idTramo5)
        \defineTramoTablero(puntosC,puntosD,idTramo6)


        # Alma central
        sup_cuadrilatera( def_pnts(puntosB[12],puntosI1[12],puntosI1[4],puntosB[4]) elemSizesIJ(ladoElemento,ladoElemento) add_labels(["ALM","CEN",idTramo1]) )
        tagsCarasAlmaCentral(inserta(last_tag_face))
        sup_cuadrilatera( def_pnts(puntosI1[12],puntosI2[12],puntosI2[4],puntosI1[4]) elemSizesIJ(ladoElemento,ladoElemento) add_labels(["ALM","CEN",idTramo2]) )
        tagsCarasAlmaCentral(inserta(last_tag_face))
        sup_cuadrilatera( def_pnts(puntosI2[12],puntosI3[12],puntosI3[4],puntosI2[4]) elemSizesIJ(ladoElemento,ladoElemento)  add_labels(["ALM","CEN",idTramo3]))
        tagsCarasAlmaCentral(inserta(last_tag_face))
        sup_cuadrilatera( def_pnts(puntosI3[12],puntosI4[12],puntosI4[4],puntosI3[4]) elemSizesIJ(ladoElemento,ladoElemento)  add_labels(["ALM","CEN",idTramo4]))
        tagsCarasAlmaCentral(inserta(last_tag_face))
        sup_cuadrilatera( def_pnts(puntosI4[12],puntosC[12],puntosC[4],puntosI4[4]) elemSizesIJ(ladoElemento,ladoElemento)  add_labels(["ALM","CEN",idTramo5]))
        tagsCarasAlmaCentral(inserta(last_tag_face))

        # Diafragmas
        sup_cuadrilatera( def_pnts(puntosB[1],puntosB[2],puntosB[10],puntosB[9]) elemSizesIJ(ladoElemento,ladoElemento) add_labels(["DFG","DRS"]))
        tagsCarasDiafragmaDorsal(inserta(last_tag_face))
        sup_cuadrilatera( def_pnts(puntosB[2],puntosB[10],puntosB[11],puntosB[3]) elemSizesIJ(ladoElemento,ladoElemento) add_labels(["DFG","DRS"]) )
        tagsCarasDiafragmaDorsal(inserta(last_tag_face))
        sup_cuadrilatera( def_pnts(puntosB[3],puntosB[11],puntosB[12],puntosB[4]) elemSizesIJ(ladoElemento,ladoElemento) add_labels(["DFG","DRS"]) )
        tagsCarasDiafragmaDorsal(inserta(last_tag_face))

        sup_cuadrilatera( def_pnts(puntosB[4],puntosB[12],puntosB[13],puntosB[5]) elemSizesIJ(ladoElemento,ladoElemento) add_labels(["DFG","DRS"]) )
        tagsCarasDiafragmaDorsal(inserta(last_tag_face))
        sup_cuadrilatera( def_pnts(puntosB[5],puntosB[13],puntosB[14],puntosB[6]) elemSizesIJ(ladoElemento,ladoElemento) add_labels(["DFG","DRS"]) )
        tagsCarasDiafragmaDorsal(inserta(last_tag_face))
        sup_cuadrilatera( def_pnts(puntosB[6],puntosB[14],puntosB[15],puntosB[7]) elemSizesIJ(ladoElemento,ladoElemento) add_labels(["DFG","DRS"]) )
        tagsCarasDiafragmaDorsal(inserta(last_tag_face))

        sup_cuadrilatera( def_pnts(puntosC[1],puntosC[2],puntosC[10],puntosC[9]) elemSizesIJ(ladoElemento,ladoElemento) add_labels(["DFG","FRN"]) )
        tagsCarasDiafragmaFrontal(inserta(last_tag_face))
        sup_cuadrilatera( def_pnts(puntosC[2],puntosC[10],puntosC[11],puntosC[3]) elemSizesIJ(ladoElemento,ladoElemento) add_labels(["DFG","FRN"]) )
        tagsCarasDiafragmaFrontal(inserta(last_tag_face))
        sup_cuadrilatera( def_pnts(puntosC[3],puntosC[11],puntosC[12],puntosC[4]) elemSizesIJ(ladoElemento,ladoElemento) add_labels(["DFG","FRN"]) )
        tagsCarasDiafragmaFrontal(inserta(last_tag_face))

        sup_cuadrilatera( def_pnts(puntosC[4],puntosC[12],puntosC[13],puntosC[5]) elemSizesIJ(ladoElemento,ladoElemento) add_labels(["DFG","FRN"]) )
        tagsCarasDiafragmaFrontal(inserta(last_tag_face))
        sup_cuadrilatera( def_pnts(puntosC[5],puntosC[13],puntosC[14],puntosC[6]) elemSizesIJ(ladoElemento,ladoElemento) add_labels(["DFG","FRN"]) )
        tagsCarasDiafragmaFrontal(inserta(last_tag_face))
        sup_cuadrilatera( def_pnts(puntosC[6],puntosC[14],puntosC[15],puntosC[7]) elemSizesIJ(ladoElemento,ladoElemento) add_labels(["DFG","FRN"]) )
        tagsCarasDiafragmaFrontal(inserta(last_tag_face))
puntoApoyoDorsalDerecho= puntosB[10]
puntoApoyoDorsalIzquierdo= puntosB[14]
puntoApoyoFrontalDerecho= puntosC[10]
puntoApoyoFrontalIzquierdo= puntosC[14]

cooPuntoFijoFrontalIzquierdo= 
cooPuntoFijoFrontalDerecho= 
\mdlr{\cad
    \pnt[puntoApoyoFrontalDerecho]
      { cooPuntoFijoFrontalDerecho= pos }
    \pnt[puntoApoyoFrontalIzquierdo]
      { cooPuntoFijoFrontalIzquierdo= pos }
  }}

cooPuntoFijoFrontalDerecho( z(z+2))
cooPuntoFijoFrontalIzquierdo( z(z+2))
'''
print("punto fijo dcho.",cooPuntoFijoFrontalDerecho,"\n")
print("punto fijo izq.",cooPuntoFijoFrontalIzquierdo,"\n")
'''

