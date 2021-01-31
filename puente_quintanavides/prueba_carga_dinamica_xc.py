# -*- coding: utf-8
exec(open('puente_quintanavides_xci.py').read())

xEjes1= LTramo0+9.4+2.535
xEjes2= xEjes1+1.689
xEjes3= xEjes2+2.019
xEjes4= xEjes3+7.514
xEjes5= xEjes3+2.019
xEjes6= xEjes5+1.689

# Ejes traseros
tagsNodosRuedas= []

\mdlr{\sets
    \setLosaSup
        \tagsNodosRuedas
          {
            # Locomotora en via 1
            inserta(getTagNearestNode(xEjes1,yVia1CD,zVia1CD))
            inserta(getTagNearestNode(xEjes1,yVia1CI,zVia1CI))
            inserta(getTagNearestNode(xEjes2,yVia1CD,zVia1CD))
            inserta(getTagNearestNode(xEjes2,yVia1CI,zVia1CI))
            inserta(getTagNearestNode(xEjes3,yVia1CD,zVia1CD))
            inserta(getTagNearestNode(xEjes3,yVia1CI,zVia1CI))
            inserta(getTagNearestNode(xEjes4,yVia1CD,zVia1CD))
            inserta(getTagNearestNode(xEjes4,yVia1CI,zVia1CI))
            inserta(getTagNearestNode(xEjes5,yVia1CD,zVia1CD))
            inserta(getTagNearestNode(xEjes5,yVia1CI,zVia1CI))
            inserta(getTagNearestNode(xEjes6,yVia1CD,zVia1CD))
            inserta(getTagNearestNode(xEjes6,yVia1CI,zVia1CI))

            # Locomotora en via 2
            inserta(getTagNearestNode(xEjes1,yVia2CD,zVia2CD))
            inserta(getTagNearestNode(xEjes1,yVia2CI,zVia2CI))
            inserta(getTagNearestNode(xEjes2,yVia2CD,zVia2CD))
            inserta(getTagNearestNode(xEjes2,yVia2CI,zVia2CI))
            inserta(getTagNearestNode(xEjes3,yVia2CD,zVia2CD))
            inserta(getTagNearestNode(xEjes3,yVia2CI,zVia2CI))
            inserta(getTagNearestNode(xEjes4,yVia2CD,zVia2CD))
            inserta(getTagNearestNode(xEjes4,yVia2CI,zVia2CI))
            inserta(getTagNearestNode(xEjes5,yVia2CD,zVia2CD))
            inserta(getTagNearestNode(xEjes5,yVia2CI,zVia2CI))
            inserta(getTagNearestNode(xEjes6,yVia2CD,zVia2CD))
            inserta(getTagNearestNode(xEjes6,yVia2CI,zVia2CI))
          }
  }}

exec(open('acciones/cargas_prueba_carga_dinamica_xci.py').read())

# Puntos de control
xPControl1= LTramo0+9
xPControl2= xPControl1+10
xPControl3= xPControl2+10

tagsNodosPControl= []
\mdlr{\sets
    \setLosaInf
        \tagsNodosPControl
          {
            inserta(getTagNearestNode(xPControl1,0,zLosaInf))
            inserta(getTagNearestNode(xPControl2,0,zLosaInf))
            inserta(getTagNearestNode(xPControl3,0,zLosaInf))
          }
  }}
def trataResultsComb(nmbComb):
    \listaDesplazamientosNodos(nmbComb,tagsNodosPControl,"%7.2f","flechasPCD","cabecera","tit")

\nuevo_archivo_salida["flechasPCD"]{"flechas_prueba_carga_dinamica.tex"}
\resuelveCombEstatLin("PCD")
\trataResultsComb("PCD")
cierra_archivo_salida("flechasPCD")
