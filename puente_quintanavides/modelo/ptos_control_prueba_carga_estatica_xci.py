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
