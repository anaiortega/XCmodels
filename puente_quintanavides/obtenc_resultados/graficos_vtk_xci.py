
exec(open('vtk/vtk_crea_array_set_data_xcm.py').read())
exec(open('obtenc_resultados/dibuja_malla_cad_xci.py').read())
exec(open('obtenc_resultados/dibuja_malla_elementos_xci.py').read())

'''
VtkCargas("NV","renderer",[1,0,1],2)
VtkCargas("VTY","renderer",[0,1,1],2)}
'''

exec(open('vtk/vtk_vista_yneg.lcmm').read())
exec(open('vtk/vtk_muestra_ventana.lcmm').read())
