# -*- coding: utf-8
# Calcula las flechas en el puente.
execfile('puente_quintanavides_xci.py')


def trataResultsComb(nmbComb):
    execfile('obtenc_resultados/lista_esf_tendones_els_xci.py')
    \nuevo_archivo_salida["flechas","app"]{"resultados/flechas_elscp.tex"}
    \listaDesplazamientosNodos(nmbComb,tagsNodosFlecha,"%7.2f","flechas","cabecera","tit")
    cierra_archivo_salida("flechas")

\mdlr{\loads
    \combinacion["FASE0"]{ descomp("1.00*G0")} # Antes de hormigonar la losa.
    execfile('combinaciones/def_hip_elscp_resumidas_xci.py')
  }}

os.system("touch resultados/flechas_elscp.tex")
os.system("mv -f resultados/flechas_elscp.tex resultados/flechas_elscp.tex.old")
os.system("rm -r -f /media/disk/tmp_xc/calcula_flechas.db")
\database["/media/disk/tmp_xc/calcula_flechas.db","BerkeleyDB"]{}


tagSaveFase0= 
\mdlr{\loads
    \combinaciones
        nombrePrevia= 
        \combinacion["FASE0"]{tagSaveFase0= tag*100}
        tagPrevia= 
        tagSave= 
  }}

execfile('solucion/resuelveFASE0_xci.py')
execfile('combinaciones/calc_hip_elscp_resumidas_xci.py')

