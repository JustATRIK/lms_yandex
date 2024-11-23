def change():
    prince_new = prince.copy()
    pauper_new = pauper.copy()
    prince.clear()
    prince.extend(pauper_new)
    pauper.clear()
    pauper.extend(prince_new)

# pauper = []
# prince = []
