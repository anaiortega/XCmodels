xEjesTraseros11= LTramo0+0.15+1.40
xEjesTraseros12= xEjesTraseros11+1.40
xEjesIntermedios1= xEjesTraseros12+4.1
xEjesDelanteros1= xEjesIntermedios1+3.6

xEjesTraseros21= xEjesDelanteros1+1.4+1+1.40
xEjesTraseros22= xEjesTraseros21+1.40
xEjesIntermedios2= xEjesTraseros22+4.1
xEjesDelanteros2= xEjesIntermedios2+3.6

xEjesTraseros31= xEjesDelanteros1+1.4+1+1.40
xEjesTraseros32= xEjesTraseros31+1.40
xEjesIntermedios3= xEjesTraseros32+4.1
xEjesDelanteros3= xEjesIntermedios3+3.6

yRuedasA= -2.5/2-1-2.5+0.25
yRuedasB= yRuedasA+2.5-0.25
yRuedasC= yRuedasB+1.5
yRuedasD= yRuedasC+2.5-0.25
yRuedasE= yRuedasD+1.5
yRuedasF= yRuedasE+2.5-0.25

# Ejes traseros
tagsNodosRuedasTraseras= 
tagsNodosRuedasIntermedias= 
tagsNodosRuedasDelanteras= 

\mdlr{\sets
    \setLosaSup
        \tagsNodosRuedasTraseras
          {
            inserta(getTagNearestNode(xEjesTraseros11,yRuedasA,1.4))
            inserta(getTagNearestNode(xEjesTraseros11,yRuedasB,1.4))
            inserta(getTagNearestNode(xEjesTraseros11,yRuedasC,1.4))
            inserta(getTagNearestNode(xEjesTraseros11,yRuedasD,1.4))
            inserta(getTagNearestNode(xEjesTraseros11,yRuedasE,1.4))
            inserta(getTagNearestNode(xEjesTraseros11,yRuedasF,1.4))

            inserta(getTagNearestNode(xEjesTraseros12,yRuedasA,1.4))
            inserta(getTagNearestNode(xEjesTraseros12,yRuedasB,1.4))
            inserta(getTagNearestNode(xEjesTraseros12,yRuedasC,1.4))
            inserta(getTagNearestNode(xEjesTraseros12,yRuedasD,1.4))
            inserta(getTagNearestNode(xEjesTraseros12,yRuedasE,1.4))
            inserta(getTagNearestNode(xEjesTraseros12,yRuedasF,1.4))

            inserta(getTagNearestNode(xEjesTraseros21,yRuedasA,1.4))
            inserta(getTagNearestNode(xEjesTraseros21,yRuedasB,1.4))
            inserta(getTagNearestNode(xEjesTraseros21,yRuedasC,1.4))
            inserta(getTagNearestNode(xEjesTraseros21,yRuedasD,1.4))
            inserta(getTagNearestNode(xEjesTraseros21,yRuedasE,1.4))
            inserta(getTagNearestNode(xEjesTraseros21,yRuedasF,1.4))

            inserta(getTagNearestNode(xEjesTraseros22,yRuedasA,1.4))
            inserta(getTagNearestNode(xEjesTraseros22,yRuedasB,1.4))
            inserta(getTagNearestNode(xEjesTraseros22,yRuedasC,1.4))
            inserta(getTagNearestNode(xEjesTraseros22,yRuedasD,1.4))
            inserta(getTagNearestNode(xEjesTraseros22,yRuedasE,1.4))
            inserta(getTagNearestNode(xEjesTraseros22,yRuedasF,1.4))

            inserta(getTagNearestNode(xEjesTraseros31,yRuedasA,1.4))
            inserta(getTagNearestNode(xEjesTraseros31,yRuedasB,1.4))
            inserta(getTagNearestNode(xEjesTraseros31,yRuedasC,1.4))
            inserta(getTagNearestNode(xEjesTraseros31,yRuedasD,1.4))
            inserta(getTagNearestNode(xEjesTraseros31,yRuedasE,1.4))
            inserta(getTagNearestNode(xEjesTraseros31,yRuedasF,1.4))

            inserta(getTagNearestNode(xEjesTraseros32,yRuedasA,1.4))
            inserta(getTagNearestNode(xEjesTraseros32,yRuedasB,1.4))
            inserta(getTagNearestNode(xEjesTraseros32,yRuedasC,1.4))
            inserta(getTagNearestNode(xEjesTraseros32,yRuedasD,1.4))
            inserta(getTagNearestNode(xEjesTraseros32,yRuedasE,1.4))
            inserta(getTagNearestNode(xEjesTraseros32,yRuedasF,1.4))
          }
        \tagsNodosRuedasIntermedias
          {
            inserta(getTagNearestNode(xEjesIntermedios1,yRuedasA,1.4))
            inserta(getTagNearestNode(xEjesIntermedios1,yRuedasB,1.4))
            inserta(getTagNearestNode(xEjesIntermedios1,yRuedasC,1.4))
            inserta(getTagNearestNode(xEjesIntermedios1,yRuedasD,1.4))
            inserta(getTagNearestNode(xEjesIntermedios1,yRuedasE,1.4))
            inserta(getTagNearestNode(xEjesIntermedios1,yRuedasF,1.4))

            inserta(getTagNearestNode(xEjesIntermedios2,yRuedasA,1.4))
            inserta(getTagNearestNode(xEjesIntermedios2,yRuedasB,1.4))
            inserta(getTagNearestNode(xEjesIntermedios2,yRuedasC,1.4))
            inserta(getTagNearestNode(xEjesIntermedios2,yRuedasD,1.4))
            inserta(getTagNearestNode(xEjesIntermedios2,yRuedasE,1.4))
            inserta(getTagNearestNode(xEjesIntermedios2,yRuedasF,1.4))

            inserta(getTagNearestNode(xEjesIntermedios3,yRuedasA,1.4))
            inserta(getTagNearestNode(xEjesIntermedios3,yRuedasB,1.4))
            inserta(getTagNearestNode(xEjesIntermedios3,yRuedasC,1.4))
            inserta(getTagNearestNode(xEjesIntermedios3,yRuedasD,1.4))
            inserta(getTagNearestNode(xEjesIntermedios3,yRuedasE,1.4))
            inserta(getTagNearestNode(xEjesIntermedios3,yRuedasF,1.4))
          }
        \tagsNodosRuedasDelanteras
          {
            inserta(getTagNearestNode(xEjesDelanteros1,yRuedasA,1.4))
            inserta(getTagNearestNode(xEjesDelanteros1,yRuedasB,1.4))
            inserta(getTagNearestNode(xEjesDelanteros1,yRuedasC,1.4))
            inserta(getTagNearestNode(xEjesDelanteros1,yRuedasD,1.4))
            inserta(getTagNearestNode(xEjesDelanteros1,yRuedasE,1.4))
            inserta(getTagNearestNode(xEjesDelanteros1,yRuedasF,1.4))

            inserta(getTagNearestNode(xEjesDelanteros2,yRuedasA,1.4))
            inserta(getTagNearestNode(xEjesDelanteros2,yRuedasB,1.4))
            inserta(getTagNearestNode(xEjesDelanteros2,yRuedasC,1.4))
            inserta(getTagNearestNode(xEjesDelanteros2,yRuedasD,1.4))
            inserta(getTagNearestNode(xEjesDelanteros2,yRuedasE,1.4))
            inserta(getTagNearestNode(xEjesDelanteros2,yRuedasF,1.4))

            inserta(getTagNearestNode(xEjesDelanteros3,yRuedasA,1.4))
            inserta(getTagNearestNode(xEjesDelanteros3,yRuedasB,1.4))
            inserta(getTagNearestNode(xEjesDelanteros3,yRuedasC,1.4))
            inserta(getTagNearestNode(xEjesDelanteros3,yRuedasD,1.4))
            inserta(getTagNearestNode(xEjesDelanteros3,yRuedasE,1.4))
            inserta(getTagNearestNode(xEjesDelanteros3,yRuedasF,1.4))
          }
  }}
