xTendon0= 3.0
xTendon1= 4.0
xTendon2= 5.0
xTendon3= 7.0

def mallaTendon(nmbSet):
    \mdlr
        listaNodos= 
        sets(nmbSet( listaNodos= getListTagNodos))

        i= 0
        nn= listaNodos.size-1
        listaElementos= 
        \for
          {
            inicio(i=0 ) continua(i<nn) incremento(i=i+1)
            \bucle
              {
                \elementos
                  {
                    nmb_material("cordon")
                    dim_elem(3)
                    truss(nodes(listaNodos[i],listaNodos[i+1]) listaElementos(inserta(tag)))
                  }
              }
          }
        sets(nmbSet( sel_elementos_lista(listaElementos)))

def asignaAreasTendon(nmbSet):
    \mdlr
        xCDG= 0
        \sets{\nmbSet{\elementos{\for_each
          {
            xCDG= getCooCdg[0]
            \if
              {
                cond((xCDG<xTendon0)|(xCDG>(LTot-xTendon0)))
                then( A(areaCordon*numCordones[0]) )
                \else{ \if
                  {
                    cond((xCDG<xTendon1)|(xCDG>(LTot-xTendon1)))
                    then( A(areaCordon*numCordones[1]) )
                \else{ \if
                  {
                    cond((xCDG<xTendon2)|(xCDG>(LTot-xTendon2)))
                    then( A(areaCordon*numCordones[2]) )
                \else{ \if
                  {
                    cond((xCDG<xTendon3)|(xCDG>(LTot-xTendon3)))
                    then( A(areaCordon*numCordones[3]) )
                \else
                  {
                    A(areaCordon*numCordones[4])
                  }
              }}}}}}}
          }}}}
        '''\sets{\nmbSet{\elementos{\for_each
          { print("elemento: ",tag," xCDG: ",getCooCdg[0]," cordones: ",getArea/areaCordon,"\n")
          }}}}'''
       }

\mallaTendon("setNodosTendon00")
\mallaTendon("setNodosTendon01")
\mallaTendon("setNodosTendon02")
\mallaTendon("setNodosTendon03")
\mallaTendon("setNodosTendon04")
\mallaTendon("setNodosTendon05")
\mallaTendon("setNodosTendon06")
\mallaTendon("setNodosTendon07")
\mallaTendon("setNodosTendon08")
\mallaTendon("setNodosTendon09")
\mallaTendon("setNodosTendon10")
\mallaTendon("setNodosTendon11")

\mallaTendon("setNodosTendonSup01")
\mallaTendon("setNodosTendonSup02")
\mallaTendon("setNodosTendonSup03")

\asignaAreasTendon("setNodosTendon00")
\asignaAreasTendon("setNodosTendon01")
\asignaAreasTendon("setNodosTendon02")
\asignaAreasTendon("setNodosTendon03")
\asignaAreasTendon("setNodosTendon04")
\asignaAreasTendon("setNodosTendon05")
\asignaAreasTendon("setNodosTendon06")
\asignaAreasTendon("setNodosTendon07")
\asignaAreasTendon("setNodosTendon08")
\asignaAreasTendon("setNodosTendon09")
\asignaAreasTendon("setNodosTendon10")
\asignaAreasTendon("setNodosTendon11")

\mdlr
    \sets{\setNodosTendonSup01{elementos(for_each(A(areaCordon*3) ))}}
    \sets{\setNodosTendonSup02{elementos(for_each(A(areaCordon*3) ))}}
    \sets{\setNodosTendonSup03{elementos(for_each(A(areaCordon*3) ))}}
