# -*- coding: utf-8 -*-
#Reactions must be previously calculated
execfile('../model_gen.py')
execfile("../env_config_deck.py")

reacfile=fullProjPath+'results_deck/reactions/react.py'
execfile(path_loads_def+'load_state_data.py')
execfile(reacfile)
resFile=fullProjPath+'results_deck/reactions/neopr_res.tex'
f=open(resFile,"w")
execfile(path_gen_results+'text_result_neopr.py')
f.close()
