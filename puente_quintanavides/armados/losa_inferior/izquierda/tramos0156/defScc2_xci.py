# Losa inferior viga. Armadura transversal.

ancho= 1.0 # XXX Ancho de la sección expresado en metros.
canto= 0.25 # XXX Canto de la sección expresado en metros.
recpos= 0.02+0.012 # XXX Recubrimiento cara + expresado en metros.
recneg= 0.02+0.012 # XXX Recubrimiento cara - expresado en metros.

areaFi8= 0.50e-4 # XXX Área de las barras expresado en metros cuadrados.
areaFi10=0.785e-4
areaFi12=1.13e-4 
areaFi16= 2.01e-4
areaFi20= 3.14e-4
areaFi25= 4.608e-4


\mdlr
    # Definimos materiales
    \materiales
        \geom_secc["geomSecHA2"]
          {
            # Hormigón
            \regiones{\reg_cuad[HP50.nmbDiagD]
              {
                nDivIJ(10)
                nDivJK(10)
                pMin(-ancho/2,-canto/2)
                pMax(ancho/2,canto/2)
              }}
            # Armadura
            \armaduras{\capa_armadura_recta[B500S.nmbDiagD]
              {
                numReinfBars(5)
                barArea(areaFi20)
                \p1{-ancho/2+recneg,-canto/2+recneg} # Armadura cara -).
                \p2{ancho/2-recneg,-canto/2+recneg}
              }
            \capa_armadura_recta[B500S.nmbDiagD]
              {
                numReinfBars(5)
                barArea(areaFi20)
                \p1{-ancho/2+recpos,canto/2-recpos} # Armadura superior (cara +).
                \p2{ancho/2-recpos,canto/2-recpos}
              }}
          }
        \fiber_section_3d["secHA2"]
          {
            def_section_repr( geom("geomSecHA2"))
          }
        \define_diagrama_interaccion["secHA2"]
          {
            tag_hormigon(tagHA)
            tag_armadura(tagB500S)
          }
