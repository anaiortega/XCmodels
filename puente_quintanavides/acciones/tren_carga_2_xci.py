# Definimos los conjuntos sobre los que se aplican las cargas
cargaP= 1.21*250e3
cargaR= 1.21*80e3
x0= 15.8 '''Abcisa hasta la que se extiende
                                  la carga uniforme.'''
x1= x0+0.8 # Abcisa de la primera carga puntual.
x2= x1+1.6 # Abcisa de la segunda carga puntual.
x3= x2+1.6 # Abcisa de la tercera carga puntual.
x4= x3+1.6 # Abcisa de la cuarta carga puntual.
x5= x4+0.8 # Vuelve a aplicarse la carga uniforme.

\sets
   {
     nP1= 
     nP2= 
     nP3= 
     nP4= 
     \lineasTablero
       {
         nP1= getTagNearestNode(x1,0.0,0.0)
         nP2= getTagNearestNode(x2,0.0,0.0)
         nP3= getTagNearestNode(x3,0.0,0.0)
         nP4= getTagNearestNode(x4,0.0,0.0)
       }
     \def_set["TC2ElementosCargaR"]
       {
         sel_elem_cond(((getCooMinNod(0)<x0) | (getCooMaxNod(0)>x5)) & (getDimension==1))
       }
     \def_set["TC2NodosCargaR"]
       {
         sel_nod_cond(((coord[0]<x1)|(coord[0]>x5)) & (coord[2]>9) )
       }
     \def_set["TC2NodosCargaP"]
       {
         sel_nod(nP1,nP2,nP3,nP4)
       }
   }
