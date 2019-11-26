# -*- coding: utf-8 -*-
#Reactions must be previously calculated
execfile('../env_config.py')
lsd.LimitStateData.envConfig= cfg
execfile("../env_config_deck.py")
execfile('../data_deck_piers.py')
reacfile=workingDirectory+'results_deck/reactions/react.py'
execfile(reacfile)
resFile=workingDirectory+'results_deck/reactions/neopr_verif.tex'
f=open(resFile,"w")


#Data
n_capas=4  #nº de capas de neopreno en cada apoyo
t_capa=8e-3 #espesor de cada capa de neopreno
thetax0=0.003 #giro mínimo considerado para absorber la falta de paralelismo tablero-apoyos

#Cargas permanentes para combinación de presión vertical mínima
CP_sgz_min=['G1']
#Cargas permanentes para combinación de presión vertical máxima
CP_sgz_max=['G1','G2']
#SC uso para combinación de presión vertical máxima
SC_uso_sgz_max=['Q1e']
#Viento  para combinación de presión vertical máxima
W_sgz_max=['Q21']

#Cargas permanentes para combinación de desplazamiento u_y máximo
CP_uy_max=['G1','G2','G4']
#SC uso para combinación de desplazamiento u_y máximo (cargas rápidas)
SC_uso_uy_max_rap=['Q1eFren','Q4']
#Cargas lentas para combinación de desplazamiento u_y máximo
Qlenta_uy_max=['Q32neopr']

#Cargas para combinación de giro máximo (theta_x)
C_tetax_max=['G1','G2','Q1bFren']
#End data

execfile(path_gen_results+'text_verif_neopr.py')
f.close()
