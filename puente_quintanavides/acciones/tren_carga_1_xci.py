# Definimos los conjuntos sobre los que se aplican las cargas
\sets
   {
     nP1= 
     nP2= 
     nP3= 
     nP4= 
     \lineasTablero
       {
         nP1= getTagNearestNode(0.0,0.0,0.0)
         nP2= getTagNearestNode(1.6,0.0,0.0)
         nP3= getTagNearestNode(2*1.6,0.0,0.0)
         nP4= getTagNearestNode(3*1.6,0.0,0.0)
       }
     \def_set["TC1ElementosCargaR"]
       {
         sel_elem_cond((getCooMaxNod(0)>3*1.6+0.8) & (getDimension==1))
         '''\elementos
           {
             \for_each
               {
                 print("tag= ",getTag)
                 nodePtrs(print(" nodo I:",getTagNode(0)," nodo J:",getTagNode(1),"\n"))
               }
           }'''
       }
     \def_set["TC1NodosCargaR"]
       {
         sel_nod_cond((coord[0]>(3*1.6+0.8)) & (coord[2]>9) )
       }
     \def_set["TC1NodosCargaP"]
       {
         sel_nod(nP1,nP2,nP3,nP4)
       }
   }
