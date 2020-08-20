


execfile('materiales/xLamina/extrae_combinaciones_xcm.py')
execfile('materiales/xLamina/modelo_xcm.py')
execfile('solution/resuelve_combinacion_xcm.py')
execfile('listados/listados_factor_capacidad_xcm.py')
execfile('materiales/xLamina/postproceso_xLamina_xcm.py')
execfile('materiales/xLamina/calculo_tn_xcm.py')


nmbArch= "esfLosaViaDerTramos24" # XXX AQUI SE ESCRIBE EL NOMBRE (SIN EXTENSIÓN) DEL LISTADO DE HIPÓTESIS
os.system("cat "+ nmbArch +".txt | sed 's/\(ELU[0-9]*\)/\"\1\"/g' > "+ nmbArch +".dat")
\extraeDatos(nmbArch+".dat")

\xLaminaConstruyeModelo("../../materiales_losa.xci","defScc1.xci","defScc2.xci")
\xLaminaCompruebaTNComb()
os.system("rm -f "+nmbArch+".dat")
