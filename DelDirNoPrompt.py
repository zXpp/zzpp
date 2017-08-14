# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 16:48:41 2017

@author: z81022868
"""
#this script is to delete the whole dirpath and files(if have) included without no prompt.
import os
def removeDir(dirPath):#list type
    if not os.path.isdir(dirPath):
        return
    files = os.listdir(dirPath)
    try:
        for file in files:
            filePath = os.path.join(dirPath, file)
            if os.path.isfile(filePath):
                os.remove(filePath)
            elif os.path.isdir(filePath):
                removeDir(filePath)
        os.rmdir(dirPath)
    except Exception, e:
        print e

if __name__ == "__main__":
	removeDir(r'C:\Users\z81022868\Desktop\EA5800-X17(N63E-22) 快速安装指南 01\XML_799'.decode('utf-8'))