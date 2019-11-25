# -*- coding: utf-8 -*-
execfile('../model_gen.py')
resFile=workingDirectory+'results_deck/reactions/react.py'
execfile(path_loads_def+'load_state_data.py')
execfile(path_gen_results+'gen_reactions.py')
f=open(resFile,'w')
f.write('React='+repr(results)+'\n')
f.close()
