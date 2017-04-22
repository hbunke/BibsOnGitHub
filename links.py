#!/usr/bin/env python

# Hendrik Bunke <h.bunke@zbw.eu>
# 2015-04-27

# transform simple github urls to markdown syntax
# usage: python links.py

filename = 'list.md'

with open(filename, 'r+') as f:
    lines = f.readlines()

newline = lambda li: "[{}]({})\n".format(li.strip('\n'), li.strip('\n'))
newlist = [newline(li) if li.startswith('https://github.com') else li for li in lines]

with open(filename, 'w+') as f:
    map(f.write, newlist)
