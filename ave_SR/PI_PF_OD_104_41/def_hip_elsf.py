# COMBINATIONS OF ACTIONS FOR SERVICEABILITY LIMIT STATES
    # name:        name to identify the combination
    # rare:        combination for a rare design situation
    # freq:        combination for a frequent design situation
    # qp:          combination for a quasi-permanent design situation
    # earthquake:  combination for a seismic design situation
#Characteristic combinations.
combContainer.SLS.rare.add("ELSR001","1.00*G1 + 1.00*C1")
combContainer.SLS.rare.add("ELSR002","1.00*G1 + 1.00*G2a + 1.00*G3 + 1.00*Q1a")
combContainer.SLS.rare.add("ELSR003","1.00*G1 + 1.00*G2a + 1.00*G3 + 1.00*Q1b")
combContainer.SLS.rare.add("ELSR004","1.00*G1 + 1.00*G2a + 1.00*G3 + 1.00*Q1c")
combContainer.SLS.rare.add("ELSR005","1.00*G1 + 1.00*G2b + 1.00*G3 + 1.00*Q1a_1via")
combContainer.SLS.rare.add("ELSR006","1.00*G1 + 1.00*G2c + 1.00*G3 + 1.00*Q1a_1via")

#Frequent combinations.
combContainer.SLS.freq.add("ELSF002","1.00*G1 + 1.00*G2a + 1.00*G3 + 0.75*Q1a")
combContainer.SLS.freq.add("ELSF003","1.00*G1 + 1.00*G2a + 1.00*G3 + 0.75*Q1b")
combContainer.SLS.freq.add("ELSF004","1.00*G1 + 1.00*G2a + 1.00*G3 + 0.75*Q1c")

#Quasi permanent combinations.
combContainer.SLS.qp.add('ELSQP001',"1.00*G1 + 1.00*G2a + 1.00*G3")
