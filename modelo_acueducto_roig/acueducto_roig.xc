
archivo_err("pp.err")
archivo_log("pp.log")

execfile("vtk/displayVtk.lcmm")
execfile("vtk/vtk_define_malla_cad.xcm")
execfile("vtk/vtk_define_malla_elementos.xcm")
execfile("vtk/vtk_cargas_elementos.xcm")
execfile("vtk/utilsVtk.lcmm")
execfile("latex/supertabular.lcmm")

execfile("listados/listados_datos.xcm")
execfile("listados/listados_cargas.xcm")
execfile("listados/listados_resultados.xcm")
execfile("modelo/fija_nodo_6gdl.xcm")
execfile("modelo/fija_nodos_lineas.xcm")
execfile("modelo/tensa_cables.xcm")
execfile("acciones/utilsAcciones.xcm")
execfile("materiales/coefsDistorsion.xcm")
execfile("fija_arranques.xcm")
execfile("modelo/cargas_elem.xcm")


execfile("solucion.xci")
execfile("solucion.xcm")
execfile("postproceso.xcm")

execfile("geom_acueducto.xci")
execfile("geom_secciones.xci")

execfile("define_casos_carga.xci")
execfile("genera_malla.xcm")

execfile("carga_agua.xci")
execfile("carga_vientoY.xci")
# execfile("incremento_temperatura.xci")

execfile("graficos_vtk.xci")
fin()
execfile("listados.xci")

execfile("cargas.xci")
execfile("resuelve_casos.xci")

