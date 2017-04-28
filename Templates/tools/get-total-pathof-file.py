# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 15:58:15 2016

@author: zzpp220
"""

import os
path=r'/media/zzpp220/Data/Linux_Documents/Mobile/ILP/audio/train/wav'
listname=os.path.join(path,'sample_list.txt')
with open(listname,'a+',0) as fileinfo:
    for root,dirs,files in os.walk(path):
        for label in files:
            fileinfo.write(label+'='+os.path.join(root,label) + '\n')