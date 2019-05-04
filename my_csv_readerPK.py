#!/usr/bin/env python

import os

file_path = 'wine.data'

if os.path.isfile('./wine.data'):
    print('I have a valid file!!!')
else:
    print('Invalid file, I\'ll crash')

file = open('wine.data')

for line in file.readlines():
    replaced_line=line.strip().replace('  ', ' ').replace('  ', ' ')
    split_line=replaced_line.split(' ')
    print(split_line)
    rebuilt_line=[]
    for value in split_line:
       print(value)
