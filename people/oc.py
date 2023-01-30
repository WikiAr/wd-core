#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

"""
#
# (C) Ibrahem Qasim, 2022
#
#
import codecs
import unicodedata
#---
from people.occupationsall import translationsOccupations as old
from people.occupationsall import translationsOccupations_new as old2
from people.occupationsall_new import translationsOccupations as new2
#---
gaga = '''
        '%s': %s,'''
#---
for x in new2:
    if not x in old and  not x in old2:
        #print("            'ar': { 'male': '%s ~', 'female': '%s ~' },\n" % ( ar2 , ar2 ) )
        print( "        '%s': {" % x )
        gagee = str(new2[x]).replace("{'en':" , "'en':").replace("}}" , "}").replace("}," , "},\n            ")
        print( '            ' + gagee )
        print( '        },' )
#---
print('==================')
#---
for x in new2:
    if x in old and new2[x] != old[x]:
        #print("            'ar': { 'male': '%s ~', 'female': '%s ~' },\n" % ( ar2 , ar2 ) )
        print( x )
        print( new2[x] )
        print( '33333333' )
#---
#---