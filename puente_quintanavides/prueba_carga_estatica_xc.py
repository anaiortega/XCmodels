# -*- coding: utf-8
exec(open('puente_quintanavides_xci.py').read()))


exec(open('modelo/sets_prueba_carga_estatica_xci.py').read()))
exec(open('acciones/cargas_prueba_carga_estatica_xci.py').read()))
exec(open('modelo/ptos_control_prueba_carga_estatica_xci.py').read()))

def trataResultsComb(nmbComb):
    \listaDesplazamientosNodos(nmbComb,tagsNodosPControl,"%7.2f","flechasPCE","cabecera","tit")
    \mdlr{\sets
       {
         \total
           {
             resultante= getResistingSVD3d(plano,o,0.01,0)
             \resultante
               {
                 fuerza= getResultante
                 momento= getMomento
                 Org= getOrg
               }
           }
       }}
    \print["flechasPCE"]{"fuerza= ",fuerza/1e3," kN\n"}
    \print["flechasPCE"]{"momento= ",momento/1e3," kN\n"}
    \print["flechasPCE"]{"org= ",Org," m\n"}


\nuevo_archivo_salida["flechasPCE"]{"resultados/flechas_prueba_carga_estatica.tex"}
os.system("rm -rf /tmp/prueba_carga_estatica.db")
\database["/tmp/prueba_carga_estatica.db","BerkeleyDB"]
tagSaveFase0PCarga= 

exec(open('solucion/resuelveFASE0PCARGA_xci.py').read()))

\mdlr
    dom(\nuevo_caso())
    database(restore(tagSaveFase0PCarga))
    \loads
        \combinacion["PCARGAE"]
          {
            descomp("1.00*G0+1.00*G0B+1.00*PCE")
            \add_to_domain()
            \sol_proc{ \static_analysis["smt"]{ analyze(1) analOk= result } }
          }

o= 
p1= 
p2= 
plano= 
o(x(19.2184, 0, zLosaInf+1.876))
\p1{x(19.2184, 10, zLosaInf+1.876)}
\p2{x(19.2184, 0, zLosaInf+1.876+10)}
\plano
    \3puntos{[o,p1,p2]}
resultante= 
fuerza= 
momento= 
Org= 

\trataResultsComb("PCARGAE")

\mdlr
    dom(nuevo_caso())
    database(restore(tagSaveFase0PCarga))
    \loads
        \combinacion["CARGAFERROVIARIA"]
          {
            descomp("1.00*G0+1.00*G1+1.00*TC2V1+1.00*TC2V2")
            add_to_domain()
            \sol_proc{ \static_analysis["smt"]{ analyze(1) analOk= result } }
          }
\trataResultsComb("CARGAFERROVIARIA")
cierra_archivo_salida("flechasPCE")
