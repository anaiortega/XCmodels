# -*- coding: utf-8
import math
import deck_geometry

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

class DeckGeometry(object):
    ''' Deck geometry.'''
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

    # Murete guardabalasto. Descarrilo en situación II.
    yMureteCI= 5.15

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

    angAlma= math.atan2(yUnionLosaSupAlmaIzquierda-yUnionLosaInfAlmaIzquierda,zUnionLosaSupAlmaIzquierda-zLosaInf)

    # Centro de la losa inferior
    xCentroLosaInf= LTramo0+LTramo1+LTramo2+LTramo3/2
    yCentroLosaInf= 0.0
    zCentroLosaInf= zLosaInf

dg= DeckGeometry()

# tag_punto(1)
abcisaSeccion= 0
puntosA= deck_geometry.defineSeccion(preprocessor, abcisaSeccion, dg)

abcisaSeccion+=LTramo0
puntosB= deck_geometry.defineSeccion(preprocessor, abcisaSeccion, dg)

abcisaSeccion+=LTramo1
puntosI1= deck_geometry.defineSeccion(preprocessor, abcisaSeccion, dg)

abcisaSeccion+=LTramo2
puntosI2= deck_geometry.defineSeccion(preprocessor, abcisaSeccion, dg)

abcisaSeccion+=LTramo3
puntosI3= deck_geometry.defineSeccion(preprocessor, abcisaSeccion, dg)

abcisaSeccion+=LTramo2
puntosI4= deck_geometry.defineSeccion(preprocessor, abcisaSeccion, dg)

abcisaSeccion+=LTramo1
puntosC= deck_geometry.defineSeccion(preprocessor, abcisaSeccion, dg)


abcisaSeccion+=LTramo0
puntosD= deck_geometry.defineSeccion(preprocessor, abcisaSeccion, dg)


deck_geometry.defineTramoTablero(preprocessor, puntosA,puntosB,idTramo0)
deck_geometry.defineTramoTablero(preprocessor, puntosB,puntosI1,idTramo1)
deck_geometry.defineTramoTablero(preprocessor, puntosI1,puntosI2,idTramo2)
deck_geometry.defineTramoTablero(preprocessor, puntosI2,puntosI3,idTramo3)
deck_geometry.defineTramoTablero(preprocessor, puntosI3,puntosI4,idTramo4)
deck_geometry.defineTramoTablero(preprocessor, puntosI4,puntosC,idTramo5)
deck_geometry.defineTramoTablero(preprocessor, puntosC,puntosD,idTramo6)


# Alma central
s= surfaces.newQuadSurfacePts(puntosB[12],puntosI1[12],puntosI1[4],puntosB[4])
s.setElemSizeIJ(ladoElemento,ladoElemento)
s.setProp("labels",["ALM","CEN",idTramo1])
tagsCarasAlmaCentral(inserta(last_tag_face))
s= surfaces.newQuadSurfacePts(puntosI1[12],puntosI2[12],puntosI2[4],puntosI1[4])
s.setElemSizeIJ(ladoElemento,ladoElemento)
s.setProp("labels",["ALM","CEN",idTramo2])
tagsCarasAlmaCentral(inserta(last_tag_face))
s= surfaces.newQuadSurfacePts(puntosI2[12],puntosI3[12],puntosI3[4],puntosI2[4])
s.setElemSizeIJ(ladoElemento,ladoElemento)
s.setProp("labels",["ALM","CEN",idTramo3])
tagsCarasAlmaCentral(inserta(last_tag_face))
s= surfaces.newQuadSurfacePts(puntosI3[12],puntosI4[12],puntosI4[4],puntosI3[4])
s.setElemSizeIJ(ladoElemento,ladoElemento)
s.setProp("labels",["ALM","CEN",idTramo4])
tagsCarasAlmaCentral(inserta(last_tag_face))
s= surfaces.newQuadSurfacePts(puntosI4[12],puntosC[12],puntosC[4],puntosI4[4])
s.setElemSizeIJ(ladoElemento,ladoElemento)
s.setProp("labels",["ALM","CEN",idTramo5])
tagsCarasAlmaCentral(inserta(last_tag_face))

# Diafragmas
s= surfaces.newQuadSurfacePts(puntosB[1],puntosB[2],puntosB[10],puntosB[9])
s.setElemSizeIJ(ladoElemento,ladoElemento)
s.setProp("labels",["DFG","DRS"])
tagsCarasDiafragmaDorsal(inserta(last_tag_face))
s= surfaces.newQuadSurfacePts(puntosB[2],puntosB[10],puntosB[11],puntosB[3])
s.setElemSizeIJ(ladoElemento,ladoElemento)
s.setProp("labels",["DFG","DRS"])
tagsCarasDiafragmaDorsal(inserta(last_tag_face))
s= surfaces.newQuadSurfacePts(puntosB[3],puntosB[11],puntosB[12],puntosB[4])
s.setElemSizeIJ(ladoElemento,ladoElemento)
s.setProp("labels",["DFG","DRS"])
tagsCarasDiafragmaDorsal(inserta(last_tag_face))

s= surfaces.newQuadSurfacePts(puntosB[4],puntosB[12],puntosB[13],puntosB[5])
s.setElemSizeIJ(ladoElemento,ladoElemento)
s.setProp("labels",["DFG","DRS"])
tagsCarasDiafragmaDorsal(inserta(last_tag_face))
s= surfaces.newQuadSurfacePts(puntosB[5],puntosB[13],puntosB[14],puntosB[6])
s.setElemSizeIJ(ladoElemento,ladoElemento)
s.setProp("labels",["DFG","DRS"])
tagsCarasDiafragmaDorsal(inserta(last_tag_face))
s= surfaces.newQuadSurfacePts(puntosB[6],puntosB[14],puntosB[15],puntosB[7])
s.setElemSizeIJ(ladoElemento,ladoElemento)
s.setProp("labels",["DFG","DRS"])
tagsCarasDiafragmaDorsal(inserta(last_tag_face))

s= surfaces.newQuadSurfacePts(puntosC[1],puntosC[2],puntosC[10],puntosC[9])
s.setElemSizeIJ(ladoElemento,ladoElemento)
s.setProp("labels",["DFG","FRN"])
tagsCarasDiafragmaFrontal(inserta(last_tag_face))
s= surfaces.newQuadSurfacePts(puntosC[2],puntosC[10],puntosC[11],puntosC[3])
s.setElemSizeIJ(ladoElemento,ladoElemento)
s.setProp("labels",["DFG","FRN"])
tagsCarasDiafragmaFrontal(inserta(last_tag_face))
s= surfaces.newQuadSurfacePts(puntosC[3],puntosC[11],puntosC[12],puntosC[4])
s.setElemSizeIJ(ladoElemento,ladoElemento)
s.setProp("labels",["DFG","FRN"])
tagsCarasDiafragmaFrontal(inserta(last_tag_face))

s= surfaces.newQuadSurfacePts(puntosC[4],puntosC[12],puntosC[13],puntosC[5])
s.setElemSizeIJ(ladoElemento,ladoElemento)
s.setProp("labels",["DFG","FRN"])
tagsCarasDiafragmaFrontal(inserta(last_tag_face))
s= surfaces.newQuadSurfacePts(puntosC[5],puntosC[13],puntosC[14],puntosC[6])
s.setElemSizeIJ(ladoElemento,ladoElemento)
s.setProp("labels",["DFG","FRN"])
tagsCarasDiafragmaFrontal(inserta(last_tag_face))
s= surfaces.newQuadSurfacePts(puntosC[6],puntosC[14],puntosC[15],puntosC[7])
s.setElemSizeIJ(ladoElemento,ladoElemento)
s.setProp("labels",["DFG","FRN"])
tagsCarasDiafragmaFrontal(inserta(last_tag_face))
puntoApoyoDorsalDerecho= puntosB[10]
puntoApoyoDorsalIzquierdo= puntosB[14]
puntoApoyoFrontalDerecho= puntosC[10]
puntoApoyoFrontalIzquierdo= puntosC[14]

cooPuntoFijoFrontalIzquierdo= puntoApoyoFrontalIzquierdo.getPos3d+geom.Vector3d(0,0,2)
cooPuntoFijoFrontalDerecho= puntoApoyoFrontalDerecho.getPos3d+geom.Vector3d(0,0,2)

print("punto fijo dcho.",cooPuntoFijoFrontalDerecho,"\n")
print("punto fijo izq.",cooPuntoFijoFrontalIzquierdo,"\n")
'''
'''

