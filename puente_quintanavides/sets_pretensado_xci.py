# -*- coding: utf-8
listaNodosTendon= []
coordsYNodosTendon= []
areasNodosTendon= []
numTotalTorones= 108
numToronesZona4= numTotalTorones
numToronesZona3= numToronesZona4-12
numToronesZona2= numToronesZona3-12
numToronesZona1= numToronesZona2-12
numToronesZona0= numToronesZona1-12
numToronesNodoZona0= []
numToronesNodoZona1= []
numToronesNodoZona2= []
numToronesNodoZona3= []
numToronesNodoZona4= []

\mdlr
    tol= ladoElemento/100
    \sets
        \def_set["setNodosLosaInf"]
           {
             sel_nod_cond((abs(coord[2]-zLosaInf)<tol))
           }
        \def_set["setNodosLosaInfX0"]
           {
             \sel_nod_cond["setNodosLosaInf"]{(abs(coord[0])<tol)}
             nodos(sort_on_prop(coord[1]))
             yAnterior= yUnionLosaInfAlmaDerecha
             tmpNodos= 
             tmpCoords= 
             tmpAreas= 
             tmpDists= 
             \nodos{\for_each
                {
                  tmpNodos(inserta(tag))
                  tmpCoords(inserta(coord[1]))
                  tmpDists(inserta(coord[1]-yAnterior))
                  yAnterior= coord[1]
                }}
             sz= tmpDists.size
             i= 0.0
             \for
               {
                 inicio(i=0 ) continua(i<sz-1) incremento(i=i+1)
                 \bucle
                    {
                      tmpAreas(inserta((tmpDists[i]+tmpDists[i+1])/2))
                    }
               }
             tmpAreas(inserta(tmpAreas[0]))

             \listaNodosTendon
               {
                 inserta(tmpNodos[1]) inserta(tmpNodos[2]) inserta(tmpNodos[3])
                 inserta(tmpNodos[4]) inserta(tmpNodos[5]) inserta(tmpNodos[6])
                 inserta(tmpNodos[8]) inserta(tmpNodos[9]) inserta(tmpNodos[10])
                 inserta(tmpNodos[11]) inserta(tmpNodos[12]) inserta(tmpNodos[13])
               }
             \coordsYNodosTendon
               {
                 inserta(tmpCoords[1]) inserta(tmpCoords[2]) inserta(tmpCoords[3])
                 inserta(tmpCoords[4]) inserta(tmpCoords[5]) inserta(tmpCoords[6])
                 inserta(tmpCoords[8]) inserta(tmpCoords[9]) inserta(tmpCoords[10])
                 inserta(tmpCoords[11]) inserta(tmpCoords[12]) inserta(tmpCoords[13])
               }
             areaTotal= 0.0
             \areasNodosTendon
               {
                 inserta(tmpAreas[1]) inserta(tmpAreas[2]) inserta(tmpAreas[3])
                 inserta(tmpAreas[4]) inserta(tmpAreas[5]) inserta(tmpAreas[6])
                 inserta(tmpAreas[8]) inserta(tmpAreas[9]) inserta(tmpAreas[10])
                 inserta(tmpAreas[11]) inserta(tmpAreas[12]) inserta(tmpAreas[13])
                 areaTotal= sumatorio
               }
             sz= areasNodosTendon.size
             i= 0.0
             \for
               {
                 inicio(i=0 ) continua(i<sz) incremento(i=i+1)
                 \bucle
                   {
                     \numToronesNodoZona4{inserta(round(areasNodosTendon[i]/areaTotal*numToronesZona4))}
                     \numToronesNodoZona3{inserta(round(areasNodosTendon[i]/areaTotal*numToronesZona3))}
                     \numToronesNodoZona2{inserta(round(areasNodosTendon[i]/areaTotal*numToronesZona2))}
                     \numToronesNodoZona1{inserta(round(areasNodosTendon[i]/areaTotal*numToronesZona1))}
                     \numToronesNodoZona0{inserta(round(areasNodosTendon[i]/areaTotal*numToronesZona0))}
                   }
               }
          }
'''
    print("numToronesNodoZona4: ",numToronesNodoZona4," sz= ",numToronesNodoZona4.size," error= ",numToronesNodoZona4.sumatorio-numToronesZona4,"\n")
    print("numToronesNodoZona3: ",numToronesNodoZona3," sz= ",numToronesNodoZona3.size," error= ",numToronesNodoZona3.sumatorio-numToronesZona3,"\n")
    print("numToronesNodoZona2: ",numToronesNodoZona2," sz= ",numToronesNodoZona2.size," error= ",numToronesNodoZona2.sumatorio-numToronesZona2,"\n")
    print("numToronesNodoZona1: ",numToronesNodoZona1," sz= ",numToronesNodoZona1.size," error= ",numToronesNodoZona1.sumatorio-numToronesZona1,"\n")
    print("numToronesNodoZona0: ",numToronesNodoZona0," sz= ",numToronesNodoZona0.size," error= ",numToronesNodoZona0.sumatorio-numToronesZona0,"\n")

    print("listaNodosTendon: ",listaNodosTendon," sz= ",listaNodosTendon.size,"\n")
    print("areasNodosTendon: ",areasNodosTendon," sz= ",areasNodosTendon.size,"\n")
'''
    # Ajustamos valores
    \numToronesNodoZona4{clear() from_string(10,11,10,9,7,7,7,7,9,10,11,10)}
    \numToronesNodoZona3{clear() from_string(10,9,9,8,6,6,6,6,8,9,9,10)}
    \numToronesNodoZona2{clear() from_string(8,8,8,7,5,6,6,5,7,8,8,8)}
    \numToronesNodoZona1{clear() from_string(7,7,6,6,5,5,5,5,6,6,7,7)}
    \numToronesNodoZona0{clear() from_string(6,6,5,5,4,4,4,4,5,5,6,6)}

'''
    print("numToronesNodoZona4: ",numToronesNodoZona4," sz= ",numToronesNodoZona4.size," error= ",numToronesNodoZona4.sumatorio-numToronesZona4,"\n")
    print("numToronesNodoZona3: ",numToronesNodoZona3," sz= ",numToronesNodoZona3.size," error= ",numToronesNodoZona3.sumatorio-numToronesZona3,"\n")
    print("numToronesNodoZona2: ",numToronesNodoZona2," sz= ",numToronesNodoZona2.size," error= ",numToronesNodoZona2.sumatorio-numToronesZona2,"\n")
    print("numToronesNodoZona1: ",numToronesNodoZona1," sz= ",numToronesNodoZona1.size," error= ",numToronesNodoZona1.sumatorio-numToronesZona1,"\n")
    print("numToronesNodoZona0: ",numToronesNodoZona0," sz= ",numToronesNodoZona0.size," error= ",numToronesNodoZona0.sumatorio-numToronesZona0,"\n")
    print("coordsYNodosTendon: ",coordsYNodosTendon," sz= ",coordsYNodosTendon.size,"\n")
'''

    assert((numToronesNodoZona4.sumatorio-numToronesZona4)== 0)
    assert((numToronesNodoZona3.sumatorio-numToronesZona3)== 0)
    assert((numToronesNodoZona2.sumatorio-numToronesZona2)== 0)
    assert((numToronesNodoZona1.sumatorio-numToronesZona1)== 0)
    assert((numToronesNodoZona0.sumatorio-numToronesZona0)== 0)
    \sets
        \def_set["setNodosTendon00"]
          {
            numCordones= [numToronesNodoZona0[0],numToronesNodoZona1[0],numToronesNodoZona2[0],numToronesNodoZona3[0],numToronesNodoZona4[0]]
            \sel_nod_cond["setNodosLosaInf"]{(abs(coord[1]-coordsYNodosTendon[0])<tol)}
            nodos(sort_on_prop(coord[0]))
          }
        \def_set["setNodosTendon01"]
          {
            numCordones= [numToronesNodoZona0[1],numToronesNodoZona1[1],numToronesNodoZona2[1],numToronesNodoZona3[1],numToronesNodoZona4[1]]
            \sel_nod_cond["setNodosLosaInf"]{(abs(coord[1]-coordsYNodosTendon[1])<tol)}
            nodos(sort_on_prop(coord[0]))
          }
        \def_set["setNodosTendon02"]
          {
            numCordones= [numToronesNodoZona0[2],numToronesNodoZona1[2],numToronesNodoZona2[2],numToronesNodoZona3[2],numToronesNodoZona4[2]]
            \sel_nod_cond["setNodosLosaInf"]{(abs(coord[1]-coordsYNodosTendon[2])<tol)}
            nodos(sort_on_prop(coord[0]))
          }
        \def_set["setNodosTendon03"]
          {
            numCordones= [numToronesNodoZona0[3],numToronesNodoZona1[3],numToronesNodoZona2[3],numToronesNodoZona3[3],numToronesNodoZona4[3]]
            \sel_nod_cond["setNodosLosaInf"]{(abs(coord[1]-coordsYNodosTendon[3])<tol)}
            nodos(sort_on_prop(coord[0]))
          }
        \def_set["setNodosTendon04"]
          {
            numCordones= [numToronesNodoZona0[4],numToronesNodoZona1[4],numToronesNodoZona2[4],numToronesNodoZona3[4],numToronesNodoZona4[4]]
            \sel_nod_cond["setNodosLosaInf"]{(abs(coord[1]-coordsYNodosTendon[4])<tol)}
            nodos(sort_on_prop(coord[0]))
          }
        \def_set["setNodosTendon05"]
          {
            numCordones= [numToronesNodoZona0[5],numToronesNodoZona1[5],numToronesNodoZona2[5],numToronesNodoZona3[5],numToronesNodoZona4[5]]
            \sel_nod_cond["setNodosLosaInf"]{(abs(coord[1]-coordsYNodosTendon[5])<tol)}
            nodos(sort_on_prop(coord[0]))
          }
        \def_set["setNodosTendon06"]
          {
            numCordones= [numToronesNodoZona0[6],numToronesNodoZona1[6],numToronesNodoZona2[6],numToronesNodoZona3[6],numToronesNodoZona4[6]]
            \sel_nod_cond["setNodosLosaInf"]{(abs(coord[1]-coordsYNodosTendon[6])<tol)}
            nodos(sort_on_prop(coord[0]))
          }
        \def_set["setNodosTendon07"]
          {
            numCordones= [numToronesNodoZona0[7],numToronesNodoZona1[7],numToronesNodoZona2[7],numToronesNodoZona3[7],numToronesNodoZona4[7]]
            \sel_nod_cond["setNodosLosaInf"]{(abs(coord[1]-coordsYNodosTendon[7])<tol)}
            nodos(sort_on_prop(coord[0]))
          }
        \def_set["setNodosTendon08"]
          {
            numCordones= [numToronesNodoZona0[8],numToronesNodoZona1[8],numToronesNodoZona2[8],numToronesNodoZona3[8],numToronesNodoZona4[8]]
            \sel_nod_cond["setNodosLosaInf"]{(abs(coord[1]-coordsYNodosTendon[8])<tol)}
            nodos(sort_on_prop(coord[0]))
          }
        \def_set["setNodosTendon09"]
          {
            numCordones= [numToronesNodoZona0[9],numToronesNodoZona1[9],numToronesNodoZona2[9],numToronesNodoZona3[9],numToronesNodoZona4[9]]
            \sel_nod_cond["setNodosLosaInf"]{(abs(coord[1]-coordsYNodosTendon[9])<tol)}
            nodos(sort_on_prop(coord[0]))
          }
        \def_set["setNodosTendon10"]
          {
            numCordones= [numToronesNodoZona0[10],numToronesNodoZona1[10],numToronesNodoZona2[10],numToronesNodoZona3[10],numToronesNodoZona4[10]]
            \sel_nod_cond["setNodosLosaInf"]{(abs(coord[1]-coordsYNodosTendon[10])<tol)}
            nodos(sort_on_prop(coord[0]))
          }
        \def_set["setNodosTendon11"]
          {
            numCordones= [numToronesNodoZona0[11],numToronesNodoZona1[11],numToronesNodoZona2[11],numToronesNodoZona3[11],numToronesNodoZona4[11]]
            \sel_nod_cond["setNodosLosaInf"]{(abs(coord[1]-coordsYNodosTendon[11])<tol)}
            nodos(sort_on_prop(coord[0]))
          }
        \def_set["setNodosTendonSup01"]
          {
            \sel_nod_cond["setAlmas"]{(abs(coord[1]-yUnionLosaSupAlmaDerecha)<tol) & (abs(coord[2]-zUnionLosaSupAlmaDerecha)<tol)}
            nodos(sort_on_prop(coord[0]))
          }
        \def_set["setNodosTendonSup02"]
          {
            \sel_nod_cond["setAlmas"]{(abs(coord[1])<tol) & (abs(coord[2]-zUnionLosaSupAlmaCentral)<tol)}
            nodos(sort_on_prop(coord[0]))
          }
        \def_set["setNodosTendonSup03"]
          {
            \sel_nod_cond["setAlmas"]{(abs(coord[1]-yUnionLosaSupAlmaIzquierda)<tol) & (abs(coord[2]-zUnionLosaSupAlmaIzquierda)<tol)}
            nodos(sort_on_prop(coord[0]))
          }
