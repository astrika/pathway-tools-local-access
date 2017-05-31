import pythoncyc
#this creates PGDB object associated with meta(MetaCyc)
meta = pythoncyc.select_organism('meta')
pathways = meta.pathways_of_compound('urea')
print pathways

"""
Query output:
$ python pathwayquery.py
[u'|PWY-40|', u'|POLYAMSYN-PWY|', u'|ARG+POLYAMINE-SYN|', u'|PWY0-823|', u'|ARGDEG-PWY|', u'|ORNARGDEG-PWY|', u'|PWY-5705|', u'|PWY-4741|', u'|PWY-5697|', u'|PWY-5694|', u'|P165-PWY|', u'|PWY-5679|', u'|PWY-5024|', u'|PWY-31|', u'|PWY-6426|', u'|PWY-7523|', u'|PWY-5742|', u'|ARGDEG-IV-PWY|', u'|ARGDEG-V-PWY|', u'|PWY-6922|', u'|CITRULBIO-PWY|', u'|ARGASEDEG-PWY|', u'|PWY-6305|', u'|ARG-GLU-PWY|', u'|ARG-PRO-PWY|', u'|PWY-4984|', u'|PWY-5004|', u'|PWY-6834|', u'|CRNFORCAT-PWY|', u'|PWY-5704|', u'|URDEGR-PWY|', u'|PWY-5703|', u'|ALLANTOINDEG-PWY|']
"""
