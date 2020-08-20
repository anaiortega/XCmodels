# -*- coding: utf-8
execfile('puente_quintanavides_xci.py')
os.system("rm -f resultados/esf*")

def trataResultsComb(nmbComb):
    execfile('obtenc_resultados/lista_reacciones_xci.py')
    execfile('obtenc_resultados/lista_esf_tendones_xci.py')
    execfile('obtenc_resultados/exporta_esfuerzos_shell_xci.py')

\mdlr{\loads
    \combinacion["FASE0"]{ descomp("1.00*G0")} # Antes de hormigonar la losa.
    execfile('combinaciones/def_hip_elu_resumidas_xci.py')
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

execfile('solucion/resuelveFASE0_xci.py')
execfile('combinaciones/calc_hip_elu_resumidas_xci.py')
cierra_archivo_salida("reacc")
quit()

execfile('graficos_vtk_xci.py')
VtkMuestraVentana("renderer",800,600)
