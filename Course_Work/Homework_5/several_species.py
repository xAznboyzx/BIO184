#Single gene in order of: Species name, sequence, gene name, expression level


data=open("data.csv")
for gene_names in data:
    order=gene_names.replace("\n","").split(",") # Removes white space for each line and splits commas into a list
    species_name=order[0]   
    sequence=order[1]
    gene_name=order[2]
    expression_level=order[3]
    if species_name == "Drosophila melanogaster" or species_name == "Drosophila simulans":
        print(gene_name)
    else:
        pass


      