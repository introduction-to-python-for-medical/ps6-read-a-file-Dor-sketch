def create_codon_dict(filename):
    codon_dict = {}
    with open(filename, 'r') as file:
        for line in file:
            codon, amino_acid, single_letter, full_name = line.split()
            codon_dict[codon] = single_letter
    return codon_dict

