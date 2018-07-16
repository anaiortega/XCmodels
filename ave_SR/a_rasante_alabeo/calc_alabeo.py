# -*- coding: utf-8 -*-
f.write('\\begin{center}  \n')
f.write('\\begin{table}  \n')
f.write('\\begin{tabular}{|c|c|c|c|c|c|c|}  \n')
f.write('\\hline \n')
f.write('coord. $Y_1$ & coord. $Y_2$ &  $u_{z1,carr1}$ & $u_{z1,carr2}$ & $u_{z2,carr1}$ & $u_{z2,carr2}$ & Alabeo \\\\  \n')
f.write('m & m & mm & mm & mm & mm & mm  \\\\  \n')
f.write('\\hline \n')

#Resultados en vía 1
for i in range(nPoints-6):
    n1carr1=nudCarr1[i]
    n2carr1=nudCarr1[i+6]
    n1carr2=nudCarr2[i]
    n2carr2=nudCarr2[i+6]
    uz_n1carr1=n1carr1.getDisp[2] #desplazamiento vertical en m
    uz_n2carr1=n2carr1.getDisp[2] 
    uz_n1carr2=n1carr2.getDisp[2] #desplazamiento vertical en m
    uz_n2carr2=n2carr2.getDisp[2]
    p1carr1=geom.Pos3d(xCarr1,yNuds[i],uz_n1carr1)
    p2carr1=geom.Pos3d(xCarr1,yNuds[i+6],uz_n2carr1)
    p1carr2=geom.Pos3d(xCarr2,yNuds[i],uz_n1carr2)
    p2carr2=geom.Pos3d(xCarr2,yNuds[i+6],uz_n2carr2)
    plano=geom.Plane3d(p1carr1,p2carr1,p1carr2)
    alabeo=p2carr2.dist2Plano3d(plano)

    f.write(str(round(yNuds[i],2)) + ' & ' + str(round(yNuds[i+6],2)) + ' & ' +   str(round(uz_n1carr1*1e3,2)) + ' & ' +   str(round(uz_n1carr2*1e3,2)) + ' & ' +   str(round(uz_n2carr1*1e3,2)) + ' & ' +   str(round(uz_n2carr2*1e3,2)) + ' & ' +   str(round(alabeo*1e3,6)) +  '\\\\  \n')

f.write('\\hline \n')
f.write('\\end{tabular}  \n')
f.write('\\caption{Alabeo en hipótesis '+ lcname+'. Vía 1} \n')
f.write('\\label{alab'+lcname+'via1}  \n')
f.write('\\end{table}  \n')
f.write('\\end{center}  \n')

f.write('\\begin{center}  \n')
f.write('\\begin{table}  \n')
f.write('\\begin{tabular}{|c|c|c|c|c|c|c|}  \n')
f.write('\\hline \n')
f.write('coord. $Y_1$ & coord. $Y_2$ &  $u_{z1,carr3}$ & $u_{z1,carr4}$ & $u_{z2,carr3}$ & $u_{z2,carr4}$ & Alabeo \\\\  \n')
f.write('m & m & mm & mm & mm & mm & mm  \\\\  \n')
f.write('\\hline \n')

#Resultados en vía 2
for i in range(nPoints-6):
    n1carr3=nudCarr3[i]
    n2carr3=nudCarr3[i+6]
    n1carr4=nudCarr4[i]
    n2carr4=nudCarr4[i+6]
    uz_n1carr3=n1carr3.getDisp[2] #desplazamiento vertical en m
    uz_n2carr3=n2carr3.getDisp[2] 
    uz_n1carr4=n1carr4.getDisp[2] #desplazamiento vertical en m
    uz_n2carr4=n2carr4.getDisp[2]
    p1carr3=geom.Pos3d(xCarr3,yNuds[i],uz_n1carr3)
    p2carr3=geom.Pos3d(xCarr3,yNuds[i+6],uz_n2carr3)
    p1carr4=geom.Pos3d(xCarr4,yNuds[i],uz_n1carr4)
    p2carr4=geom.Pos3d(xCarr4,yNuds[i+6],uz_n2carr4)
    plano=geom.Plane3d(p1carr3,p2carr3,p1carr4)
    alabeo=p2carr4.dist2Plano3d(plano)
    f.write(str(round(yNuds[i],2)) + ' & ' + str(round(yNuds[i+6],2)) + ' & ' +   str(round(uz_n1carr3*1e3,2)) + ' & ' +   str(round(uz_n1carr4*1e3,2)) + ' & ' +   str(round(uz_n2carr3*1e3,2)) + ' & ' +   str(round(uz_n2carr4*1e3,2)) + ' & ' +   str(round(alabeo*1e3,6)) +  '\\\\  \n')

f.write('\\hline \n')
f.write('\\end{tabular}  \n')
f.write('\\caption{Alabeo en hipótesis '+ lcname+'. Vía 2} \n')
f.write('\\label{alab'+lcname+'via2}  \n')
f.write('\\end{table}  \n')
f.write('\\end{center}  \n')
