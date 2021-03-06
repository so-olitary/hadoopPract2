﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys
import operator
import itertools
import collections

# reducer

def kkey(d):
    return d.split('\t')[0]

for key, group in itertools.groupby([line.strip() for line in sys.stdin], kkey):    
    dic = collections.defaultdict(int)
    for g in group:
        fields = re.split('\t|:', g)        
        field_i1, field_i2 = fields[1], fields[2]
        dic[field_i2] += 1

    sorted_dic = sorted(dic.items(), key=operator.itemgetter(1))

    n = len(dic)
    count_unique = n 
    min  = sorted_dic[ 0][1] 
    mid  = sorted_dic[int(n/2)][1] 
    max  = sorted_dic[-1][1] 
    mean = (sum(   float(v)  for v in dic.values() ) / n)
    devi = (sum( (v-mean)**2 for v in dic.values() ) / n) ** 0.5

    print '%s\t%s\t%s\t%s\t%s\t%s\t%s' % (field_i1, count_unique, min, mid, max, mean, devi)


