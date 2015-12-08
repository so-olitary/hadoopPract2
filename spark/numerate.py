﻿#!/usr/bin python
# -*- coding: utf-8 -*-

import codecs
import sys
import re


re_norm_url = re.compile(ur'^https?://[^/]*lenta\./|/?\r?\n?$')
def normalize(url):  return re_norm_url.sub(u'', url)


def numerate(url, urls, new_urls):
    if  url in urls:
        return unicode(urls[url])

    id = unicode(len(urls))
    new_urls.append( (id, url) )
    urls[url] = id
    return id


fn_urls = sys.argv[1]
with codecs.open(fn_urls, 'r', encoding='utf-8') as f_urls:
    splts = [ line.split(u'\t') for line in f_urls ]
    urls = dict( (normalize(url), id) for id, url in splts )


new_urls = []
# Используем unicode в стандартных потоках io
sys.stdin  = codecs.getreader('utf-8')(sys.stdin)
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
sys.stderr = codecs.getwriter('utf-8')(sys.stderr)
# type reduced | python numerate.py "C:\data\lenta.ru\all\urls.txt" "new_urls.txt" | sort > numerate
for line in sys.stdin:
    splt = line.split(u'\t')

    if  len(splt) == 3:
        v, PR,  wlinks = splt
        w_urls = wlinks.split(u'|')

        if  not unicode(v).isdigit():
            v = numerate(v, urls, new_urls)

        ws = [ numerate(url, urls, new_urls) for url in w_urls ]
        print u'%s\t%s\t%s' % ( v, PR, u','.join(ws) )

    elif  len(splt) == 5:
        v, h, a, w_links, u_links = splt
        w_urls = w_links.split(u'|')
        u_urls = u_links.split(u'|')

        if  not unicode(v).isdigit():
            v = numerate(v, urls, new_urls)

        ws = [ numerate(url, urls, new_urls) for url in w_urls ]
        us = [ numerate(url, urls, new_urls) for url in u_urls ]
        print u'%s\t%s\t%s\t%s\t%s' % (v, h, a, u'|'.join(ws), u'|'.join(us) )


fn_new_urls = sys.argv[2]
with codecs.open(fn_new_urls, 'a', encoding='utf-8') as f:
    print >>f, u''.join([ u'%s\t%s\n' % (id,url) for id,url in new_urls ])
