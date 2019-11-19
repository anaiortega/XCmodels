# -*- coding: utf-8 -*-

f=open("resZap.tex","w")
f.write('\\begin{center} \n')
f.write('\\begin{longtable}{|l|c|rrrrrr|} \n')
f.write('\\caption{Reacciones en la base de las pilas.} \\label{reacZap}  \\\\ \n')
f.write('\\hline \n')
f.write("Acción & Pila & $F_x$ & $F_y$ & $F_z$ & $M_x$ & $M_y$ & $M_z$   \\\\ \n")
f.write(" &  & [kN] & [kN] & [kN] & [mkN] & [mkN] & [mkN]  \\\\ \n")
f.write('\\hline \n')
f.write("\\endfirsthead  \n")

f.write('\\hline \n')
f.write("Acción & Pila & $F_x$ & $F_y$ & $F_z$ & $M_x$ & $M_y$ & $M_z$   \\\\ \n")
f.write(" &  & [kN] & [kN] & [kN] & [mkN] & [mkN] & [mkN]  \\\\ \n")
f.write('\\hline \n')
f.write("\\endhead  \n")

f.write("\\hline \\multicolumn{8}{|r|}{{Continúa en la siguiente página}} \\\\ \\hline \n \\endfoot \n \\hline \n \\endlastfoot  \n ")

for lc in actRes:
    Rpil1=React[lc]['Rpilas_n1']
    Rpil2=React[lc]['Rpilas_n2']
    Rpil3=React[lc]['Rpilas_n3']
    Rpil4=React[lc]['Rpilas_n4']
    f.write(lc.replace('_','\_') + ' & P1 & '+ str(round(Rpil1[0]*1e-3,2)) + ' & '+ str(round(Rpil1[1]*1e-3,2)) + ' & '+ str(round(Rpil1[2]*1e-3,2)) + ' & ' + str(round(Rpil1[3]*1e-3,2))+ ' & ' + str(round(Rpil1[4]*1e-3,2))+ ' & ' + str(round(Rpil1[5]*1e-3,2))  + ' \\\\ \n')
    f.write( ' & P2 & '+ str(round(Rpil2[0]*1e-3,2)) + ' & '+ str(round(Rpil2[1]*1e-3,2)) + ' & '+ str(round(Rpil2[2]*1e-3,2)) + ' & ' + str(round(Rpil2[3]*1e-3,2))+ ' & ' + str(round(Rpil2[4]*1e-3,2))+ ' & ' + str(round(Rpil2[5]*1e-3,2)) + ' \\\\ \n')
    f.write( ' & P3 & '+ str(round(Rpil3[0]*1e-3,2)) + ' & '+ str(round(Rpil3[1]*1e-3,2)) + ' & '+ str(round(Rpil3[2]*1e-3,2)) + ' & ' + str(round(Rpil3[3]*1e-3,2))+ ' & ' + str(round(Rpil3[4]*1e-3,2))+ ' & ' + str(round(Rpil3[5]*1e-3,2)) + ' \\\\ \n')
    f.write( ' & P4 & '+ str(round(Rpil4[0]*1e-3,2)) + ' & '+ str(round(Rpil4[1]*1e-3,2)) + ' & '+ str(round(Rpil4[2]*1e-3,2)) + ' & ' + str(round(Rpil4[3]*1e-3,2))+ ' & ' + str(round(Rpil4[4]*1e-3,2))+ ' & ' + str(round(Rpil4[5]*1e-3,2)) + ' \\\\ \n')
    f.write('\\hline \n ')

f.write('\\end{longtable} \n')
f.write('\\end{center} \n')



f.close()

