# Abcisas para aplicación de las cargas del tren 1.
x1TC1= LTramo0
x2TC1= x1TC1+1.6
x3TC1= x2TC1+1.6
x4TC1= x3TC1+1.6
x5TC1= x4TC1+0.8

# Abcisas para aplicación de las cargas del tren 2.
x0TC2= 15.8
x1TC2= x0TC2+0.8
x2TC2= x1TC2+1.6
x3TC2= x2TC2+1.6
x4TC2= x3TC2+1.6
x5TC2= x4TC2+0.8

# Abcisas para aplicación de las cargas del tren 3.
x4TC3= LTot-LTramo0
x3TC3= x4TC3-1.6
x2TC3= x3TC3-1.6
x1TC3= x2TC3-1.6
x0TC3= x1TC3-0.8

\mdlr
    \sets
         tol= ladoElemento/100

         \def_set["setNodosVia1"]
           {
             sel_nod_cond((abs(coord[1]-yVia1CD)<tol) & (abs(coord[2]-zVia1CD)<tol))
             sel_nod_cond((abs(coord[1]-yVia1CI)<tol) & (abs(coord[2]-zVia1CI)<tol))
           }
         \def_set["setNodosVia2"]
           {
             sel_nod_cond((abs(coord[1]-yVia2CD)<tol) & (abs(coord[2]-zVia2CD)<tol))
             sel_nod_cond((abs(coord[1]-yVia2CI)<tol) & (abs(coord[2]-zVia2CI)<tol))
           }
         \def_set["setNodosMureteCI"]
           {
             sel_nod_cond((abs(coord[1]-yMureteCI)<0.4))
           }
         # Elementos sobre los que actúa la carga de nieve.
         \def_set["setElemsNieve"]
           {
             sel_elem_cond((getCooCdg[1]<yVia1CD) & (getCooCdg[2]>1.3) & (getDimension>1))
             sel_elem_cond((getCooCdg[1]>yVia1CI) & (getCooCdg[1]<yVia2CD) & (getCooCdg[2]>1.3) & (getDimension>1))
             sel_elem_cond((getCooCdg[1]>yVia2CI) & (getCooCdg[2]>1.3) & (getDimension>1))
           }
         \def_set["setNodosPVia1TC1"]
           {
             \sel_nod_cond["setNodosVia1"]{(abs(coord[0]-x1TC1)<tol)}
             \sel_nod_cond["setNodosVia1"]{(abs(coord[0]-x2TC1)<tol*10)}
             \sel_nod_cond["setNodosVia1"]{(abs(coord[0]-x3TC1)<tol*10)}
             \sel_nod_cond["setNodosVia1"]{(abs(coord[0]-x4TC1)<tol*15)}
             assert(getNumNodos==8)
           }
         \def_set["setNodosRVia1TC1"]
           {
             \sel_nod_cond["setNodosVia1"]{coord[0]>x5TC1}
           }
         \def_set["setNodosPVia2TC1"]
           {
             \sel_nod_cond["setNodosVia2"]{(abs(coord[0]-x1TC1)<tol)}
             \sel_nod_cond["setNodosVia2"]{(abs(coord[0]-x2TC1)<tol*10)}
             \sel_nod_cond["setNodosVia2"]{(abs(coord[0]-x3TC1)<tol*10)}
             \sel_nod_cond["setNodosVia2"]{(abs(coord[0]-x4TC1)<tol*15)}
             assert(getNumNodos==8)
           }
         \def_set["setNodosRVia2TC1"]
           {
             \sel_nod_cond["setNodosVia2"]{coord[0]>x5TC1}
           }
         \def_set["setNodosPMureteCI"]
           {
             \sel_nod_cond["setNodosMureteCI"]{(abs(coord[0]-x1TC1)<tol)}
             \sel_nod_cond["setNodosMureteCI"]{(abs(coord[0]-x2TC1)<tol*10)}
             \sel_nod_cond["setNodosMureteCI"]{(abs(coord[0]-x3TC1)<tol*10)}
             \sel_nod_cond["setNodosMureteCI"]{(abs(coord[0]-x4TC1)<tol*15)}
             assert(getNumNodos==4)
           }
         \def_set["setNodosRMureteCI"]
           {
             \sel_nod_cond["setNodosMureteCI"]{(coord[0]>x5TC1) & (coord[0]<20)}
             \nodos{\for_each
                {
print("x= ",coord[0],", y= ",coord[1],", z= ",coord[2],"\n")
                }}
           }
         \def_set["setNodosPVia1TC2"]
           {
             \sel_nod_cond["setNodosVia1"]{(abs(coord[0]-x1TC2)<tol*45)}
             \sel_nod_cond["setNodosVia1"]{(abs(coord[0]-x2TC2)<tol*45)}
             \sel_nod_cond["setNodosVia1"]{(abs(coord[0]-x3TC2)<tol*45)}
             \sel_nod_cond["setNodosVia1"]{(abs(coord[0]-x4TC2)<tol*45)}
             assert(getNumNodos==8)
           }
         \def_set["setNodosRVia1TC2"]
           {
             \sel_nod_cond["setNodosVia1"]{coord[0]<x0TC2}
             \sel_nod_cond["setNodosVia1"]{coord[0]>x5TC2}
           }
         \def_set["setNodosPVia2TC2"]
           {
             \sel_nod_cond["setNodosVia2"]{(abs(coord[0]-x1TC2)<tol*45)}
             \sel_nod_cond["setNodosVia2"]{(abs(coord[0]-x2TC2)<tol*45)}
             \sel_nod_cond["setNodosVia2"]{(abs(coord[0]-x3TC2)<tol*45)}
             \sel_nod_cond["setNodosVia2"]{(abs(coord[0]-x4TC2)<tol*45)}
             assert(getNumNodos==8)
           }
         \def_set["setNodosRVia2TC2"]
           {
             \sel_nod_cond["setNodosVia2"]{coord[0]<x0TC2}
             \sel_nod_cond["setNodosVia2"]{coord[0]>x5TC2}
           }

         \def_set["setNodosPVia1TC3"]
           {
             \sel_nod_cond["setNodosVia1"]{(abs(coord[0]-x1TC3)<tol*15)}
             \sel_nod_cond["setNodosVia1"]{(abs(coord[0]-x2TC3)<tol*10)}
             \sel_nod_cond["setNodosVia1"]{(abs(coord[0]-x3TC3)<tol*10)}
             \sel_nod_cond["setNodosVia1"]{(abs(coord[0]-x4TC3)<tol)}
             assert(getNumNodos==8)
           }
         \def_set["setNodosRVia1TC3"]
           {
             \sel_nod_cond["setNodosVia1"]{coord[0]<x0TC3}
           }
         \def_set["setNodosPVia2TC3"]
           {
             \sel_nod_cond["setNodosVia2"]{(abs(coord[0]-x1TC3)<tol*15)}
             \sel_nod_cond["setNodosVia2"]{(abs(coord[0]-x2TC3)<tol*10)}
             \sel_nod_cond["setNodosVia2"]{(abs(coord[0]-x3TC3)<tol*10)}
             \sel_nod_cond["setNodosVia2"]{(abs(coord[0]-x4TC3)<tol)}
             assert(getNumNodos==8)
           }
         \def_set["setNodosRVia2TC3"]
           {
             \sel_nod_cond["setNodosVia2"]{coord[0]<x0TC3}
           }
         # Elementos sobre los que actúa la componente horizontal del viento transversal.
         \def_set["setElemsVientoTrsvH"]
           {
             sel_elem_cond((getCooCdg[1]<yUnionLosaInfAlmaDerecha) & (getCooCdg[1]>yUnionLosaSupAlmaDerecha) & (getCooCdg[2]<zUnionLosaSupAlmaDerecha) & (getCooCdg[2]>(zUnionLosaSupAlmaDerecha+zLosaInf)/2) & (abs(getCooCdg[0]-0.6)>tol) & (abs(getCooCdg[0]-38.6)>tol) & (getDimension>1))
             # completa_hacia_abajo(
             print("Número de elementos: ",getNumElementos,"\n")
             print("Número de nodos: ",getNumNodos,"\n"))
           }
         # Elementos sobre los que actúa la componente vertical del viento transversal.
         \def_set["setElemsVientoTrsvV"]
           {
             sel_elem_cond((getCooCdg[1]<0) & (getCooCdg[2]>zExtremoAlas) & (getDimension>1))
             # completa_hacia_abajo(
             print("Número de elementos: ",getNumElementos,"\n")
             print("Número de nodos: ",getNumNodos,"\n"))
           }
         # Elementos sobre los que actúa el viento transversal.
         \def_set["setElemsVientoTrsv"]
           {
             sel_set("setElemsVientoTrsvH") sel_set("setElemsVientoTrsvV")
             # completa_hacia_abajo(
             print("Número de elementos: ",getNumElementos,"\n")
             print("Número de nodos: ",getNumNodos,"\n"))
           }
         # Elementos sobre los que actúa el viento longitudinal.
         \def_set["setElemsVientoLong"]
           {
             sel_elem_cond((getCooCdg[2]>zExtremoAlas) & (getDimension>1))
             # completa_hacia_abajo(
             print("Número de elementos: ",getNumElementos,"\n")
             print("Número de nodos: ",getNumNodos,"\n"))
           }
