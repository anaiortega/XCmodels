# -*- coding: utf-8 -*-
execfile('../model_gen.py')
reacfile=home+'results/reactions/react.py'
execfile(path_loads_def+'load_state_data.py')
execfile(reacfile)
resFile=home+'results/reactions/neopr.tex'
f=open(resFile,"w")
execfile(path_gen_results+'text_result_neopr.py')
f.close()
