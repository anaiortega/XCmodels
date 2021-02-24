# -*- coding: utf-8
exec(open('puente_quintanavides_xci.py').read())


def trataResultsComb(nmbComb):
    mdlr(dom(calculate_nodal_reactions(1)\listaReaccionesNodos(nmbComb,tagsNodosCoartados,"%7.2f","reacc","cabecera","tit")))

\nuevo_archivo_salida["reacc"]{"reacciones_por_hipotesis.tex"}
exec(open('resuelve_hipotesis_simples_xci.py').read())
cierra_archivo_salida("reacc")

'''
mdlr(loads(exec(open('combinaciones/def_hip_elspf_xci.py')).read())
exec(open('combinaciones/calc_hip_elspf_xci.py').read())
'''
exec(open('graficos_vtk_xci.py').read())
VtkMuestraVentana("renderer",800,600)
