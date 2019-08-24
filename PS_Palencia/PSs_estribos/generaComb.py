# -*- coding: utf-8 -*-

import xc_base
import loadCombinations
from loadCombinationUtils import iap11

lcg= iap11.controlCombGenerator
#print '*******', pond.permanentActions.gammaF.getGammaFELU.desfavorable

G1=lcg.insert("IAP11","permanentes",loadCombinations.Action("G1","Peso propio"),"permanente","default")
G2=lcg.insert("IAP11","permanentes",loadCombinations.Action("G2","Carga muerta" ),"permanente","default")
G3=lcg.insert("IAP11","permanentes_nc",loadCombinations.Action("G3","Reológicas"),"permanente","nc_Reologic")
G4=lcg.insert("IAP11","permanentes_nc",loadCombinations.Action("G4","Empuje del terreno"),"permanente","nc_Terr")

Q1a_1=lcg.insert("IAP11","variables",loadCombinations.Action("Q1a_1","Tren cargas pos. A1"),"vehículos_pesados","SCuso")
Q1a_1.getRelaciones.agregaIncompatible("Q1.*")
Q1a_1.getRelaciones.agregaIncompatible("Q2_1.*")

Q1a_2=lcg.insert("IAP11","variables",loadCombinations.Action("Q1a_2","Tren cargas pos. A2"),"vehículos_pesados","SCuso")
Q1a_2.getRelaciones.agregaIncompatible("Q1.*")
Q1a_2.getRelaciones.agregaIncompatible("Q2_1.*")

Q1b_1=lcg.insert("IAP11","variables",loadCombinations.Action("Q1b_1","Tren cargas pos. B1"),"vehículos_pesados","SCuso")
Q1b_1.getRelaciones.agregaIncompatible("Q1.*")
Q1b_1.getRelaciones.agregaIncompatible("Q2_1.*")

Q1b_2=lcg.insert("IAP11","variables",loadCombinations.Action("Q1b_2","Tren cargas pos. B2"),"vehículos_pesados","SCuso")
Q1b_2.getRelaciones.agregaIncompatible("Q1.*")
Q1b_2.getRelaciones.agregaIncompatible("Q2_1.*")

Q1c=lcg.insert("IAP11","variables",loadCombinations.Action("Q1c","Tren cargas pos. C"),"vehículos_pesados","SCuso")
Q1c.getRelaciones.agregaIncompatible("Q1.*")
Q1c.getRelaciones.agregaIncompatible("Q2_1.*")

Q1d=lcg.insert("IAP11","variables",loadCombinations.Action("Q1d","Tren cargas pos. D"),"vehículos_pesados","SCuso")
Q1d.getRelaciones.agregaIncompatible("Q1.*")
Q1d.getRelaciones.agregaIncompatible("Q2_1.*")

Q1e=lcg.insert("IAP11","variables",loadCombinations.Action("Q1e","Tren cargas pos. E"),"vehículos_pesados","SCuso")
Q1e.getRelaciones.agregaIncompatible("Q1.*")
Q1e.getRelaciones.agregaIncompatible("Q2_1.*")

Q1f=lcg.insert("IAP11","variables",loadCombinations.Action("Q1f","Tren cargas pos. F"),"vehículos_pesados","SCuso")
Q1f.getRelaciones.agregaIncompatible("Q1.*")
Q1f.getRelaciones.agregaIncompatible("Q2_1.*")

Q1b_fren=lcg.insert("IAP11","variables",loadCombinations.Action("Q1b_fren","Tren cargas pos. B1 + frenado"),"vehículos_pesados","SCuso")
Q1b_fren.getRelaciones.agregaIncompatible("Q.*")

Q1d_fren=lcg.insert("IAP11","variables",loadCombinations.Action("Q1d_fren","Tren cargas pos. D + frenado"),"vehículos_pesados","SCuso")
Q1d_fren.getRelaciones.agregaIncompatible("Q.*")

Q1e_fren=lcg.insert("IAP11","variables",loadCombinations.Action("Q1e_fren","Tren cargas pos. E + frenado"),"vehículos_pesados","SCuso")
Q1e_fren.getRelaciones.agregaIncompatible("Q.*")

Q2_1=lcg.insert("IAP11","variables",loadCombinations.Action("Q2_1","Viento"),"viento_sit_persistente","SCuso")
Q2_1.getRelaciones.agregaIncompatible("Q1.*")
Q2_1.getRelaciones.agregaIncompatible("Q2_2.*")
Q2_1.getRelaciones.agregaIncompatible("Q3.*")

Q2_2=lcg.insert("IAP11","variables",loadCombinations.Action("Q2_2","Viento con SC uso"),"viento_sit_persistente","SCuso")
Q2_2.getRelaciones.agregaIncompatible("Q2_1.*")
Q2_2.getRelaciones.agregaIncompatible("Q3.*")


Q3_1=lcg.insert("IAP11","variables",loadCombinations.Action("Q3_1","Temperatura uniforme, contracción"),"termica","SCuso")
Q3_1.getRelaciones.agregaIncompatible("Q2.*")
Q3_1.getRelaciones.agregaIncompatible("Q3.*")

Q3_2=lcg.insert("IAP11","variables",loadCombinations.Action("Q3_2","Temperatura uniforme, dilatación"),"termica","SCuso")
Q3_2.getRelaciones.agregaIncompatible("Q2.*")
Q3_2.getRelaciones.agregaIncompatible("Q3.*")

Q3_3=lcg.insert("IAP11","variables",loadCombinations.Action("Q3_3","Diferencia temperatura, fibra sup. más caliente"),"termica","SCuso")
Q3_3.getRelaciones.agregaIncompatible("Q2.*")
Q3_3.getRelaciones.agregaIncompatible("Q3.*")

Q3_4=lcg.insert("IAP11","variables",loadCombinations.Action("Q3_4","Diferencia temperatura, fibra sup. más fría"),"termica","SCuso")
Q3_4.getRelaciones.agregaIncompatible("Q2.*")
Q3_4.getRelaciones.agregaIncompatible("Q3.*")

Q4=lcg.insert("IAP11","variables",loadCombinations.Action("Q4","Sobrecarga sobre relleno trasdós"),"sobrecarga_uniforme","SCuso")
Q4.getRelaciones.agregaIncompatible("Q1.*")
Q4.getRelaciones.agregaIncompatible("Q2_1.*")
Q4.getRelaciones.agregaIncompatible("Q3.*")

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

