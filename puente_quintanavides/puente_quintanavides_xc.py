# -*- coding: utf-8
execfile('puente_quintanavides_xci.py')


def trataResultsComb(nmbComb):
    mdlr(dom(calculate_nodal_reactions(1)\listaReaccionesNodos(nmbComb,tagsNodosCoartados,"%7.2f","reacc","cabecera","tit")))

\nuevo_archivo_salida["reacc"]{"reacciones_por_hipotesis.tex"}
execfile('resuelve_hipotesis_simples_xci.py')
cierra_archivo_salida("reacc")

'''
mdlr(loads(execfile('combinaciones/def_hip_elspf_xci.py')))
execfile('combinaciones/calc_hip_elspf_xci.py')
'''
execfile('graficos_vtk_xci.py')
VtkMuestraVentana("renderer",800,600)
