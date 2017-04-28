# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 11:27:27 2017

@author: zzpp220
"""
from __future__ import print_function
import sys
import os
#import pprint
import sklearn as sl
import numpy as np
import librosa
import librosa.feature as f
import librosa.util as lu
 
#---Feature extraction and store, including MFCC, DMFCC
def mfcclist(data_dir):
#==============================================================================
#    
#     dm = []
#==============================================================================
    concate = []
    audiofilelist=lu.find_files(data_dir,'wav')
    for wavname in audiofilelist:
        
        #filepath = os.path.join(data_dir, wavname)
        print(wavname)
        arr=mfccfile(wavname)
        mean=np.mean(arr,axis=0)
        concate.append(mean)
        np.savetxt(os.path.join(data_dir,"scut_testchain_430.pyfea"),concate,fmt='%s',newline='\n')
#==============================================================================
#         m.append(am)
#         dm.append(adm)
#         #i += 1
     
#     np.savetxt(os.path.join(data_dir,"frame_mfcc"),dm,fmt='%s',newline='\n')
#     #print(m)
#     #print(dm)
#==============================================================================
'''
    fout = open(output_file,'w')
    fout.write(str(am) + '\n')
    fout.write(str(adm))
    fout.close()
'''
 
def mfccfile(input_file):
    print('Loading ', input_file)
    y, sr = librosa.load(input_file,sr=16000,mono=True)
    M = f.mfcc(y,sr,S=None, n_mfcc=13,hop_length=int(0.01*sr),htk=True,n_mels=24)#M--D*N
    basename=input_file[input_file.rfind('/')+1:input_file.rfind('.')]
    #np.savetxt(os.path.join(datadir,basename+".pymfcc"),M.T,fmt='%s',newline='\n')
    
    print (basename+".pymfcc "," saved successfully!")
    return M.T
#==============================================================================
#     tmp1,tmp2=M[::,1::],M[::,0:-1:1]#tmp1是M缺失第一帧，tmp2是缺失第2帧
#     size1,size2=tmp1.shape,tmp2.shape
#     DM = M[::,1::] - M[::,0:-1:1]
#     am = np.mean(M, axis = 1)#样本求平均
#     adm = np.mean(DM, axis = 1)#差值求平均是什么意思
#==============================================================================
    #return (am, M.T)
 
#---Loading stored features file
def loadfeatures(features_file):
    fin = open(features_file, 'r')
    features = [map(float,ln.strip().split(' '))
                for ln in fin.read().splitlines() if ln.strip()]
                #pprint.pprint(features)
    print(features)

datadir='/media/zzpp220/Data/Linux_Documents/Mobile/ILP/chain6.0/SCUTPHONE/scut_test_chain430'
#==============================================================================
# audiofile=r'/media/zzpp220/Data/Linux_Documents/Mobile/DATA/CV/14cellphones/WAV/HP_IPAQ514_train1.wav'
# _,Mfcc=mfccfile(audiofile)
# np.savetxt(os.path.join(datadir,"ture_mfcc.txt"),Mfcc,fmt='%s',newline='\n')
#==============================================================================
#Mfcc.tofile(os.path.join(datadir,"true_mfcc.txt"),sep=" ")
mfcclist(datadir)
