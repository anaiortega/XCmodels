


exec(open('materiales/xLamina/extrae_combinaciones_xcm.py').read())
exec(open('materiales/xLamina/modelo_xcm.py').read())
exec(open('solution/resuelve_combinacion_xcm.py').read())
exec(open('listados/listados_factor_capacidad_xcm.py').read())
exec(open('materiales/xLamina/postproceso_xLamina_xcm.py').read())
exec(open('materiales/xLamina/calculo_tn_xcm.py').read())


nmbArch= "esfVoladizoIzqTramos0156" # XXX AQUI SE ESCRIBE EL NOMBRE (SIN EXTENSI�N) DEL LISTADO DE HIP�TESIS
os.system("cat "+ nmbArch +".txt | sed 's/\(ELU[0-9]*\)/\"\1\"/g' > "+ nmbArch +".dat")
\extraeDatos(nmbArch+".dat")

\xLaminaConstruyeModelo("../../materiales_losa.xci","defScc1.xci","defScc2.xci")
\xLaminaCompruebaTNComb()
os.system("rm -f "+nmbArch+".dat")
