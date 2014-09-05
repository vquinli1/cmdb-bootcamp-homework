#!/usr/bin/env python

"""
Modified from FASTA parser built morning of day 3
Returns tuples of (sid, sequence) for the 100 longest sequences in ascending order
"""

import sys
from fasta import FASTAReader
        
reader = FASTAReader(sys.stdin) 

for sid,sequence in reader: 
   def sort_key(item):
       return len(item [1])
   
   longest = sorted(reader, key = sort_key)[-100:]
   print longest