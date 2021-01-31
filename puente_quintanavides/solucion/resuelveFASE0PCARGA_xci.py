modelSpace.removeAllLoadPatternsFromDomain()
modelSpace.revertToStart()
modelSpace.deactivateElements(setLosaSup) # Deactivate bridge deck.

lc0= modelSpace.addLoadCaseToDomain('G0')
analOk= solProc.solve()

modelSpace.activateElements(setLosaSup) # Activate bridge deck.
tPruebaCarga= 200 # Instante de la prueba de carga.

exec(open('modelo/retraccion_fluencia_xci.py').read()))
\mdlr
    # Deformaciones de retracción.
    \sets
        \def_set["setPrefabricado"]{ sel_set("setArtesa") sel_set("setDiafragmas")}
        \def_set["setHormigonTablero"]{sel_set("setLosaSup") sel_set("setPrefabricado")}
        \setLosaSup{\elementos
          {
            \for_each
              {
                ladoMedio= getPerimetro/4
                grueso= 
                \material[0]{grueso= getThickness}
                Ac= ladoMedio*grueso
                u= 2*ladoMedio
                espMedio= 2*Ac/u
                epsRetracc= getDeformacionRetraccion(30e6,tPruebaCarga,tSecadoLosa,Hrel,u,Ac,velCemento)
              }
          }}
        \setPrefabricado{\elementos
          {
            \for_each
              {
                ladoMedio= getPerimetro/4
                grueso= 
                \material[0]{grueso= getThickness}
                Ac= ladoMedio*grueso
                u= 2*ladoMedio
                espMedio= 2*Ac/u
                epsRetracc= getDeformacionRetraccion(30e6,tPruebaCarga,tSecadoVigas,Hrel,u,Ac,velCemento)
              }
          }}
    loads(casos(set_current_load_pattern("RETRACC")))
    \sets
        \setHormigonTablero{\elementos
          {
            \for_each
              {
                \strain_load
                  {
                    \strain(0,0){epsRetracc}
                    \strain(1,0){epsRetracc}
                    \strain(2,0){epsRetracc}
                    \strain(3,0){epsRetracc}
                    \strain(0,1){epsRetracc}
                    \strain(1,1){epsRetracc}
                    \strain(2,1){epsRetracc}
                    \strain(3,1){epsRetracc}
                  }
              }
          }}

    dom(nuevo_caso())
    \loads
        \combinacion["FASE0PCARGA"]
          {
            descomp("1.00*G0+1.00*G0B+1.00*RETRACC")
            tagSaveFase0PCarga= tag*100
            add_to_domain()
            \sol_proc{ \static_analysis["smt"]{ analyze(1) analOk= result } }
          }
        combinaciones(remove("FASE0PCARGA")) # Para que no siga añadiendo retracción en cada cálculo.
    # Deformaciones de fluencia.
    \sets
        \setLosaSup{\elementos
          {
            \for_each
              {
                epsFluencia1= 
                epsFluencia2= 
                \materiales
                  {
                    tension1Media= ,n1Medio/Ac
                    tension2Media= ,n2Medio/Ac
                    fi1= getPhiFluencia(30e6,tPruebaCarga,t0Vigas,Hrel,u,Ac)
                    epsFluencia1= getDeformacionFluencia(30e6,t0Losa,arido,0.25,fi1,tension1Media)
                    epsFluencia2= getDeformacionFluencia(30e6,t0Losa,arido,0.25,fi1,tension2Media)
                  }
              }
          }}
        \setPrefabricado{\elementos
          {
            \for_each
              {
                epsFluencia1= 
                epsFluencia2= 
                \materiales
                  {
                    tension1Media= ,n1Medio/Ac
                    tension2Media= ,n2Medio/Ac
                    fi1= getPhiFluencia(30e6,tPruebaCarga,t0Losa,Hrel,u,Ac)
                    epsFluencia1= getDeformacionFluencia(30e6,t0Losa,arido,0.25,fi1,tension1Media)
                    epsFluencia2= getDeformacionFluencia(30e6,t0Losa,arido,0.25,fi1,tension2Media)
    print("epsFluencia1= ",epsFluencia1,"\n")
    print("epsFluencia2= ",epsFluencia2,"\n")
                  }
              }
          }}
    loads(casos(set_current_load_pattern("FLU")))
    \sets
        \setHormigonTablero{\elementos
          {
            \for_each
              {
                \strain_load
                  {
                    \strain(0,0){epsFluencia1}
                    \strain(1,0){epsFluencia1}
                    \strain(2,0){epsFluencia1}
                    \strain(3,0){epsFluencia1}
                    \strain(0,1){epsFluencia2}
                    \strain(1,1){epsFluencia2}
                    \strain(2,1){epsFluencia2}
                    \strain(3,1){epsFluencia2}
                  }
              }
          }}
    dom(nuevo_caso())
    \loads
        \combinacion["FASE0PCARGA"]
          {
            descomp("1.00*G0+1.00*G0B+1.00*FLU")
            tagSaveFase0PCarga= tag*100
            add_to_domain()
            \sol_proc{ \static_analysis["smt"]{ analyze(1) analOk= result } }
          }
        combinaciones(remove("FASE0PCARGA")) # Para que no siga añadiendo fluencia en cada cálculo.
        database(save(tagSaveFase0PCarga))
