# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 10:49:06 2016

@author: zzpp220
"""

#!/usr/bin/env python2
#-*-encoding:utf-8-*-
## this script is used to select N wav from 2520 samples randomly,and give them index
"""os.walk(path),遍历path，返回一个对象，他的每个部分都是一个三元组,('目录x'，[目录x下的目录list]，目录x下面的文件)"""

import os
from random import sample
import shutil
def walk_dir(dir,fileinfo,destdir,concate_num,topdown=True):
    for root, dirs, files in os.walk(dir, topdown):
        slice=sample(files,concate_num)
            
        #print slice
        i=0
        for label in slice:
            #print label
            totalname=os.path.join(root,label)
            #fileinfo.write(totalname + '\n')
            fileinfo.write(label+'='+os.path.join(dir,label) + '\n')
            i+=1
            label_index=str(i).zfill(3)+'_'+label
            #totalname_index=os.path.join(destdir,label_index)
            #os.rename(totalname,totalname_index)
            os.rename(totalname,os.path.join(root,label_index))
            shutil.move(os.path.join(root,label_index),destdir)
            #shutil.move(os.path.join(root,totalname),destdir)
            
#dir = raw_input('please input the path:')
dir = r'/media/zzpp220/Data/Linux_Documents/Mobile/DATA/Total_TestData/14cellphones/WAV_14cellphones/'            
numtoconcate=432
label_set=['wind','river water','rain','male','female','gunshot','drum','bird','bass','baby','applause'] ##wenjianjia ming
#newchaindir=r'/media/zzpp220/Data/Linux_Documents/Mobile/ILP/audio/cv/wav'
newchaindir=r'/media/zzpp220/Data/Linux_Documents/Mobile/ILP/chain6.0/14cellphones/cells_test_chain'+str(numtoconcate)
listname=os.path.join(newchaindir,'sample_list'+str(numtoconcate)+r'.txt')
fileinfo = open(listname,'w',0)

#for type in label_set:
#    

#    

walk_dir(dir,fileinfo,newchaindir,numtoconcate)
fileinfo.close()