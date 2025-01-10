# -*- coding: utf-8
exec(open('puente_quintanavides_xci.py').read())
os.system("rm -f resultados/esf*")

def trataResultsComb(nmbComb):
    exec(open('obtenc_resultados/lista_reacciones_xci.py').read())
    exec(open('obtenc_resultados/lista_esf_tendones_xci.py').read())
    exec(open('obtenc_resultados/exporta_esfuerzos_shell_xci.py').read())

\mdlr{\loads
    \combinacion["FASE0"]{ descomp("1.00*G0")} # Antes de hormigonar la losa.
    exec(open('combinaciones/def_hip_elu_resumidas_xci.py').read())
  }}

os.system("rm -r -f ./flash/tmp_xc/calcula_elu.db")
\database["./flash/tmp_xc/calcula_elu.db","BerkeleyDB"]{}


tagSaveFase0= 
\mdlr{\loads
    \combinaciones
        nombrePrevia= 
        \combinacion["FASE0"]{tagSaveFase0= tag*100}
        tagPrevia= 
        tagSave= 
  }}
\nuevo_archivo_salida["reacc"]{"resultados/reacciones_elu.tex"}

exec(open('solucion/resuelveFASE0_xci.py').read())
exec(open('combinaciones/calc_hip_elu_resumidas_xci.py').read())
cierra_archivo_salida("reacc")
quit()

exec(open('graficos_vtk_xci.py').read())
setup_render_window(renderer,800,600)
