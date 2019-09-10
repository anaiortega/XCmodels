# -*- coding: utf-8 -*-
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

for lc in resLoadCases_neopr:
    text=lc.loadCaseName.replace('_','\_')
    print text
    for i in range(len(neopsE1)):
        defN=React[lc.loadCaseName]['neoprStrain_e'+str(i+1)]
        tensN=(defN[2]/hNetoNeopr)*Eneopr #sigmaz en MPa (E_neopreno=600MPa)
        text+=' & N' + str(i+1)+' & '+ str(round(defN[0]*1e3,2)) + ' & '+ str(round(defN[1]*1e3,2)) + ' & '+ str(round(defN[2]*1e3,2)) + ' & ' + str(round(defN[3]*1e3,2))+ ' & ' + str(round(defN[4]*1e3,2))+ ' & ' + str(round(defN[5]*1e3,2)) + ' & '+ str(round(tensN*1e-6,2)) + ' \\\\ \n'
        f.write(text)
        text=''
    f.write('\\hline \n ')

f.write('\\end{longtable} \n')
f.write('\\end{center} \n')


