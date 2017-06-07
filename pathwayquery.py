import sys
import pythoncyc
#this creates PGDB object associated with meta(MetaCyc)

meta = pythoncyc.select_organism('meta')
pathways = meta.pathways_of_compound(sys.argv[1])
print pathways

# compounds = meta.compounds_of_pathway('PWY-6552')
# print compounds
