inst_root= '/opt/salome'
python_version= '2.7'
med_root_dir= inst_root + '/MED_7.5.1'
medfile_root_dir= inst_root + 'med-3.0.8'
ld_library_path= medfile_root_dir + '/lib'
ld_library_path+= ':' + med_root_dir + '/lib/salome'
pythonpath= medfile_root_dir+ '/lib/python'+ python_version + '/site-packages'
pythonpath+= ':' + med_root_dir + '/bin/salome'
pythonpath+= ':' + med_root_dir + '/lib/salome'
pythonpath+= ':' + med_root_dir + '/lib/python' + python_version + '/site-packages/salome'
