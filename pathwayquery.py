import pythoncyc
#this creates PGDB object associated with meta(MetaCyc)
meta = pythoncyc.select_organism('meta')
compound = raw_input("Enter name of compound:")
def search(compound):
    pathways = meta.pathways_of_compound(compound)
    print pathways
    return pathways
search(compound)
