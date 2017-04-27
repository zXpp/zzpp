# -*- coding: utf-8 -*-

#Created on Wed Mar 29 21:36:40 2017

#@author: zzpp220
"""
二分类问题的评估模型即得分
"""
import numpy as np
import pandas as pd
from itertools import cycle
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve,auc,confusion_matrix,classification_report,roc_auc_score
from scipy import interp
fpr = dict()
tpr = dict()
roc_auc = dict()
n_classes=21
lw=4
truelabel_path=r"/media/zzpp220/Data/Linux_Documents/Mobile/DATA/TRAIN/Mobile_Timit/lists/"
sysout_path=r"/media/zzpp220/Data/Linux_Documents/Mobile/DATA/TRAIN/Mobile_Timit/result/kmeans-gmsv/kmeans-13-256/"
fina_sysout=np.loadtxt(sysout_path+"2520_meancen_kmean120.txt")
test_label=np.loadtxt(truelabel_path+"true_labels.lst")

#==============================================================================
# fina_sysout=np.concatenate(fina_sysout)
# fina_sysout=np.array([int(i) for i in fina_sysout])
# test_label=np.concatenate(test_label)
#==============================================================================

print confusion_matrix(test_label,fina_sysout)
print classification_report(test_label,fina_sysout)
"""
roc_auc_score 只适合二分类。所以这里不能用
print "the accuracy is : {0:.3f}%".format(roc_auc_score(test_label,fina_sysout)*100)
"""


for i in range(n_classes):
    #y_ref=np.array(pd.get_dummies(fina_sysout))[:, i]
    #y_sys=np.array(pd.get_dummies(test_label))[:, i]
    fpr[i], tpr[i], _ = roc_curve(np.array(pd.get_dummies(fina_sysout))[:, i], np.array(pd.get_dummies(test_label))[:, i])#一类一类的比较结果，得到n_Calss条roc,_代表这个变量用不到，返回3个数组.每个数组都是递增的
    roc_auc[i] = auc(fpr[i], tpr[i])
    
c=np.concatenate([fpr[i] for i in range(n_classes)])
np.unique(c)

all_fpr = np.unique(np.concatenate([fpr[i] for i in range(n_classes)]))##3个元素
mean_tpr = np.zeros_like(all_fpr)
for i in range(n_classes):
    mean_tpr += interp(all_fpr, fpr[i], tpr[i])##内插值？

mean_tpr /= n_classes

fpr["macro"] = all_fpr#fpr的均值？
tpr["macro"] = mean_tpr#tpr的均值？
roc_auc["macro"] = auc(fpr["macro"], tpr["macro"])#auc的均值？

plt.figure(figsize=(25,17))#横坐标、纵坐标
plt.plot(fpr["macro"], tpr["macro"],
         label='"macro"-average ROC curve (area = {0:0.2f})'
               ''.format(roc_auc["macro"]),
         color='purple', linestyle=':', linewidth=6)

colors = cycle(['aqua', 'darkorange', 'cornflowerblue','azure','darkgoldenrod','deeppink','mediumaquamarine','olive','saddlebrown','yellowgreen'])#3类
for i, color in zip(range(n_classes), colors):
    plt.plot(fpr[i], tpr[i], color=color, lw=lw,
             label='ROC curve of class {0} (area = {1:0.2f})'
             ''.format(i, roc_auc[i]))#对每一类都有一个roc曲线

plt.plot([0, 1], [0, 1], 'k--',color='red', lw=3)#lw=linewidth
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.annotate('Random Guess',(.5,.48),color='red')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic for Naive Bayes - IRIS DATASET')
plt.legend(loc="lower right")#图例，右下角
plt.show()