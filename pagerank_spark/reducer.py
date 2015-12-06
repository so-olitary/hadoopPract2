﻿#!/usr/bin python
# -*- coding: utf-8 -*-
import codecs
import sys
import re

# Используем unicode в стандартных потоках io
sys.stdin  = codecs.getreader('utf-8')(sys.stdin)
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
sys.stderr = codecs.getwriter('utf-8')(sys.stderr)

# format:  v h a ws us
# format:  v pr ws
prev_v = None
ws, us = [], []
# type mapped | python reducer.py | sort > reduced
for line in sys.stdin:
    splt = line.rstrip('\n').split('\t')

    if  len(splt) == 2:

        key, val = splt
        v, cmd = key.split('|') 

        # print >>sys.stderr, cmd, v
        if  prev_v and prev_v != v:
            # print >>sys.stderr, prev_v, len(ws), len(us) # , ws, us
            print u'%s\t%.2f\t%s'       % (prev_v, 0.15, '|'.join(ws) )
            print u'%s\t%d\t%d\t%s\t%s' % (prev_v, 1, 1, '|'.join(ws), '|'.join(us) )
            ws, us = [], []

        if   cmd == 'frw': ws.append(val)
        elif cmd == 'rev': us.append(val)
        prev_v = v

