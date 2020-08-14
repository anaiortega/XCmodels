tagNodoCentroLosaInf= 
\mdlr
    \nodos
        ncoo_def(3) # Dimensiones de los nodos
        ngdl_def(6) # Grados de libertad de los nodos
        \nod_semilla[0]{coo(0.0,0.0,0.0)}
    \elementos{\elem_semilla
        nmb_material("hormLosaInf")
        \shell_mitc4[1]{}
      }}

    \sets
        \setLosaInf
          {
            malla()
            fillDownwards()
            tagNodoCentroLosaInf= getTagNearestNode(xCentroLosaInf,yCentroLosaInf,zCentroLosaInf)
          }

    elementos(elem_semilla(nmb_material("hormAlmas30")))
    \sets{\setAlmas30{malla()fillDownwards()} }
    elementos(elem_semilla(nmb_material("hormAlmas27")))
    \sets{\setAlmas27{malla()fillDownwards()} }
    elementos(elem_semilla(nmb_material("hormAlmas22")))
    \sets{\setAlmas22{malla()fillDownwards()} }
    elementos(elem_semilla(nmb_material("hormAlmaC50")))
    \sets{\setAlmasC50{malla()fillDownwards()} }
    elementos(elem_semilla(nmb_material("hormAlmaC40")))
    \sets{\setAlmasC40{malla()fillDownwards()} }

    sets(setAlmas(fillDownwards()) )

    elementos(elem_semilla(nmb_material("hormDiafrag")))
    sets(setDiafragmas(malla()fillDownwards()) )
tagNodoApoyoDorsalDerecho= getTagNodoPunto(puntoApoyoDorsalDerecho)
tagNodoApoyoDorsalIzquierdo= getTagNodoPunto(puntoApoyoDorsalIzquierdo)
tagNodoApoyoFrontalDerecho= getTagNodoPunto(puntoApoyoFrontalDerecho)
tagNodoApoyoFrontalIzquierdo= getTagNodoPunto(puntoApoyoFrontalIzquierdo)

tagsNodosFlecha= [tagNodoCentroLosaInf]
