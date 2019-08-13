# -*- coding: utf-8 -*-

import xc_base
import loadCombinations
from loadCombinationUtils import iap11
'''
##Nota:
El coeficiente de simultaneidad fi0 de las cargas verticales debidas a vehículo pesado es fi0=0.75 mientras que el de sobrecarga uniforme es fi0=0.4.
Ambas cargas están consideradas en el mismo load case y el programa aplica elcoeficiente 0.75.
Para no penalizar las hipótesis en las que la sobrecarga de tráfico actúa como concomitante, en las hipotesis generadas se ha sustituido el coeficiente 1.35*0.75=1.01 por un coeficiente conjunto igual a 0.6 (ponderando las cargas de los carriles ficticios 1 y 2 actuando en el vano central)
'''
lcg= iap11.controlCombGenerator
#print '*******', pond.permanentActions.gammaF.getGammaFELU.desfavorable

G12=lcg.insert("IAP11","permanentes",loadCombinations.Action("G12","Peso propio + carga muerta"),"permanentes","permanentes")

G3=lcg.insert("IAP11","permanentes_nc",loadCombinations.Action("G3","Reológicas"),"permanentes","permanentes_nc_Reol")

Q1a1=lcg.insert("IAP11","variables",loadCombinations.Action("Q1a1","Tren cargas pos. A1"),"vehículos_pesados","variables_SCuso")
Q1a1.getRelaciones.agregaIncompatible("Q1.*")
Q1a1.getRelaciones.agregaIncompatible("Q21.*")

Q1a2=lcg.insert("IAP11","variables",loadCombinations.Action("Q1a2","Tren cargas pos. A2"),"vehículos_pesados","variables_SCuso")
Q1a2.getRelaciones.agregaIncompatible("Q1.*")
Q1a2.getRelaciones.agregaIncompatible("Q21.*")

Q1b1=lcg.insert("IAP11","variables",loadCombinations.Action("Q1b1","Tren cargas pos. B1"),"vehículos_pesados","variables_SCuso")
Q1b1.getRelaciones.agregaIncompatible("Q1.*")
Q1b1.getRelaciones.agregaIncompatible("Q21.*")

Q1b2=lcg.insert("IAP11","variables",loadCombinations.Action("Q1b2","Tren cargas pos. B2"),"vehículos_pesados","variables_SCuso")
Q1b2.getRelaciones.agregaIncompatible("Q1.*")
Q1b2.getRelaciones.agregaIncompatible("Q21.*")

Q1c=lcg.insert("IAP11","variables",loadCombinations.Action("Q1c","Tren cargas pos. C"),"vehículos_pesados","variables_SCuso")
Q1c.getRelaciones.agregaIncompatible("Q1.*")
Q1c.getRelaciones.agregaIncompatible("Q21.*")

Q1d=lcg.insert("IAP11","variables",loadCombinations.Action("Q1d","Tren cargas pos. D"),"vehículos_pesados","variables_SCuso")
Q1d.getRelaciones.agregaIncompatible("Q1.*")
Q1d.getRelaciones.agregaIncompatible("Q21.*")

Q1e=lcg.insert("IAP11","variables",loadCombinations.Action("Q1e","Tren cargas pos. E"),"vehículos_pesados","variables_SCuso")
Q1e.getRelaciones.agregaIncompatible("Q1.*")
Q1e.getRelaciones.agregaIncompatible("Q21.*")

#Q1f=lcg.insert("IAP11","variables",loadCombinations.Action("Q1f","Tren cargas pos. F"),"vehículos_pesados","variables_SCuso")
#Q1f.getRelaciones.agregaIncompatible("Q1.*")
#Q1f.getRelaciones.agregaIncompatible("Q21.*")

Q1bFren=lcg.insert("IAP11","variables",loadCombinations.Action("Q1bFren","Tren cargas pos. B1 + frenado"),"vehículos_pesados","variables_SCuso")
Q1bFren.getRelaciones.agregaIncompatible("Q.*")

Q1dFren=lcg.insert("IAP11","variables",loadCombinations.Action("Q1dFren","Tren cargas pos. D + frenado"),"vehículos_pesados","variables_SCuso")
Q1dFren.getRelaciones.agregaIncompatible("Q.*")

Q1eFren=lcg.insert("IAP11","variables",loadCombinations.Action("Q1eFren","Tren cargas pos. E + frenado"),"vehículos_pesados","variables_SCuso")
Q1eFren.getRelaciones.agregaIncompatible("Q.*")

Q21=lcg.insert("IAP11","variables",loadCombinations.Action("Q21","Viento"),"viento_sit_persistente","variables_climatica")
Q21.getRelaciones.agregaIncompatible("Q1.*")
Q21.getRelaciones.agregaIncompatible("Q22.*")
Q21.getRelaciones.agregaIncompatible("Q3.*")

Q22=lcg.insert("IAP11","variables",loadCombinations.Action("Q22","Viento con SC uso"),"viento_sit_persistente","variables_climatica")
Q22.getRelaciones.agregaIncompatible("Q21.*")
Q22.getRelaciones.agregaIncompatible("Q3.*")


Q31=lcg.insert("IAP11","variables",loadCombinations.Action("Q31","Temperatura uniforme, contracción"),"termica","variables_climatica")
Q31.getRelaciones.agregaIncompatible("Q2.*")
Q31.getRelaciones.agregaIncompatible("Q3.*")

Q32=lcg.insert("IAP11","variables",loadCombinations.Action("Q32","Temperatura uniforme, dilatación"),"termica","variables_climatica")
Q32.getRelaciones.agregaIncompatible("Q2.*")
Q32.getRelaciones.agregaIncompatible("Q3.*")

Q33=lcg.insert("IAP11","variables",loadCombinations.Action("Q33","Diferencia temperatura, fibra sup. más caliente"),"termica","variables_climatica")
Q33.getRelaciones.agregaIncompatible("Q2.*")
Q33.getRelaciones.agregaIncompatible("Q3.*")

Q34=lcg.insert("IAP11","variables",loadCombinations.Action("Q34","Diferencia temperatura, fibra sup. más fría"),"termica","variables_climatica")
Q34.getRelaciones.agregaIncompatible("Q2.*")
Q34.getRelaciones.agregaIncompatible("Q3.*")

lcg.genera()
ldComb=lcg.getLoadCombinations
ULSperm=ldComb.getULSTransientCombinations
SLSchar=ldComb.getSLSCharacteristicCombinations
SLSfrq=ldComb.getSLSFrequentCombinations
SLSqperm=ldComb.getSLSQuasiPermanentCombinations


f=open("loadComb.py","w")
ftex=open("loadComb.tex","w")
f.write('from actions import combinations as cc \n \n')
f.write('combContainer= cc.CombContainer() \n \n')

#Combinaciones en ELU
ftex.write('\\begin{center} \n')
ftex.write('\\begin{longtable}{|l|p{20cm}|} \n')
ftex.write('\\caption{Combinaciones para comprobaciones en ELU.} \\label{combELU}  \\\\ \n')
ftex.write('\\hline \n')
ftex.write("ELU & Combinación de acciones \\\\ \n")
ftex.write('\\hline \n')
ftex.write("\\endfirsthead  \n")

ftex.write('\\hline \n')
ftex.write("ELU & Combinación de acciones \\\\ \n")
ftex.write('\\hline \n')
ftex.write("\\endhead  \n")

ftex.write("\\hline \\multicolumn{2}{|r|}{Continúa en la siguiente página} \\\\ \\hline \n \\endfoot \n \\hline \n \\endlastfoot  \n ")

cont=1
for lc in ULSperm:
    f.write('combContainer.ULS.perm.add("ELU' +str(cont).rjust(3,'0') + '" , "'+ lc.name +'") \n')
    ftex.write('ELU' +str(cont).rjust(3,'0') +' & ' + lc.descripcion + ' \\\\ \n')
    cont+=1
ftex.write('\\end{longtable} \n')
ftex.write('\\end{center} \n \n \n')
f.write('\n \n')
    


#Combinaciones características en ELS
ftex.write('\\begin{center} \n')
ftex.write('\\begin{longtable}{|l|p{20cm}|} \n')
ftex.write('\\caption{Combinaciones características (poco probables o raras) para comprobaciones en ELS.} \\label{combELSR}  \\\\ \n')
ftex.write('\\hline \n')
ftex.write("ELS & Combinación de acciones \\\\ \n")
ftex.write('\\hline \n')
ftex.write("\\endfirsthead  \n")

ftex.write('\\hline \n')
ftex.write("ELS & Combinación de acciones \\\\ \n")
ftex.write('\\hline \n')
ftex.write("\\endhead  \n")

ftex.write("\\hline \\multicolumn{2}{|r|}{Continúa en la siguiente página} \\\\ \\hline \n \\endfoot \n \\hline \n \\endlastfoot  \n ")

cont=1
for lc in SLSchar:
    f.write('combContainer.SLS.rare.add("ELSR' +str(cont).rjust(3,'0') + '" , "'+ lc.name +'") \n')
    ftex.write('ELSR' +str(cont).rjust(3,'0') +' & ' + lc.descripcion + ' \\\\ \n')
    cont+=1
ftex.write('\\end{longtable} \n')
ftex.write('\\end{center} \n \n \n')
f.write('\n \n')


#Combinaciones frecuentes en ELS
ftex.write('\\begin{center} \n')
ftex.write('\\begin{longtable}{|l|p{20cm}|} \n')
ftex.write('\\caption{Combinaciones frecuentes para comprobaciones en ELS.} \\label{combELSF}  \\\\ \n')
ftex.write('\\hline \n')
ftex.write("ELS & Combinación de acciones \\\\ \n")
ftex.write('\\hline \n')
ftex.write("\\endfirsthead  \n")

ftex.write('\\hline \n')
ftex.write("ELS & Combinación de acciones \\\\ \n")
ftex.write('\\hline \n')
ftex.write("\\endhead  \n")

ftex.write("\\hline \\multicolumn{2}{|r|}{Continúa en la siguiente página} \\\\ \\hline \n \\endfoot \n \\hline \n \\endlastfoot  \n ")

cont=1
for lc in SLSfrq:
    f.write('combContainer.SLS.freq.add("ELSF' +str(cont).rjust(3,'0') + '" , "'+ lc.name +'") \n')
    ftex.write('ELSF' +str(cont).rjust(3,'0') +' & ' + lc.descripcion + ' \\\\ \n')
    cont+=1
ftex.write('\\end{longtable} \n')
ftex.write('\\end{center} \n \n \n')
f.write('\n \n')


#Combinaciones casi-permanentes en ELS
ftex.write('\\begin{center} \n')
ftex.write('\\begin{longtable}{|l|p{20cm}|} \n')
ftex.write('\\caption{Combinaciones casi-permanentes para comprobaciones en ELS.} \\label{combELSQP}  \\\\ \n')
ftex.write('\\hline \n')
ftex.write("ELS & Combinación de acciones \\\\ \n")
ftex.write('\\hline \n')
ftex.write("\\endfirsthead  \n")

ftex.write('\\hline \n')
ftex.write("ELS & Combinación de acciones \\\\ \n")
ftex.write('\\hline \n')
ftex.write("\\endhead  \n")

ftex.write("\\hline \\multicolumn{2}{|r|}{Continúa en la siguiente página} \\\\ \\hline \n \\endfoot \n \\hline \n \\endlastfoot  \n ")

cont=1
for lc in SLSqperm:
    f.write('combContainer.SLS.qp.add("ELSQP' +str(cont).rjust(3,'0') + '" , "'+ lc.name +'") \n')
    ftex.write('ELSQP' +str(cont).rjust(3,'0') +' & ' + lc.descripcion + ' \\\\ \n')
    cont+=1
ftex.write('\\end{longtable} \n')
ftex.write('\\end{center} \n \n \n')


f.close()
ftex.close()

