# -*- coding: utf-8 -*-

f=open("resNeopr.tex","w")
f.write('\\begin{center} \n')
f.write('\\begin{longtable}{|l|c|rrrrrr|r|} \n')
f.write('\\caption{Aparatos de apoyo. Deformaciones y tensiones.} \\label{defNeop}  \\\\ \n')
f.write('\\hline \n')
f.write("Acción & Neopr. & $u_x$ & $u_y$ & $u_z$ & $\\theta_x$ & $\\theta_y$ & $\\theta_z$ & $\\sigma_z$  \\\\ \n")
f.write(" &  & [mm] & [mm] & [mm] & $\\times 10^{-3}$ [rad] & $\\times 10^{-3}$[rad] & $\\times 10^{-3}$[rad] &  [MPa] \\\\ \n")
f.write('\\hline \n')
f.write("\\endfirsthead  \n")

f.write('\\hline \n')
f.write("Acción & Neopr. & $u_x$ & $u_y$ & $u_z$ & $\\theta_x$ & $\\theta_y$ & $\\theta_z$ &  $\\sigma_z$  \\\\ \n")
f.write(" &  & [mm] & [mm] & [mm] & $\\times 10^{-3}$ [rad] & $\\times 10^{-3}$[rad] & $\\times 10^{-3}$[rad] &  [MPa]  \\\\ \n")
f.write('\\hline \n')
f.write("\\endhead  \n")

f.write("\\hline \\multicolumn{9}{|r|}{{Continúa en la siguiente página}} \\\\ \\hline \n \\endfoot \n \\hline \n \\endlastfoot  \n ")

for lc in actResNeopr:
    defN1=React[lc]['neoprStrain_e1']
    defN2=React[lc]['neoprStrain_e2']
    defN3=React[lc]['neoprStrain_e3']
    defN4=React[lc]['neoprStrain_e4']
    tensN1=(defN1[2]/hNetoNeopr)*600 #sigmaz en MPa (E_neopreno=600MPa)
    tensN2=(defN2[2]/hNetoNeopr)*600
    tensN3=(defN3[2]/hNetoNeopr)*600
    tensN4=(defN4[2]/hNetoNeopr)*600
    f.write(lc.replace('_','\_') + ' & N1 & '+ str(round(defN1[0]*1e3,2)) + ' & '+ str(round(defN1[1]*1e3,2)) + ' & '+ str(round(defN1[2]*1e3,2)) + ' & ' + str(round(defN1[3]*1e3,2))+ ' & ' + str(round(defN1[4]*1e3,2))+ ' & ' + str(round(defN1[5]*1e3,2)) + ' & '+ str(round(tensN1,2)) + ' \\\\ \n')
    f.write( ' & N2 & '+ str(round(defN2[0]*1e3,2)) + ' & '+ str(round(defN2[1]*1e3,2)) + ' & '+ str(round(defN2[2]*1e3,2)) + ' & ' + str(round(defN2[3]*1e3,2))+ ' & ' + str(round(defN2[4]*1e3,2))+ ' & ' + str(round(defN2[5]*1e3,2)) + ' & '+ str(round(tensN2,2)) + ' \\\\ \n')
    f.write( ' & N3 & '+ str(round(defN3[0]*1e3,2)) + ' & '+ str(round(defN3[1]*1e3,2)) + ' & '+ str(round(defN3[2]*1e3,2)) + ' & ' + str(round(defN3[3]*1e3,2))+ ' & ' + str(round(defN3[4]*1e3,2))+ ' & ' + str(round(defN3[5]*1e3,2)) + ' & '+ str(round(tensN3,2)) + ' \\\\ \n')
    f.write( ' & N4 & '+ str(round(defN4[0]*1e3,2)) + ' & '+ str(round(defN4[1]*1e3,2)) + ' & '+ str(round(defN4[2]*1e3,2)) + ' & ' + str(round(defN4[3]*1e3,2))+ ' & ' + str(round(defN4[4]*1e3,2))+ ' & ' + str(round(defN4[5]*1e3,2)) + ' & '+ str(round(tensN4,2)) + ' \\\\ \n')
    f.write('\\hline \n ')

f.write('\\end{longtable} \n')
f.write('\\end{center} \n')



f.close()

