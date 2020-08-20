listaAcciones= 
\mdlr{\loads
    \constant_ts["cts"]{ factor(1.0) } # Time series: constant_ts[nombre]{factor}
     set_current_time_series("cts")

    \load_pattern["RETRACC"]
    \load_pattern["FLU"]

    \load_pattern["G0"] # Peso propio de la sección prefabricada
    \load_pattern["G0B"] # Peso propio de la losa superior
    \load_pattern["G1"] # Peso propio de la losa superior y de la carga muerta
    \load_pattern["TC1V1"] # Tren de cargas 1 en vía 1
    \load_pattern["TC1V2"] # Tren de cargas 1 en vía 2
    \load_pattern["TC2V1"] # Tren de cargas 2 en vía 1
    \load_pattern["TC2V2"] # Tren de cargas 2 en vía 2
    \load_pattern["TC3V1"] # Tren de cargas 3 en vía 1
    \load_pattern["TC3V2"] # Tren de cargas 3 en vía 2
    \load_pattern["FV1"] # Frenado en vía 1
    \load_pattern["FV2"] # Frenado en vía 2
    \load_pattern["ARRV1"] # Arranque en vía 1
    \load_pattern["ARRV2"] # Arranque en vía 2
    \load_pattern["LZV1"] # Efecto de lazo en vía 1
    \load_pattern["LZV2"] # Efecto de lazo en vía 2
    \load_pattern["VTRSV"] # Viento transversal
    \load_pattern["VLONG"] # Viento longitudinal
    \load_pattern["NV"] # Nieve
    \load_pattern["AD2"] # Situación de descarrilo 2

    listaAcciones= listaNombresLoadPatterns()
  }}
numAcciones= listaAcciones.size
nPaso= 0
