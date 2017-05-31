import pythoncyc
#this creates PGDB object associated with meta(MetaCyc)
meta = pythoncyc.select_organism('meta')
pathways = meta.pathways_of_compound('urea')
print pathways
