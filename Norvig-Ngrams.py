"""
Code to accompany the chapter "Natural Language Corpus Data"
from the book "Beautiful Data" (Segaran and Hammerbacher, 2009)
http://oreilly.com/catalog/9780596157111/

Code copyright (c) 2008-2009 by Peter Norvig

You are free to use this code under the MIT licencse: 
http://www.opensource.org/licenses/mit-license.php
"""

import re, string, random, glob, operator, heapq
from collections import defaultdict
from math import log10

def edits(word, d=2): 
    "Return a dict of {correct: edit} pairs within d edits of word." 
    results = {} 
    def editsR(hd, tl, d, edits): 
        def ed(L,R): return edits+[R+'|'+L] 
        C = hd+tl 
        if C in Pw: 
            e = '+'.join(edits) 
            if C not in results: results[C] = e 
            else: results[C] = max(results[C], e, key=Pedit) 
        if d <= 0: return 
        extensions = [hd+c for c in alphabet if hd+c in PREFIXES] 
        p = (hd[-1] if hd else '<') # previous character 
        # Insertion 
        for h in extensions: 
            editsR(h, tl, d-1, ed(p+h[-1], p)) 
        if not tl: return 
        # Deletion 
        editsR(hd, tl[1:], d-1, ed(p, p+tl[0])) 
        for h in extensions: 
            if h[-1] == tl[0]: # Match 
                editsR(h, tl[1:], d, edits) 
            else: # Replacement 
                editsR(h, tl[1:], d-1, ed(h[-1], tl[0])) 
        # Transpose 
        if len(tl)>=2 and tl[0]!=tl[1] and hd+tl[1] in PREFIXES: 
            editsR(hd+tl[1], tl[0]+tl[2:], d-1, 
                   ed(tl[1]+tl[0], tl[0:2])) 
    # Body of edits: 
    editsR('', word, d, []) 
    return results 

PREFIXES = set(w[:i] for w in Pw for i in range(len(w) + 1)) 
