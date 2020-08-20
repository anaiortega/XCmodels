# -*- coding: utf-8

\mdlr
    \dom
        \mesh
          {
            constraints(print("antes num sps: ",getNumSPs,"\n\n"))
          }
    sets(setLosaSup(kill_elements() )) # Desactivamos los elementos de la losa superior.

    \dom
        \mesh
          {
            set_dead_srf(0)
            freeze_dead_nodes("congelaLosa") # Coacciona nodos inactivos.
          }

