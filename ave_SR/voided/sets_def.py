pilas=pilasBarlov+pilasSotav
pilas.description='Pilas'
pilas.color=cfg.colors['brown03']

pilasInf=gridPil.getSetLinOneXYZRegion(((xPil[0],yPil[0],-hTotPilas),(xPil[-1],yPil[-1],zInfPilas)),'pilasInf')
pilasInf.description='Pilas, zona inferior'
pilasInf.color=cfg.colors['brown04']
pilasSup=gridPil.getSetLinOneXYZRegion(((xPil[0],yPil[0],zInfPilas),(xPil[-1],yPil[-1],zLosInf)),'pilasSup')
pilasSup.description='Pilas, zona superior'
pilasSup.color=cfg.colors['brown01']

