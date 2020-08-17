# -*- coding: utf-8
''' Bridge deck geometry.'''
import xc_base
import geom



def defineSeccion(preprocessor, abcisa, deckGeometry):
    points= preprocessor.getMultiBlockTopology.getPoints
    pointList= list()
    pointList.append(points.newPntFromPos3d( geom.Pos3d(abcisa, -7, deckGeometry.zExtremoAlas)))
    pointList.append(points.newPntFromPos3d( geom.Pos3d(abcisa, deckGeometry.yUnionLosaSupAlmaDerecha, deckGeometry.zUnionLosaSupAlmaDerecha))) 
    pointList.append(points.newPntFromPos3d( geom.Pos3d(abcisa, deckGeometry.yVia1CD, deckGeometry.zVia1CD)))
    pointList.append(points.newPntFromPos3d( geom.Pos3d(abcisa, deckGeometry.yVia1CI, deckGeometry.zVia1CI))) 
    pointList.append(points.newPntFromPos3d( geom.Pos3d(abcisa, 0, deckGeometry.zUnionLosaSupAlmaCentral)))
    pointList.append(points.newPntFromPos3d( geom.Pos3d(abcisa, deckGeometry.yVia2CD, deckGeometry.zVia2CD)))
    pointList.append(points.newPntFromPos3d( geom.Pos3d(abcisa, deckGeometry.yVia2CI, deckGeometry.zVia2CI)))
    pointList.append(points.newPntFromPos3d( geom.Pos3d(abcisa, deckGeometry.yUnionLosaSupAlmaIzquierda, deckGeometry.zUnionLosaSupAlmaIzquierda)))
    pointList.append(points.newPntFromPos3d( geom.Pos3d(abcisa, 7, deckGeometry.zExtremoAlas)))
    pointList.append(points.newPntFromPos3d( geom.Pos3d(abcisa, deckGeometry.yUnionLosaInfAlmaDerecha, deckGeometry.zLosaInf)))
    pointList.append(points.newPntFromPos3d( geom.Pos3d(abcisa, -1.575, deckGeometry.zLosaInf)))
    pointList.append(points.newPntFromPos3d( geom.Pos3d(abcisa, -0.7875, deckGeometry.zLosaInf)))
    pointList.append(points.newPntFromPos3d( geom.Pos3d(abcisa, 0, deckGeometry.zLosaInf)))
    pointList.append(points.newPntFromPos3d( geom.Pos3d(abcisa, 0.7875, deckGeometry.zLosaInf)))
    pointList.append(points.newPntFromPos3d( geom.Pos3d(abcisa, 1.575, deckGeometry.zLosaInf)))
    pointList.append(points.newPntFromPos3d( geom.Pos3d(abcisa, deckGeometry.yUnionLosaInfAlmaIzquierda, deckGeometry.zLosaInf)))
    return pointList

def defineTramoTablero(preprocessor, listaPuntos1,listaPuntos2,idTramo):
    surfaces= preprocessor.getMultiBlockTopology.getSurfaces

    s= surfaces.newQuadSurfacePts(listaPuntos1[0].tag,listaPuntos2[0].tag,listaPuntos2[1].tag,listaPuntos1[1].tag)
    s.setElemSizeIJ(ladoElemento,ladoElemento)
    s.setProp("labels",["VOL","IZQ",idTramo])
    tagsCarasVoladizoIzquierdo(inserta(last_tag_face))

    s= surfaces.newQuadSurfacePts(listaPuntos1[1].tag,listaPuntos2[1].tag,listaPuntos2[2].tag,listaPuntos1[2].tag)
    s.setElemSizeIJ(ladoElemento,ladoElemento)
    s.setProp("labels",["VIA","IZQ",idTramo])
    tagsCarasLosaViaIzquierda(inserta(last_tag_face))
    s= surfaces.newQuadSurfacePts(listaPuntos1[2].tag,listaPuntos2[2].tag,listaPuntos2[3].tag,listaPuntos1[3].tag)
    s.setElemSizeIJ(ladoElemento,ladoElemento)
    s.setProp("labels",["VIA","IZQ",idTramo])
    tagsCarasLosaViaIzquierda(inserta(last_tag_face))
    s= surfaces.newQuadSurfacePts(listaPuntos1[3].tag,listaPuntos2[3].tag,listaPuntos2[4].tag,listaPuntos1[4].tag)
    s.setElemSizeIJ(ladoElemento,ladoElemento)
    s.setProp("labels",["VIA","IZQ",idTramo])
    tagsCarasLosaViaIzquierda(inserta(last_tag_face))

    s= surfaces.newQuadSurfacePts(listaPuntos1[4].tag,listaPuntos2[4].tag,listaPuntos2[5].tag,listaPuntos1[5].tag)
    s.setElemSizeIJ(ladoElemento,ladoElemento)
    s.setProp("labels",["VIA","DCH",idTramo])
    tagsCarasLosaViaDerecha(inserta(last_tag_face))
    s= surfaces.newQuadSurfacePts(listaPuntos1[5].tag,listaPuntos2[5].tag,listaPuntos2[6].tag,listaPuntos1[6].tag)
    s.setElemSizeIJ(ladoElemento,ladoElemento)
    s.setProp("labels",["VIA","DCH",idTramo])
    tagsCarasLosaViaDerecha(inserta(last_tag_face))
    s= surfaces.newQuadSurfacePts(listaPuntos1[6].tag,listaPuntos2[6].tag,listaPuntos2[7].tag,listaPuntos1[7].tag)
    s.setElemSizeIJ(ladoElemento,ladoElemento)
    s.setProp("labels",["VIA","DCH",idTramo])
    tagsCarasLosaViaDerecha(inserta(last_tag_face))

    s= surfaces.newQuadSurfacePts(listaPuntos1[7].tag,listaPuntos2[7].tag,listaPuntos2[8].tag,listaPuntos1[8].tag)
    s.setElemSizeIJ(ladoElemento,ladoElemento)
    s.setProp("labels",["VOL","DCH",idTramo])
    tagsCarasVoladizoDerecho(inserta(last_tag_face))

    s= surfaces.newQuadSurfacePts(listaPuntos1[1].tag,listaPuntos2[1].tag,listaPuntos2[9].tag,listaPuntos1[9].tag)
    s.setElemSizeIJ(ladoElemento,ladoElemento)
    s.setProp("labels",["ALM","IZQ",idTramo])
    tagsCarasAlmaIzquierda(inserta(last_tag_face))

    s= surfaces.newQuadSurfacePts(listaPuntos1[9].tag,listaPuntos2[9].tag,listaPuntos2[10].tag,listaPuntos1[10].tag)
    s.setElemSizeIJ(ladoElemento,ladoElemento)
    s.setProp("labels",["LINF","IZQ",idTramo])
    tagsCarasLosaInfIzquierda(inserta(last_tag_face))
    s= surfaces.newQuadSurfacePts(listaPuntos1[10].tag,listaPuntos2[10].tag,listaPuntos2[11].tag,listaPuntos1[11].tag)
    s.setElemSizeIJ(ladoElemento,ladoElemento)
    s.setProp("labels",["LINF","IZQ",idTramo])
    tagsCarasLosaInfIzquierda(inserta(last_tag_face))
    s= surfaces.newQuadSurfacePts(listaPuntos1[11].tag,listaPuntos2[11].tag,listaPuntos2[12].tag,listaPuntos1[12].tag)
    s.setElemSizeIJ(ladoElemento,ladoElemento)
    s.setProp("labels",["LINF","IZQ",idTramo])
    tagsCarasLosaInfIzquierda(inserta(last_tag_face))

    s= surfaces.newQuadSurfacePts(listaPuntos1[12].tag,listaPuntos2[12].tag,listaPuntos2[13].tag,listaPuntos1[13].tag)
    s.setElemSizeIJ(ladoElemento,ladoElemento)
    s.setProp("labels",["LINF","DCH",idTramo])
    tagsCarasLosaInfDerecha(inserta(last_tag_face))
    s= surfaces.newQuadSurfacePts(listaPuntos1[13].tag,listaPuntos2[13].tag,listaPuntos2[14].tag,listaPuntos1[14].tag)
    s.setElemSizeIJ(ladoElemento,ladoElemento)
    s.setProp("labels",["LINF","DCH",idTramo])
    tagsCarasLosaInfDerecha(inserta(last_tag_face))
    s= surfaces.newQuadSurfacePts(listaPuntos1[14].tag,listaPuntos2[14].tag,listaPuntos2[15].tag,listaPuntos1[15].tag)
    s.setElemSizeIJ(ladoElemento,ladoElemento)
    s.setProp("labels",["LINF","DCH",idTramo])
    tagsCarasLosaInfDerecha(inserta(last_tag_face))

    s= surfaces.newQuadSurfacePts(listaPuntos1[15].tag,listaPuntos2[15].tag,listaPuntos2[7].tag,listaPuntos1[7].tag)
    s.setElemSizeIJ(ladoElemento,ladoElemento)
    s.setProp("labels",["ALM","DCH",idTramo])
    tagsCarasAlmaDerecha(inserta(last_tag_face))
