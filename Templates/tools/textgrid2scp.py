#!/usr/bin/python
# this script is to transform TextGrid file to RTTM file

import os,sys,math


#if len(sys.argv) != 2:
#   print "\n USAGE: scriptname TextGridfile"
#   sys.exit()
#
#file1 = sys.argv[1]
path=r'/media/zzpp220/Data/Linux_Documents/Mobile/ILP/chain6.0/14cellphones/textgrid' #-----1
bn_path=r'/media/zzpp220/Data/Linux_Documents/Mobile/Auto_Code/cell/13.500.500.13/dae_bnfea/'#-----2
samplenum=408#-----3
file_label=r'cells_test_chain'+str(samplenum) #-----4
file1=os.path.join(path,file_label+r'.TextGrid')
file2 = file1
#while '/' in file2:
#    file2 = file2[file2.find('/')+1 : len(file2)]  # delete '/'
#file2 = file2[0 : file2.find('.')]
#file2name = file2
file2 =os.path.join(path,file_label+r'.scp')

f1 = open(file1, 'r')
f2 = open(file2, 'w',0)
#f2.write(';;This is an RTTM file. Each record contains 9 whitespace separated fields:\n')   # write the first line
#f2.write(';;1:type	2:file		3:chnl		4:tbe		5:tdur		6:ortho		7:subtype	8:spkrname	9:conf\n') # write the second line
#f2.write(';SPKR-INFO FileName	1	<NA>	<NA>	<NA>	unknown	SpeakerName	<NA>\n')
iter = 0
lastlabel =''
while True:
    line1 = f1.readline()
    if not line1:
        break
    elif 'intervals [' in line1:
        line2 = f1.readline()
        start_point = line2.split()[2]
        sp=int(round(float(start_point)*100))
        line3 = f1.readline()
        end_point = line3.split()[2]
        ep=int(round(float(end_point)*100)) # si she wu ru qu zhengshu bufen
        scp_sp=str(sp+1 if sp!=0 else sp)
        scp_ep=str(ep)
        f2.write(file_label+'_'+scp_sp+'_'+scp_ep+'=')
        f2.write(bn_path+file_label+r'.htk['+scp_sp+','+scp_ep+']')
        f2.write('\n')
f1.close
f2.close
