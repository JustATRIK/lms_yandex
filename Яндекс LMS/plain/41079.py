def molecule_assembly(*args, overwrite=False):
    global molecule_dna, dna_chain
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

    if len(args) >= 2:
        data = args[0]
        new_dna = args[1]
        if overwrite:
            dna_chain = new_dna
        else:
            dna_chain += new_dna
    elif len(args) == 1:
        data = args[0]
    else:
        return [f"{p[0]}{p[1]}" for p in molecule_dna]
    
    if len(args) >= 1:
        data_available = args[0]
        while dna_chain and data_available:
            current_nuc = dna_chain[0]
            comp = complement.get(current_nuc, None)
            if comp is None:
                break
            if comp in data_available:
                data_available.remove(comp)
                molecule_dna.append((current_nuc, comp))
                dna_chain = dna_chain[1:]
            else:
                break

    return [f"{pair[0]}{pair[1]}" for pair in molecule_dna]
    