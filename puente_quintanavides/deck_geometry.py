# -*- coding: utf-8
''' Bridge deck geometry.'''
from __future__ import print_function
from __future__ import division


import math
import xc_base
import geom
import xc

from model import predefined_spaces

class DeckGeometry(predefined_spaces.StructuralMechanics3D):
    ''' Deck geometry.'''
    luzVano= 38
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
    
    def __init__(self, nodes):
        ''' Constructor.'''
        super(DeckGeometry,self).__init__(nodes)
        # Centro de la losa inferior
        self.xCentroLosaInf= self.LTramo0+self.LTramo1+self.LTramo2+self.LTramo3/2
        self.yCentroLosaInf= 0.0
        self.zCentroLosaInf= self.zLosaInf
        self.ladoElemento= 0.8
        self.carasVoladizoIzquierdo= list()
        self.carasVoladizoDerecho= list()
        self.carasLosaViaIzquierda= list()
        self.carasLosaViaDerecha= list()
        self.carasAlmaIzquierda= list()
        self.carasAlmaCentral= list()
        self.carasAlmaDerecha= list()
        self.carasLosaInfIzquierda= list()
        self.carasLosaInfDerecha= list()
        self.carasDiafragmaDorsal= list()
        self.carasDiafragmaFrontal= list()

    def defineSeccion(self, abcisa):
        points= self.preprocessor.getMultiBlockTopology.getPoints
        pointList= list()
        pointList.append(points.newPntFromPos3d( geom.Pos3d(abcisa, -7.0, self.zExtremoAlas)))
        pointList.append(points.newPntFromPos3d( geom.Pos3d(abcisa, self.yUnionLosaSupAlmaDerecha, self.zUnionLosaSupAlmaDerecha))) 
        pointList.append(points.newPntFromPos3d( geom.Pos3d(abcisa, self.yVia1CD, self.zVia1CD)))
        pointList.append(points.newPntFromPos3d( geom.Pos3d(abcisa, self.yVia1CI, self.zVia1CI))) 
        pointList.append(points.newPntFromPos3d( geom.Pos3d(abcisa, 0, self.zUnionLosaSupAlmaCentral)))
        pointList.append(points.newPntFromPos3d( geom.Pos3d(abcisa, self.yVia2CD, self.zVia2CD)))
        pointList.append(points.newPntFromPos3d( geom.Pos3d(abcisa, self.yVia2CI, self.zVia2CI)))
        pointList.append(points.newPntFromPos3d( geom.Pos3d(abcisa, self.yUnionLosaSupAlmaIzquierda, self.zUnionLosaSupAlmaIzquierda)))
        pointList.append(points.newPntFromPos3d( geom.Pos3d(abcisa, 7, self.zExtremoAlas)))
        pointList.append(points.newPntFromPos3d( geom.Pos3d(abcisa, self.yUnionLosaInfAlmaDerecha, self.zLosaInf)))
        pointList.append(points.newPntFromPos3d( geom.Pos3d(abcisa, -1.575, self.zLosaInf)))
        pointList.append(points.newPntFromPos3d( geom.Pos3d(abcisa, -0.7875, self.zLosaInf)))
        pointList.append(points.newPntFromPos3d( geom.Pos3d(abcisa, 0, self.zLosaInf)))
        pointList.append(points.newPntFromPos3d( geom.Pos3d(abcisa, 0.7875, self.zLosaInf)))
        pointList.append(points.newPntFromPos3d( geom.Pos3d(abcisa, 1.575, self.zLosaInf)))
        pointList.append(points.newPntFromPos3d( geom.Pos3d(abcisa, self.yUnionLosaInfAlmaIzquierda, self.zLosaInf)))
        return pointList

    def defineSecciones(self):
        # tag_punto(1)
        abcisaSeccion= 0
        self.puntosA= self.defineSeccion(abcisaSeccion)

        abcisaSeccion+= self.LTramo0
        self.puntosB= self.defineSeccion(abcisaSeccion)

        abcisaSeccion+= self.LTramo1
        self.puntosI1= self.defineSeccion(abcisaSeccion)

        abcisaSeccion+= self.LTramo2
        self.puntosI2= self.defineSeccion(abcisaSeccion)

        abcisaSeccion+= self.LTramo3
        self.puntosI3= self.defineSeccion(abcisaSeccion)

        abcisaSeccion+= self.LTramo2
        self.puntosI4= self.defineSeccion(abcisaSeccion)

        abcisaSeccion+= self.LTramo1
        self.puntosC= self.defineSeccion(abcisaSeccion)


        abcisaSeccion+= self.LTramo0
        self.puntosD= self.defineSeccion(abcisaSeccion)

    def getLTot(self):
        return (self.LTramo0+self.LTramo1+self.LTramo2)*2.0+self.LTramo3

    def defineTramoTablero(self, listaPuntos1,listaPuntos2,idTramo):
        surfaces= self.preprocessor.getMultiBlockTopology.getSurfaces

        s= surfaces.newQuadSurfacePts(listaPuntos1[0].tag,listaPuntos2[0].tag,listaPuntos2[1].tag,listaPuntos1[1].tag)
        s.setElemSizeIJ(self.ladoElemento,self.ladoElemento)
        s.setProp("labels",["VOL","IZQ",idTramo])
        self.carasVoladizoIzquierdo.append(s)

        s= surfaces.newQuadSurfacePts(listaPuntos1[1].tag,listaPuntos2[1].tag,listaPuntos2[2].tag,listaPuntos1[2].tag)
        s.setElemSizeIJ(self.ladoElemento,self.ladoElemento)
        s.setProp("labels",["VIA","IZQ",idTramo])
        self.carasLosaViaIzquierda.append(s)
        s= surfaces.newQuadSurfacePts(listaPuntos1[2].tag,listaPuntos2[2].tag,listaPuntos2[3].tag,listaPuntos1[3].tag)
        s.setElemSizeIJ(self.ladoElemento,self.ladoElemento)
        s.setProp("labels",["VIA","IZQ",idTramo])
        self.carasLosaViaIzquierda.append(s)
        s= surfaces.newQuadSurfacePts(listaPuntos1[3].tag,listaPuntos2[3].tag,listaPuntos2[4].tag,listaPuntos1[4].tag)
        s.setElemSizeIJ(self.ladoElemento,self.ladoElemento)
        s.setProp("labels",["VIA","IZQ",idTramo])
        self.carasLosaViaIzquierda.append(s)

        s= surfaces.newQuadSurfacePts(listaPuntos1[4].tag,listaPuntos2[4].tag,listaPuntos2[5].tag,listaPuntos1[5].tag)
        s.setElemSizeIJ(self.ladoElemento,self.ladoElemento)
        s.setProp("labels",["VIA","DCH",idTramo])
        self.carasLosaViaDerecha.append(s)
        s= surfaces.newQuadSurfacePts(listaPuntos1[5].tag,listaPuntos2[5].tag,listaPuntos2[6].tag,listaPuntos1[6].tag)
        s.setElemSizeIJ(self.ladoElemento,self.ladoElemento)
        s.setProp("labels",["VIA","DCH",idTramo])
        self.carasLosaViaDerecha.append(s)
        s= surfaces.newQuadSurfacePts(listaPuntos1[6].tag,listaPuntos2[6].tag,listaPuntos2[7].tag,listaPuntos1[7].tag)
        s.setElemSizeIJ(self.ladoElemento,self.ladoElemento)
        s.setProp("labels",["VIA","DCH",idTramo])
        self.carasLosaViaDerecha.append(s)

        s= surfaces.newQuadSurfacePts(listaPuntos1[7].tag,listaPuntos2[7].tag,listaPuntos2[8].tag,listaPuntos1[8].tag)
        s.setElemSizeIJ(self.ladoElemento,self.ladoElemento)
        s.setProp("labels",["VOL","DCH",idTramo])
        self.carasVoladizoDerecho.append(s)

        s= surfaces.newQuadSurfacePts(listaPuntos1[1].tag,listaPuntos2[1].tag,listaPuntos2[9].tag,listaPuntos1[9].tag)
        s.setElemSizeIJ(self.ladoElemento,self.ladoElemento)
        s.setProp("labels",["ALM","IZQ",idTramo])
        self.carasAlmaIzquierda.append(s)

        s= surfaces.newQuadSurfacePts(listaPuntos1[9].tag,listaPuntos2[9].tag,listaPuntos2[10].tag,listaPuntos1[10].tag)
        s.setElemSizeIJ(self.ladoElemento,self.ladoElemento)
        s.setProp("labels",["LINF","IZQ",idTramo])
        self.carasLosaInfIzquierda.append(s)
        s= surfaces.newQuadSurfacePts(listaPuntos1[10].tag,listaPuntos2[10].tag,listaPuntos2[11].tag,listaPuntos1[11].tag)
        s.setElemSizeIJ(self.ladoElemento,self.ladoElemento)
        s.setProp("labels",["LINF","IZQ",idTramo])
        self.carasLosaInfIzquierda.append(s)
        s= surfaces.newQuadSurfacePts(listaPuntos1[11].tag,listaPuntos2[11].tag,listaPuntos2[12].tag,listaPuntos1[12].tag)
        s.setElemSizeIJ(self.ladoElemento,self.ladoElemento)
        s.setProp("labels",["LINF","IZQ",idTramo])
        self.carasLosaInfIzquierda.append(s)

        s= surfaces.newQuadSurfacePts(listaPuntos1[12].tag,listaPuntos2[12].tag,listaPuntos2[13].tag,listaPuntos1[13].tag)
        s.setElemSizeIJ(self.ladoElemento,self.ladoElemento)
        s.setProp("labels",["LINF","DCH",idTramo])
        self.carasLosaInfDerecha.append(s)
        s= surfaces.newQuadSurfacePts(listaPuntos1[13].tag,listaPuntos2[13].tag,listaPuntos2[14].tag,listaPuntos1[14].tag)
        s.setElemSizeIJ(self.ladoElemento,self.ladoElemento)
        s.setProp("labels",["LINF","DCH",idTramo])
        self.carasLosaInfDerecha.append(s)
        s= surfaces.newQuadSurfacePts(listaPuntos1[14].tag,listaPuntos2[14].tag,listaPuntos2[15].tag,listaPuntos1[15].tag)
        s.setElemSizeIJ(self.ladoElemento,self.ladoElemento)
        s.setProp("labels",["LINF","DCH",idTramo])
        self.carasLosaInfDerecha.append(s)

        s= surfaces.newQuadSurfacePts(listaPuntos1[15].tag,listaPuntos2[15].tag,listaPuntos2[7].tag,listaPuntos1[7].tag)
        s.setElemSizeIJ(self.ladoElemento,self.ladoElemento)
        s.setProp("labels",["ALM","DCH",idTramo])
        self.carasAlmaDerecha.append(s)

    def defineTramosTablero(self):
        self.defineSecciones()
        self.defineTramoTablero(self.puntosA,self.puntosB,self.idTramo0)
        self.defineTramoTablero(self.puntosB,self.puntosI1,self.idTramo1)
        self.defineTramoTablero(self.puntosI1,self.puntosI2,self.idTramo2)
        self.defineTramoTablero(self.puntosI2,self.puntosI3,self.idTramo3)
        self.defineTramoTablero(self.puntosI3,self.puntosI4,self.idTramo4)
        self.defineTramoTablero(self.puntosI4,self.puntosC,self.idTramo5)
        self.defineTramoTablero(self.puntosC,self.puntosD,self.idTramo6)

    def defineTablero(self):
        self.defineTramosTablero()

        surfaces= self.preprocessor.getMultiBlockTopology.getSurfaces
        # Alma central
        s= surfaces.newQuadSurfacePts(self.puntosB[12].tag,self.puntosI1[12].tag,self.puntosI1[4].tag,self.puntosB[4].tag)
        s.setElemSizeIJ(self.ladoElemento,self.ladoElemento)
        s.setProp("labels",["ALM","CEN",self.idTramo1])
        self.carasAlmaCentral.append(s)
        s= surfaces.newQuadSurfacePts(self.puntosI1[12].tag,self.puntosI2[12].tag,self.puntosI2[4].tag,self.puntosI1[4].tag)
        s.setElemSizeIJ(self.ladoElemento,self.ladoElemento)
        s.setProp("labels",["ALM","CEN",self.idTramo2])
        self.carasAlmaCentral.append(s)
        s= surfaces.newQuadSurfacePts(self.puntosI2[12].tag,self.puntosI3[12].tag,self.puntosI3[4].tag,self.puntosI2[4].tag)
        s.setElemSizeIJ(self.ladoElemento,self.ladoElemento)
        s.setProp("labels",["ALM","CEN",self.idTramo3])
        self.carasAlmaCentral.append(s)
        s= surfaces.newQuadSurfacePts(self.puntosI3[12].tag,self.puntosI4[12].tag,self.puntosI4[4].tag,self.puntosI3[4].tag)
        s.setElemSizeIJ(self.ladoElemento,self.ladoElemento)
        s.setProp("labels",["ALM","CEN",self.idTramo4])
        self.carasAlmaCentral.append(s)
        s= surfaces.newQuadSurfacePts(self.puntosI4[12].tag,self.puntosC[12].tag,self.puntosC[4].tag,self.puntosI4[4].tag)
        s.setElemSizeIJ(self.ladoElemento,self.ladoElemento)
        s.setProp("labels",["ALM","CEN",self.idTramo5])
        self.carasAlmaCentral.append(s)

        # Diafragmas
        s= surfaces.newQuadSurfacePts(self.puntosB[1].tag,self.puntosB[2].tag,self.puntosB[10].tag,self.puntosB[9].tag)
        s.setElemSizeIJ(self.ladoElemento,self.ladoElemento)
        s.setProp("labels",["DFG","DRS"])
        self.carasDiafragmaDorsal.append(s)
        s= surfaces.newQuadSurfacePts(self.puntosB[2].tag,self.puntosB[10].tag,self.puntosB[11].tag,self.puntosB[3].tag)
        s.setElemSizeIJ(self.ladoElemento,self.ladoElemento)
        s.setProp("labels",["DFG","DRS"])
        self.carasDiafragmaDorsal.append(s)
        s= surfaces.newQuadSurfacePts(self.puntosB[3].tag,self.puntosB[11].tag,self.puntosB[12].tag,self.puntosB[4].tag)
        s.setElemSizeIJ(self.ladoElemento,self.ladoElemento)
        s.setProp("labels",["DFG","DRS"])
        self.carasDiafragmaDorsal.append(s)

        s= surfaces.newQuadSurfacePts(self.puntosB[4].tag,self.puntosB[12].tag,self.puntosB[13].tag,self.puntosB[5].tag)
        s.setElemSizeIJ(self.ladoElemento,self.ladoElemento)
        s.setProp("labels",["DFG","DRS"])
        self.carasDiafragmaDorsal.append(s)
        s= surfaces.newQuadSurfacePts(self.puntosB[5].tag,self.puntosB[13].tag,self.puntosB[14].tag,self.puntosB[6].tag)
        s.setElemSizeIJ(self.ladoElemento,self.ladoElemento)
        s.setProp("labels",["DFG","DRS"])
        self.carasDiafragmaDorsal.append(s)
        s= surfaces.newQuadSurfacePts(self.puntosB[6].tag,self.puntosB[14].tag,self.puntosB[15].tag,self.puntosB[7].tag)
        s.setElemSizeIJ(self.ladoElemento,self.ladoElemento)
        s.setProp("labels",["DFG","DRS"])
        self.carasDiafragmaDorsal.append(s)

        s= surfaces.newQuadSurfacePts(self.puntosC[1].tag,self.puntosC[2].tag,self.puntosC[10].tag,self.puntosC[9].tag)
        s.setElemSizeIJ(self.ladoElemento,self.ladoElemento)
        s.setProp("labels",["DFG","FRN"])
        self.carasDiafragmaFrontal.append(s)
        s= surfaces.newQuadSurfacePts(self.puntosC[2].tag,self.puntosC[10].tag,self.puntosC[11].tag,self.puntosC[3].tag)
        s.setElemSizeIJ(self.ladoElemento,self.ladoElemento)
        s.setProp("labels",["DFG","FRN"])
        self.carasDiafragmaFrontal.append(s)
        s= surfaces.newQuadSurfacePts(self.puntosC[3].tag,self.puntosC[11].tag,self.puntosC[12].tag,self.puntosC[4].tag)
        s.setElemSizeIJ(self.ladoElemento,self.ladoElemento)
        s.setProp("labels",["DFG","FRN"])
        self.carasDiafragmaFrontal.append(s)

        s= surfaces.newQuadSurfacePts(self.puntosC[4].tag,self.puntosC[12].tag,self.puntosC[13].tag,self.puntosC[5].tag)
        s.setElemSizeIJ(self.ladoElemento,self.ladoElemento)
        s.setProp("labels",["DFG","FRN"])
        self.carasDiafragmaFrontal.append(s)
        s= surfaces.newQuadSurfacePts(self.puntosC[5].tag,self.puntosC[13].tag,self.puntosC[14].tag,self.puntosC[6].tag)
        s.setElemSizeIJ(self.ladoElemento,self.ladoElemento)
        s.setProp("labels",["DFG","FRN"])
        self.carasDiafragmaFrontal.append(s)
        s= surfaces.newQuadSurfacePts(self.puntosC[6].tag,self.puntosC[14].tag,self.puntosC[15].tag,self.puntosC[7].tag)
        s.setElemSizeIJ(self.ladoElemento,self.ladoElemento)
        s.setProp("labels",["DFG","FRN"])
        self.carasDiafragmaFrontal.append(s)
        self.puntoApoyoDorsalDerecho= self.puntosB[10]
        self.puntoApoyoDorsalIzquierdo= self.puntosB[14]
        self.puntoApoyoFrontalDerecho= self.puntosC[10]
        self.puntoApoyoFrontalIzquierdo= self.puntosC[14]

        self.cooPuntoFijoFrontalIzquierdo= self.puntoApoyoFrontalIzquierdo.getPos+geom.Vector3d(0,0,2)
        self.cooPuntoFijoFrontalDerecho= self.puntoApoyoFrontalDerecho.getPos+geom.Vector3d(0,0,2)

        '''
        print("punto fijo dcho.",self.cooPuntoFijoFrontalDerecho,"\n")
        print("punto fijo izq.",self.cooPuntoFijoFrontalIzquierdo,"\n")
        '''

    def selFacesFromList(self,xcSetName, surfList):
        xcSet= self.preprocessor.getSets.defSet(xcSetName)
        for s in surfList:
            xcSet.surfaces.append(s)
        #xcSet.fillDownwards()
        return xcSet

    def selFacesWithLabel(self, xcSetName, labelList, fromSet= None):
        xcSet= self.preprocessor.getSets.defSet(xcSetName)
        if(fromSet):
            surfList= fromSet.surfaces
        else:
            surfList= self.getTotalSet().surfaces
        for s in surfList:
            for lbl in labelList:
                if s.hasProp('labels'):
                    labels= s.getProp('labels')
                    if lbl in labels:
                        xcSet.surfaces.append(s)
        #xcSet.fillDownwards()
        return xcSet

    def defineSets(self):
        self.setVoladizoIzquierdo= self.selFacesFromList('setVoladizoIzquierdo',self.carasVoladizoIzquierdo)
        self.setVoladizoDerecho= self.selFacesFromList('setVoladizoDerecho',self.carasVoladizoDerecho)

        self.setLosaViaIzquierda= self.selFacesFromList('setLosaViaIzquierda',self.carasLosaViaIzquierda)
        self.setLosaViaDerecha= self.selFacesFromList('setLosaViaDerecha',self.carasLosaViaDerecha)

        self.setVoladizos= self.setSum('setVoladizos', [self.setVoladizoIzquierdo, self.setVoladizoDerecho])
        self.setLosasVias= self.setSum('setLosasVias', [self.setLosaViaIzquierda, self.setLosaViaDerecha])
        self.setLosaSup= self.setSum('setLosaSup', [self.setVoladizos, self.setLosasVias])

        self.setAlmaIzquierda= self.selFacesFromList('setAlmaIzquierda',self.carasAlmaIzquierda)
        self.setAlmaCentral= self.selFacesFromList('setAlmaCentral',self.carasAlmaCentral)
        self.setAlmaDerecha= self.selFacesFromList('setAlmaDerecha',self.carasAlmaDerecha)
        self.setAlmasLaterales= self.setSum('setAlmasLaterales',[self.setAlmaIzquierda, self.setAlmaDerecha])
        self.setAlmas= self.setSum('setAlmas',[self.setAlmasLaterales, self.setAlmaCentral])

        self.setLosaInfIzquierda= self.selFacesFromList('setLosaInfIzquierda',self.carasLosaInfIzquierda)
        self.setLosaInfDerecha= self.selFacesFromList('setLosaInfDerecha',self.carasLosaInfDerecha)
        self.setLosaInf= self.setSum('setLosaInf',[self.setLosaInfIzquierda, self.setLosaInfDerecha])

        self.setArtesa= self.setSum('setArtesa',[self.setLosaInf, self.setAlmas])

        self.setDiafragmaDorsal= self.selFacesFromList('setDiafragmaDorsal',self.carasDiafragmaDorsal)
        self.setDiafragmaFrontal= self.selFacesFromList('setDiafragmaFrontal',self.carasDiafragmaFrontal)
        self.setDiafragmas= self.setSum('setDiafragmas',[self.setDiafragmaDorsal, self.setDiafragmaFrontal])


        self.setTramo0= self.selFacesWithLabel('setTramo0', [self.idTramo0])
        self.setTramo1= self.selFacesWithLabel('setTramo1', [self.idTramo1])
        self.setTramo2= self.selFacesWithLabel('setTramo2', [self.idTramo2])
        self.setTramo3= self.selFacesWithLabel('setTramo3', [self.idTramo3])
        self.setTramo4= self.selFacesWithLabel('setTramo4', [self.idTramo4])
        self.setTramo5= self.selFacesWithLabel('setTramo5', [self.idTramo5])
        self.setTramo6= self.selFacesWithLabel('setTramo6', [self.idTramo6])

        self.setAlmas30= self.selFacesWithLabel('setAlmas30', [self.idTramo0, self.idTramo1, self.idTramo5, self.idTramo6])
        self.setAlmas27= self.selFacesWithLabel('setAlmas27', [self.idTramo2, self.idTramo4])
        self.setAlmas22= self.selFacesWithLabel('setAlmas22', [self.idTramo3])
        self.setAlmasC50= self.selFacesWithLabel('setAlmasC50', [self.idTramo1, self.idTramo5])
        self.setAlmasC40= self.selFacesWithLabel('setAlmasC40', [self.idTramo2, self.idTramo3, self.idTramo4])


    def genMesh(self):
        ''' Generate mesh.'''
        seedElemHandler= self.preprocessor.getElementHandler.seedElemHandler
        self.preprocessor.getMultiBlockTopology.getSurfaces.conciliaNDivs()
        seedElemHandler.defaultMaterial= "hormLosaInf"
        elem= seedElemHandler.newElement("ShellMITC4",xc.ID([0,0,0,0]))

        self.setLosaInf.genMesh(xc.meshDir.I)
        self.setLosaInf.fillDownwards()
        nodoCentroLosaInf= self.setLosaInf.getNearestNode(geom.Pos3d(self.xCentroLosaInf, self.yCentroLosaInf, self.zCentroLosaInf))

        seedElemHandler.defaultMaterial= 'hormAlmas30'
        self.setAlmas30.genMesh(xc.meshDir.I)
        self.setAlmas30.fillDownwards()
        seedElemHandler.defaultMaterial= 'hormAlmas27'
        self.setAlmas27.genMesh(xc.meshDir.I)
        self.setAlmas27.fillDownwards()
        seedElemHandler.defaultMaterial= 'hormAlmas22'
        self.setAlmas22.genMesh(xc.meshDir.I)
        self.setAlmas22.fillDownwards()
        seedElemHandler.defaultMaterial= 'hormAlmaC50'
        self.setAlmasC50.genMesh(xc.meshDir.I)
        self.setAlmasC50.fillDownwards()
        seedElemHandler.defaultMaterial= 'hormAlmaC40'
        self.setAlmasC40.genMesh(xc.meshDir.I)
        self.setAlmasC40.fillDownwards()

        self.setAlmas.fillDownwards()

        seedElemHandler.defaultMaterial= 'hormDiafrag'
        self.setDiafragmas.genMesh(xc.meshDir.I)
        self.setDiafragmas.fillDownwards()

        xcTotalSet= self.getTotalSet()
        self.nodoApoyoDorsalDerecho= xcTotalSet.getNearestNode(self.puntoApoyoDorsalDerecho.getPos)
        self.nodoApoyoDorsalIzquierdo= xcTotalSet.getNearestNode(self.puntoApoyoDorsalIzquierdo.getPos)
        self.nodoApoyoFrontalDerecho= xcTotalSet.getNearestNode(self.puntoApoyoFrontalDerecho.getPos)
        self.nodoApoyoFrontalIzquierdo= xcTotalSet.getNearestNode(self.puntoApoyoFrontalIzquierdo.getPos)

        self.tagsNodosFlecha= [nodoCentroLosaInf]

    def setConstraints(self):
        ''' Define constraints.'''
        self.fixNode('FF0_FFF', self.nodoApoyoDorsalDerecho.tag) # PL
        self.fixNode('F00_FFF', self.nodoApoyoDorsalIzquierdo.tag) # PU
        self.fixNode('000_FFF', self.nodoApoyoFrontalDerecho.tag) # PF
        self.fixNode('0F0_FFF', self.nodoApoyoFrontalIzquierdo.tag) # PU

        self.nodosCoartados= [self.nodoApoyoDorsalDerecho, self.nodoApoyoDorsalIzquierdo, self.nodoApoyoFrontalDerecho, self.nodoApoyoFrontalIzquierdo]

    def defineSetNodosTendonInf(self, setName, index):
        ''' Define el conjunto de nodos de un tendón de la losa inferior.'''
        retval= self.preprocessor.getSets.defSet(setName)
        numCordones= [numToronesNodoZona0[index],numToronesNodoZona1[index],numToronesNodoZona2[index],numToronesNodoZona3[index],numToronesNodoZona4[index]]
        tmpNod= list()
        for n in setNodosLosaInf.nodes:
            pos= n.getInitialPos3d
            if(abs(pos.y-coordsYNodosTendon[index])<tol):
                tmpNod.append((n, pos.x))
        tmpNod.sort(key=lambda tup: tup[1])
        for n_y in tmpNod:
            retval.append(n_y[0])
       
    def defineSetNodosTendonSup(self, setName, index, y, z):
        ''' Define el conjunto de nodos de un tendón de la losa inferior.'''
        retval= self.preprocessor.getSets.defSet(setName)
        tmpNod= list()
        for n in setAlmas.nodes:
            pos= n.getInitialPos3d
            if( (abs(pos.y-y)<tol) and (abs(pos.z-z)<tol) ):
                tmpNod.append((n, pos.x))
        tmpNod.sort(key=lambda tup: tup[1])
        for n_y in tmpNod:
            retval.append(n_y[0])
        
    def defineSetsPretensado(self):
        ''' Define conjuntos para introducir el pretensado.'''
        numTotalTorones= 120
        numToronesZona4= numTotalTorones
        numToronesZona3= numToronesZona4-12
        numToronesZona2= numToronesZona3-12
        numToronesZona1= numToronesZona2-12
        numToronesZona0= numToronesZona1-12

        tol= self.ladoElemento/100.0

        xcTotalSet= self.getTotalSet()
        setNodosLosaInf= self.preprocessor.getSets.defSet("setNodosLosaInf")
        for n in xcTotalSet.nodes:
            pos= n.getInitialPos3d
            if(abs(pos.z-self.zLosaInf)<tol):
                setNodosLosaInf.nodes.append(n)

        setNodosLosaInfX0= self.preprocessor.getSets.defSet("setNodosLosaInfX0")
        tmpNod= list()
        for n in setNodosLosaInf.nodes:
            pos= n.getInitialPos3d
            if(abs(pos.x)<tol):
                tmpNod.append((n, pos.y))
        tmpNod.sort(key=lambda tup: tup[1])
        print(tmpNod)
        for n_y in tmpNod:
            setNodosLosaInfX0.nodes.append(n_y[0])
        yAnterior= self.yUnionLosaInfAlmaDerecha
        tmpNodos= list()
        tmpCoords= list()
        tmpAreas= list()
        tmpDists= list()
        for n_x in tmpNod:
            n= n_x[0]
            y= n_x[1]
            tmpNodos.append(n)
            tmpCoords.append(y)
            tmpDists.append(y-yAnterior)
            yAnterior= y
        sz= len(tmpDists)
        print('tmpDists= ', tmpDists)
        dPrev= tmpDists[0]
        for d in tmpDists[1:]:
            tmpAreas.append((dPrev+d)/2.0)
        tmpAreas.append(tmpAreas[0])
        listaNodosTendon= [tmpNodos[1], tmpNodos[2], tmpNodos[3], tmpNodos[4], tmpNodos[5], tmpNodos[6], tmpNodos[8], tmpNodos[9], tmpNodos[10], tmpNodos[11], tmpNodos[12], tmpNodos[13]]

        coordsYNodosTendon= [tmpCoords[1], tmpCoords[2], tmpCoords[3], tmpCoords[4], tmpCoords[5], tmpCoords[6], tmpCoords[8], tmpCoords[9], tmpCoords[10], tmpCoords[11], tmpCoords[12], tmpCoords[13]]

        areaTotal= 0.0
        areasNodosTendon= [tmpAreas[1], tmpAreas[2], tmpAreas[3], tmpAreas[4], tmpAreas[5], tmpAreas[6], tmpAreas[8], tmpAreas[9], tmpAreas[10], tmpAreas[11], tmpAreas[12], tmpAreas[13]]
        areaTotal= sum(areasNodosTendon)

        sz= len(areasNodosTendon)
        for i in range(0,sz):
            numToronesNodoZona4.append((round(areasNodosTendon[i]/areaTotal*numToronesZona4)))
            numToronesNodoZona3.append((round(areasNodosTendon[i]/areaTotal*numToronesZona3)))
            numToronesNodoZona2.append((round(areasNodosTendon[i]/areaTotal*numToronesZona2)))
            numToronesNodoZona1.append((round(areasNodosTendon[i]/areaTotal*numToronesZona1)))
            numToronesNodoZona0.append((round(areasNodosTendon[i]/areaTotal*numToronesZona0)))

        print("numToronesNodoZona4: ",numToronesNodoZona4," sz= ",numToronesNodoZona4.size," error= ",numToronesNodoZona4.sumatorio-numToronesZona4)
        print("numToronesNodoZona3: ",numToronesNodoZona3," sz= ",numToronesNodoZona3.size," error= ",numToronesNodoZona3.sumatorio-numToronesZona3)
        print("numToronesNodoZona2: ",numToronesNodoZona2," sz= ",numToronesNodoZona2.size," error= ",numToronesNodoZona2.sumatorio-numToronesZona2)
        print("numToronesNodoZona1: ",numToronesNodoZona1," sz= ",numToronesNodoZona1.size," error= ",numToronesNodoZona1.sumatorio-numToronesZona1)
        print("numToronesNodoZona0: ",numToronesNodoZona0," sz= ",numToronesNodoZona0.size," error= ",numToronesNodoZona0.sumatorio-numToronesZona0)

        print("listaNodosTendon: ",listaNodosTendon," sz= ",listaNodosTendon.size)
        print("areasNodosTendon: ",areasNodosTendon," sz= ",areasNodosTendon.size)
        '''
        '''

        # Ajustamos valores
        numToronesNodoZona4= [11,12,11,10,8,8,8,8,10,11,12,11]
        numToronesNodoZona3= [11,10,10,9,7,7,7,7,9,10,10,11]
        numToronesNodoZona2= [9,9,9,8,6,7,7,6,8,9,9,9]
        numToronesNodoZona1= [8,8,7,7,6,6,6,6,7,7,8,8]
        numToronesNodoZona0= [7,7,6,6,5,5,5,5,6,6,7,7]

        print("numToronesNodoZona4: ",numToronesNodoZona4," sz= ",numToronesNodoZona4.size," error= ",numToronesNodoZona4.sumatorio-numToronesZona4)
        print("numToronesNodoZona3: ",numToronesNodoZona3," sz= ",numToronesNodoZona3.size," error= ",numToronesNodoZona3.sumatorio-numToronesZona3)
        print("numToronesNodoZona2: ",numToronesNodoZona2," sz= ",numToronesNodoZona2.size," error= ",numToronesNodoZona2.sumatorio-numToronesZona2)
        print("numToronesNodoZona1: ",numToronesNodoZona1," sz= ",numToronesNodoZona1.size," error= ",numToronesNodoZona1.sumatorio-numToronesZona1)
        print("numToronesNodoZona0: ",numToronesNodoZona0," sz= ",numToronesNodoZona0.size," error= ",numToronesNodoZona0.sumatorio-numToronesZona0)
        print("coordsYNodosTendon: ",coordsYNodosTendon," sz= ",coordsYNodosTendon.size)
        '''
        '''

        assert((sum(numToronesNodoZona4)-numToronesZona4)== 0)
        assert((sum(numToronesNodoZona3)-numToronesZona3)== 0)
        assert((sum(numToronesNodoZona2)-numToronesZona2)== 0)
        assert((sum(numToronesNodoZona1)-numToronesZona1)== 0)
        assert((sum(numToronesNodoZona0)-numToronesZona0)== 0)

        setNodosTendon00= self.defineSetNodosTendonInf("setNodosTendon00", 0)
        setNodosTendon01= self.defineSetNodosTendonInf("setNodosTendon01", 1)
        setNodosTendon02= self.defineSetNodosTendonInf("setNodosTendon02", 2)
        setNodosTendon03= self.defineSetNodosTendonInf("setNodosTendon03", 3)
        setNodosTendon04= self.defineSetNodosTendonInf("setNodosTendon04", 4)
        setNodosTendon05= self.defineSetNodosTendonInf("setNodosTendon05", 5)
        setNodosTendon06= self.defineSetNodosTendonInf("setNodosTendon06", 6)
        setNodosTendon07= self.defineSetNodosTendonInf("setNodosTendon07", 7)
        setNodosTendon08= self.defineSetNodosTendonInf("setNodosTendon08", 8)
        setNodosTendon09= self.defineSetNodosTendonInf("setNodosTendon09", 9)
        setNodosTendon10= self.defineSetNodosTendonInf("setNodosTendon10", 0)
        setNodosTendon11= self.defineSetNodosTendonInf("setNodosTendon11", 1)

        setNodosTendonSup01= self.defineSetNodosTendonSup("setNodosTendonSup01", yUnionLosaSupAlmaDerecha, zUnionLosaSupAlmaDerecha)
        setNodosTendonSup02= self.defineSetNodosTendonSup("setNodosTendonSup02", 0.0, zUnionLosaSupAlmaCentral)
        setNodosTendonSup03= self.defineSetNodosTendonSup("setNodosTendonSup03", yUnionLosaSupAlmaIzquierda, zUnionLosaSupAlmaIzquierda)
        print('here')
