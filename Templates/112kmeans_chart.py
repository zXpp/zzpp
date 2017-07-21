#!/usr/bin/python
# this script is to compute the acp asp  k of the result from k-means 
# YOU NEED GO TO THE DIRECTpath of the res.txt to use this script ,or the kfile will meet error!!!
import numpy as np
#from pyh import *
import os,os.path,sys,operator
#from pandas import Series
from pandas import DataFrame

def k_value(i):    
    label='shuf-208-500-500-26-21-26-256-'+str(i)
    clu = os.path.join(clu_base,str(i),label+'-clu.txt')
    f = open(clu,'r')
    clu_basename=os.path.basename(clu)
    clu_dir=os.path.dirname(clu)
    clures = clu_basename[0 : clu_basename.find('.')]
    cluresname=clures+'.res' #630_21.res
    njname=clures+'.k.res' 
    chart_file=os.path.join(clu_dir,clures+'.xls')#630_21.k.res
    f3=open(os.path.join(clu_dir,njname),'wa')
    f2=open(os.path.join(clu_dir,cluresname),'wa')
    fid=f.readlines()
    list1,y,ind_col,col_col=[],[],[],[]
    #import crash_on_ipy 
    #N=2520 #total sample number
    N=2520
    #num_sample=120    ###CHANGE WITH YOUR NUMBER OF SAMPLES IN EACH MODEL sample number of each spker
    num_sample=120
    PI=[] #21 acp
    ACP=0.0
    data={}
    for i in range(0,modelnum): #21 spkers0-20
    	p=i+1
    	count_dict = {}
    	
    	f2.write("----------------\n")
    	f2.write("model_NUM:%d\n" %i)
    	for line in fid[num_sample*i:num_sample*p]:	#spker sample 	
    		line = line.strip().zfill(3)
    		count = count_dict.setdefault(line, 0)
    		count += 1
    		count_dict[line] = count
    	###sorted_count_dict =[('3', 12), ('15', 10), ('9', 4), ('2', 4)]
    	#
    	sorted_count_dict = sorted(count_dict.iteritems(), key=operator.itemgetter(1), reverse=True)
    	data.setdefault(str(i).zfill(3),0)
    	data[str(i).zfill(3)]=count_dict
    	print "------->"
    	print sorted_count_dict #an value ni xu 
    	#comPUTE ACP
    	
    	p_i=0.0
    	n_i=num_sample
    	for num in range(len(sorted_count_dict)):
    		print sorted_count_dict[num][1]
    		p_i += (sorted_count_dict[num][1] ** 2.0)/float(n_i **2.0)
    	#sum_i=p_i
    	print p_i
    	#PI[i] +=( p_i *n_i )
    	#print ACP[i]
    	#ACP=ACP/N
    	PI.insert(i,p_i*n_i)
    	maxnum=sorted_count_dict[0][1]
    	#print maxnum
    	list1.append(sorted_count_dict[0][0])	 #get the max number
    	clu_percent=maxnum/float(num_sample)
    	f2.write("max cluster:******************%s ***********%s/%s =%r\n"% (sorted_count_dict[0][0],sorted_count_dict[0][1],num_sample,format(clu_percent,'-6.2%')))
    	for item in sorted_count_dict:
    		f2.write( "%s ------> %d\n" % (item[0], item[1]))
    		y.append((int(item[0]),item[1]))	
    	f2.write("******** ***** *********\n")
    	f2.write(" \n")
    	ind_col+=[str(i)]
    	col_col+=[str(i+1)]
    #==============================================================================
    chart=DataFrame(data)
    chart=chart.dropna(how='all')
    chart=chart.stack().unstack(level=0)
    #chart.columns=[str(n) for n in range(1,(len(chart.columns)+1))]
    #chart.index=[str(m) for m in range(modelnum)]
    fchart=open(chart_file,'wb')
    fchart.close()
    chart.to_excel(chart_file,encoding='utf8')
     
    #==============================================================================
    #print chart
    #==============================================================================
    # wb = xlwt.Workbook()
    # ws = wb.add_sheet('A Test Sheet')
    # ws.write(chart)
    #wb.save('example.xls')
    #==============================================================================
    
    
    
    ACP=sum(PI)/N
    print PI
    #print ACP	
    list2=set(list1)
    list2count=len(list2)
    #print list2count
    accur=float(list2count)/modelnum
    f2.write("the total cluster is %d\n"% list2count)
    f2.write("the accur is******%s/%s**************%r\n"% (list2count,modelnum,format(accur,'-6.2%')))
    
    
    ## comptut asp
    #print sorted(y)	
    dict={}
    dict2={}
    tmp_tm=[]
    for tup in sorted(y):
    	#print tup
    	#f3.write("%s ------> %d\n" % (tup[0], tup[1]))
    	t_s,t_m,t1=0,0,0
    	#if tup[0] in tmp: 
    	if tup[0] in dict.keys():
    		dict[tup[0]] += tup[1]	
    		t1 = dict[tup[0]] 
    		
    		t_m +=t1 **2.0
    		tmp_tm.append(t_m)
    		#print "--%d"%(t_m)	
    	else:
    		dict[tup[0]]=tup[1]
    		t1=dict[tup[0]] 
    		t_m = (t1 ** 2.0)
    		#tmp_tm.append(t_m)
    		#print "--%d"%(t_m)
    	if tup[0] in dict2.keys():
    		dict2[tup[0]] += (tup[1] **2.0)	
    		t_s = dict2[tup[0]]
    		#print "***ts:%d"%(t_s)	
    	else:
    		dict2[tup[0]]=tup[1] **2.0
    		t_s=dict2[tup[0]]
    		#print "***ts:%d"%(t_s)	
    #print tmp_tm
    dict3={}
    dict4={}
    for tup1 in dict.items():
    	#if tup1[0] in dict3.keys():
    	dict3[tup1[0]]=dict2[tup1[0]]/(dict[tup1[0]] ** 2.0)
    	dict4[tup1[0]]=(dict3[tup1[0]]*dict[tup1[0]])/N ##asp
    	f3.write("%s ------> %d\n" % (tup1[0], dict[tup1[0]]))
    #print dict
    #print dict2
    #print dict3
    #print dict4
    N_sys=dict.values()
    f3.write("N=:%d\n" % sum(N_sys))
    asp=dict4.values()
    print asp
    ASP=sum(asp)
    K = np.sqrt(ACP*ASP)
    f3.write("ACP=:%r\n" % format(ACP,'-6.2%'))
    f3.write("ASP=:%r\n" % format(ASP,'-6.2%'))
    f3.write("K=:%r\n" % format(K,'-6.2%'))
    kfile="K=:"+format(K,'-6.2%')+clures+".empty"
    f4=open(os.path.join(clu_dir,kfile),'wa')
    f4.close
    #print k
    f3.close()
    f2.close()
    f.close()


brandnamelist=["Apple_iPhone5","HTC_Desire_c","HTC_Sensation_xe","LG_GS290","LG_L3","LG_Optimus_L5","LG_Optimus_L9","Nokia_5530","Nokia_C5","Nokia_N70","Samsung_E1230","Samsung_E2121B","Samsung_E2600","Samsung_Galaxy_GT-I9100_s2","Samsung_Galaxy_Nexus_S","Samsung_Gt-I8190_mini","Samsung_Gt-N7100","Samsung_S5830i","Sony_Ericson_c510i","Sony_Ericson_c902","Vodafone_joy_845"]
#import crash_on_ipy 
#if len(sys.argv) != 5:
#     print "------------------------------------------------"
#     print "\nUSAGE: python  script.py cluster_labels.txt_file totalnums eachspknums spknums"
#     print "\nexample: python 112kmeans_needchange.py ~/DATA/TRAIN/cluster_labels.txt 2520 120 21"
#     print "\n---------- Error!! --------------------------------------"
#     sys.exit()
#coding=utf-8
#rootdir='/home/zzpp220/DATA/TRAIN/630/630clu_/'
#for parent,dirnames,filenames in os.walk(rootdir):
#	#print filenames
#	for clu in filenames:
#		print clu
modelnum=21#the speaker type)
set_clusters=[23,17,16,20,19,15,22]
clu_base='/media/zzpp220/Data/Linux_Documents/Mobile/DATA/TRAIN/Mobile_Timit/result/kmeans-dnn/208.500.500.26.21-26-256/shuf_clustercenter_test'
for i in set_clusters:
    k_value(i)