import pythoncyc
#this creates PGDB object associated with meta(MetaCyc)
meta = pythoncyc.select_organism('meta')
#prints pathways of compound specified
print meta.pathways_of_compound('thiourea')
