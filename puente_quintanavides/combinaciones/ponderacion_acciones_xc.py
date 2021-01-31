# Archivo para la generación de combinaciones



exec(open('listados/listado_hipotesis_xcm.py').read())


\comb_acciones
    exec(open('comb_acciones/iapf/gammaf_iapf.cmbm').read())
    \pond_acciones
        \IAPF
          {
            exec(open('comb_acciones/iapf/coefs_psi_iapf.cmbm').read())
            \permanentes
              {
                \acciones
                  {
                    \accion
                      {
                        nombre("G1") descripcion("Carga permanente")
                      }
                  }
              }
            \variables
              {
                \acciones
                  {
                    \accion
                      {
                        nombre("TC1V1") descripcion("Tren de cargas 1 en vía 1")
                        relaciones(incompatibles("TC.*V1"))
                        setCoefsPsi("iapf_por_defecto")
                      }
                    \accion
                      {
                        nombre("TC1V2") descripcion("Tren de cargas 1 en vía 2")
                        relaciones(incompatibles("TC.*V2"))
                        setCoefsPsi("iapf_por_defecto")
                      }
                    \accion
                      {
                        nombre("TC2V1") descripcion("Tren de cargas 2 en vía 1")
                        relaciones(incompatibles("TC.*V1"))
                        setCoefsPsi("iapf_por_defecto")
                      }
                    \accion
                      {
                        nombre("TC2V2") descripcion("Tren de cargas 2 en vía 2")
                        relaciones(incompatibles("TC.*V2"))
                        setCoefsPsi("iapf_por_defecto")
                      }
                    \accion
                      {
                        nombre("TC3V1") descripcion("Tren de cargas 3 en vía 1")
                        relaciones(incompatibles("TC.*V1"))
                        setCoefsPsi("iapf_por_defecto")
                      }
                    \accion
                      {
                        nombre("TC3V2") descripcion("Tren de cargas 3 en vía 2")
                        relaciones(incompatibles("TC.*V2"))
                        setCoefsPsi("iapf_por_defecto")
                      }
                    \accion
                      {
                        nombre("FV1") descripcion("Frenado en vía 1")
                        relaciones(maestras("TC2V1") incompatibles("ARRV1"))
                        setCoefsPsi("iapf_arranque_frenado")
                      }
                    \accion
                      {
                        nombre("FV2") descripcion("Frenado en vía 2")
                        relaciones(maestras("TC2V2") incompatibles("ARRV2"))
                        setCoefsPsi("iapf_arranque_frenado")
                      }
                    \accion
                      {
                        nombre("ARRV1") descripcion("Arranque en vía 1")
                        relaciones(maestras("TC2V1") incompatibles("FV1"))
                        setCoefsPsi("iapf_arranque_frenado")
                      }
                    \accion
                      {
                        nombre("ARRV2") descripcion("Arranque en vía 2")
                        relaciones(maestras("TC2V2") incompatibles("FV2"))
                        setCoefsPsi("iapf_arranque_frenado")
                      }
                    \accion
                      {
                        nombre("LZV1") descripcion("Efecto de lazo en vía 1")
                        relaciones(maestras("TC.*V1") incompatibles("LZV2") incompatibles("ARR.*")incompatibles("F.*"))
                        setCoefsPsi("iapf_por_defecto")
                      }
                    \accion
                      {
                        nombre("LZV2") descripcion("Efecto de lazo en vía 2")
                        relaciones(maestras("TC.*V2") incompatibles("LZV2") incompatibles("ARR.*")incompatibles("F.*") )
                        setCoefsPsi("iapf_por_defecto")
                      }
                    \accion
                      {
                        nombre("VTRSV") descripcion("Viento transversal")
                        relaciones( incompatibles("V.*") incompatibles("N.*"))
                        setCoefsPsi("iapf_viento")
                      }
                    \accion
                      {
                        nombre("VLONG") descripcion("Viento longitudinal")
                        relaciones( incompatibles("V.*") incompatibles("N.*")) # El peso de la nieve es favorable
                        setCoefsPsi("iapf_viento")
                      }
                    \accion
                      {
                        nombre("NV") descripcion("Nieve")
                        setCoefsPsi("iapf_nieve")
                      }
                  }
              }
        }
    
    \genera_combinaciones()

    exec(open('comb_acciones/listados/trata_comb_els_xci.py').read())
    exec(open('comb_acciones/listados/trata_comb_elu_xci.py').read())

