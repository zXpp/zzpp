
# coding: utf-8

# In[6]:

import numpy as np
import pandas as pd


# In[7]:

tanic=pd.read_csv("titanic_train.csv")
tanic.head()#默认显示前5行


# In[8]:

"""
数据预处理：包括数据清洗，丢掉脏数据，填充缺失值，数值转换（映射）等。
"""
#第一步：检查各列特征下是否有缺失值
print tanic.describe()#按列进行统计，由age看到，714<891，数据缺失了，而其他各列的count值都是891，即没有缺失。因此要对数据进行预处理，缺失值填充-选择均值-mean填充


# In[9]:

tanic["Age"]=tanic["Age"].fillna(int(tanic["Age"].mean()))#这里age是int类型，可以选用中位数median，也可以选平均数近似为29
##！注意，fillna 并不是原地修改，而是返回一个新的值，因此要将新的赋值给原来旧的
print tanic.describe() #只会显示该列的取值为数值型的统计数据，字符型等其他非数值性的则不会显示
#由describe可知各列无缺失值，都是891


# In[10]:

print int(tanic["Age"].mean()),tanic["Age"].median()


# In[11]:

help(tanic["Age"].mean)


# In[12]:

help(tanic["Age"].median)


# In[13]:

"""
接下来要研究哪些特征影响该样本能否获救，这些特征的影响程度是怎样的，那个最大？
显然，这是一个分类问题，二分类。
第二步：将案例中的各特征的样本值转化为可以用计算机语言、模型处理的值的形式，例如将str类型转换为int型，即数值转换。
先扫描一遍那些特征的取值是非数值，特征取值一共哟哪几种，为这些取值分别做一个非数值性到数值型的映射。
"""


# In[14]:

#首先看性别,取值只有两种，且为str类型
print tanic["Sex"].unique()
#性别各取值的人数分布。男的比女的多
tanic["Sex"].groupby(tanic["Sex"]).value_counts()


# In[15]:

#数值转化 
help(tanic.loc)


# In[16]:

#定位SEX属性的行，并且做数值映射 ，替换原来的值.loc[row_indexer,col_indexer] = value instead
#需要先定位约束条件，才能修改该约束条件下的某个值
tanic.loc[tanic["Sex"]=="male","Sex"]=0
tanic.loc[tanic["Sex"]=="female","Sex"]=1
tanic["Sex"].unique()
#看如下结果，修改完成


# In[17]:

#还有Embarked 列。代表登船地点，同样的方法处理
tanic["Embarked"].unique()#array(['S', 'C', 'Q', nan], dtype=object)
#发现有缺失值，首先进行填充，--看各其他取非nan值的分布--groupby
tanic["Embarked"].value_counts(dropna=False)#不要扔掉nan
"""
S      644
C      168
Q       77
NaN      2
Name: Embarked, dtype: int64

将nan的样本用最多的取值“S”进行填充
"""
tanic["Embarked"]=tanic["Embarked"].fillna("S")#将填充后的列替换填充前的列
#填充完缺失值再进行数值映射，替换原来的值
tanic.loc[tanic["Embarked"]=="S","Embarked"]=0
tanic.loc[tanic["Embarked"]=="C","Embarked"]=1
tanic.loc[tanic["Embarked"]=="Q","Embarked"]=2
tanic["Embarked"].unique()
#替换完成


# In[18]:

"""
接下来，选取用来进行分类的样本特征以及分类器建立模型
"""
#首先选择表中最直接观测可以作为特征的属性，浅层的，不涉及特征的组合和特征选择
features=["Pclass","Sex","Age","SibSp","Parch","Fare","Embarked"]
from sklearn.linear_model import LinearRegression#引入线性回归模型
from sklearn.cross_validation import KFold #引入K折交叉验证

line_model=LinearRegression()#初始化线性回归模型对象
#sklearn.cross_validation.KFold(n=4, n_folds=2, shuffle=False,random_state=None)

print tanic[features].shape #返回（行数，列数）

kf=KFold(tanic[features].shape[0],n_folds=5,random_state=1)#输入样本数、要将训练集分为几分
#每一次都会训练模型，一共5次，最后的结果是5次结果的平均。
print len(kf)


# In[19]:

help(tanic.iloc)#按照下标进行定位


# In[20]:

print tanic[features]


# In[21]:

pred_score=[]#存放每次交叉验证的结果,
'''注意 这次并没哟真正意义上的测试数据，整个列表看做训练数据的话。交叉验证只是为了让模型的训练误差尽量小，
。训练好的 的模型并没哟真正用到独立与整个训练集的测试集。
'''
for train ,test in kf:#每次都要训练模型
    
    train_features=tanic[features].iloc[train,:]#在所有样本上述特征中取出train的样本特征【row_index,col_indexer】
    train_label=tanic["Survived"].iloc[train] #取出上面训练样本特征对应的标签
    line_model.fit(train_features,train_label)#训练模型
    test_sysout=line_model.predict(tanic[features].iloc[test,:])#本次的测试集上应用模型，得到系统输出,是一个数组
    pred_score.append(test_sysout)#将每一次的测试结果收集。
    


# In[22]:

print [i.shape for i in pred_score]#每一组都是平均178个样本的概率值


# In[23]:

import numpy as np

help(np.concatenate)


# In[24]:

pred_score=np.concatenate(pred_score,axis=0)

pred_score


# In[25]:

#将结果数组中的概率值映射为输出。0,1.在设置阈值为0.5
threshold=0.5
pred_score[pred_score>threshold]=1
pred_score[pred_score<=threshold]=0
print pred_score.shape
print pred_score[pred_score==tanic["Survived"]].shape

accuracy=sum(pred_score[pred_score==tanic["Survived"]])/len(pred_score)#最后的结果为均值
print "accuracy_linear_regression is :",accuracy


# In[26]:

"""用逻辑回归，同时交叉验证用更方便的表示"""
from sklearn.cross_validation import cross_val_score
#cross_val_score(estimator, X, y=None, scoring=None, cv=None, n_jobs=1, verbose=0, fit_params=None, pre_dispatch='2*n_jobs')
from sklearn.linear_model import LogisticRegression

log_model=LogisticRegression()
# Compute the accuracy score for all the cross validation folds.  (much simpler than what we did before!)
log_sysout=cross_val_score(log_model,tanic[features],tanic["Survived"],cv=5)#同样有5个元素
print "accuracy_logistic_regression is :{0:.3f}%".format(log_sysout.mean())


# In[27]:

"""
改用随机森林，综合利用特征，防止过拟合
"""
from sklearn.ensemble import  RandomForestClassifier
# Initialize our algorithm with the default paramters
# n_estimators is the number of trees we want to make,随机数设置为10
# min_samples_split is 分裂一个中间结点的最小样本数，即只要该结点下的样本数大于=2就等继续分裂。#每棵树结点分裂的终止条件
# min_samples_leaf is 叶子结点中的最小样本数 (the bottom points of the tree)
ranforest_model=RandomForestClassifier(n_estimators=10,min_samples_split=2,min_samples_leaf=1)

ranforest_sysout=cross_val_score(ranforest_model,tanic[features],tanic["Survived"],cv=5,scoring="accuracy")
print "accuracy_random_forest is :{0:.3f}% ".format(ranforest_sysout.mean()*100)


# In[28]:

"""
在上述随机森林的分类器中调节参数,加大加深随机森林，结点分裂的终止条件宽松一点
"""
ranforest2_model=RandomForestClassifier(n_estimators=100,min_samples_split=5,min_samples_leaf=2)
ranforest2_sysout=cross_val_score(ranforest2_model,tanic[features],tanic["Survived"],cv=5,scoring="accuracy")
print "accuracy_random_forest--paramenter-modified is :{0:.3f}%".format(ranforest2_sysout.mean()*100)


# In[29]:

"""
------------------------------------------------------------------------------------------------------
以上是基于样本数据的原始特征应用线性回归、逻辑回归、随机森林等方法进行预测是否被救的可能性
但是实际问题中数据挖掘往往要建立以个特征工程：即在原始特征的基础上进行选择、抽取、组合出新的特征，更加综合，再进行预测
"""
#1.由兄弟姐妹、父母孩子的个数可知该家庭的总人数，可能也会影响最后获救与否，人多力量大？--生成一个家庭总人数的新特征：
tanic["FamilySize"]=tanic["SibSp"]+tanic["Parch"]

#2.从样本名字中提取新特征--可能达官贵人的名字都比较长？-----生成一个样本名字长度的新特征
tanic["NameLength"]=tanic["Name"].apply(lambda x:len(x))#对该列的每一个值求名字长度

#3.样本名字中的称谓可能叶影响-----生成获取样本名称中对应称谓的新特征
import re
#----------------------------------------------------------------------------------
#定义函数，用正则表达式获取名字中的称谓
def gettitle(name):
    title_search=re.search('([A-Za-z]+)\.',name)#捕获一个子表达式
    #注意 search和findall 不一样，search是找到一个就好了。findall是找到模式匹配的全部
    title_findall=re.findall('([A-Za-z]+)\.',name)
    if title_search:
        return title_search.group(1)#返回捕获的表达式
    return ""
#----------------------------------------------------------------------------------
tanic["Title"]=tanic["Name"].apply(gettitle)
tanic["Title"].value_counts(dropna=False)#查看该特征的取值
#将特征的取值做数值转换
title_mapping = {"Mr": 1, "Miss": 2, "Mrs": 3, "Master": 4, "Dr": 5, "Rev": 6, "Major": 7, "Col": 7, "Mlle": 8, "Mme": 8, "Don": 9, "Lady": 10, "Countess": 10, "Jonkheer": 10, "Sir": 9, "Capt": 7, "Ms": 2}
for k,v in title_mapping.items():
    tanic["Title"][tanic["Title"]==k]=v
    #tanic.loc[tanic["Title"==k],"Title"]=v #会报错
print tanic["Title"].value_counts()


# In[30]:

features.extend(["FamilySize","NameLength","Title"])
"""#现在有的所有的特征如下:features 
features=['Pclass','Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked', 'FamilySize', 'NameLength', 'Title']

接下来要对特征进行衡量，那些特征有用，有用的程度是多少，那些没用？对特征进行选择，选出影响最大的几个特征，都用feature_importance量化查看
"""


# In[31]:

from sklearn.feature_selection import SelectKBest, f_classif#
import matplotlib.pyplot as plt

"""
help(SelectKBest)
Parameters
 |  ----------
 |  score_func : callable
 |      Function taking two arrays X and y, and returning a pair of arrays
 |      (scores, pvalues) or a single array with scores.
 |      Default is f_classif (see below "See also"). The default function only
 |      works with classification tasks.
 |  
 |  k : int or "all", optional, default=10
 |      Number of top features to select.
 |      The "all" option bypasses selection, for use in a parameter search.
 |  
Attributes
 |  ----------
 |  scores_ : array-like, shape=(n_features,)
 |      Scores of features.
 |  
 |  pvalues_ : array-like, shape=(n_features,)
 |      p-values of feature scores, None if `score_func` returned only scores.
 |  

"""
fea_selector=SelectKBest(f_classif,k=5)
fea_selector.fit(tanic[features],tanic["Survived"])
# Get the raw p-values for each feature, and 
print fea_selector.pvalues_,fea_selector.scores_ #总共10个特征，得到没分特征的原始P-value
scores = -np.log10(fea_selector.pvalues_)#transform from p-values into scores
print scores#这个score不是scores_


# In[32]:

#scores反映了每个特征在该分类问题的中的影响程度，用画图的方式开看更直观些
# Plot the scores.
plt.bar(range(len(features)),scores)#选择条形图。横坐标定为1-10，纵坐标对应为特征取值
plt.xticks(range(len(features)), features, rotation='vertical')#更改横坐标各个点代表的标签值
plt.show()


# In[33]:

# from the chart,Pick only the top5 features.
top5_fea = [ "Sex","Pclass", "Title","NameLength","Fare"]
#重新用该特征组合 运用随机森林
top_ranforest_model=RandomForestClassifier(n_estimators=100,min_samples_split=4,min_samples_leaf=2,random_state=1)
top_ranforest_sysout=cross_val_score(top_ranforest_model,tanic[top5_fea],tanic["Survived"],cv=5,scoring="accuracy")
print "accuracy_top_random_forest--paramenter-modified is :{0:.3f}%".format(top_ranforest_sysout.mean()*100)
#由结果可知，和之前的随机森林结果82.724相比，虽然差一点但很微小，但是特征的维度减低了一半啊，计算复杂度降低了，很实用的一个功能！！


# In[34]:

"""
使用集成学习的迭代决策树
特征不仅可以组合，也可以考虑将分类算法进行集成，综合多个分类器的优缺点

"""

from sklearn.ensemble import GradientBoostingClassifier


# In[35]:

help(GradientBoostingClassifier)
ensemble_fea=["Pclass","Sex","Age","Fare","Title","NameLength","Embarked"]
#选定特征都要永在两种算法。
gbrt_model=GradientBoostingClassifier(random_state=1,n_estimators=25,max_depth=3)
lg_model=LogisticRegression(random_state=1)
algorithm=[[gbrt_model,ensemble_fea],[lg_model,ensemble_fea]]#一行写不下分两行


# In[36]:

#自己的方法
score_gbrt=cross_val_score(gbrt_model,tanic[ensemble_fea],tanic["Survived"],cv=5,scoring="accuracy")
score_lg=cross_val_score(lg_model,tanic[ensemble_fea],tanic["Survived"],cv=5,scoring="accuracy")
score_ensemble=(score_gbrt+score_lg)/2
print "accuracy_semble_gbrt_lg is :{0:.3f}%".format(score_ensemble.mean()*100)


# In[37]:

test_tanic=pd.read_csv("test.csv")
test_tanic.describe()


# In[38]:

#测试数据预处理
test_tanic["Age"]=test_tanic["Age"].fillna(int(test_tanic["Age"].mean()))
test_tanic["Fare"]=test_tanic["Fare"].fillna(test_tanic["Fare"].median())


#定位SEX属性的行，并且做数值映射 ，替换原来的值.loc[row_indexer,col_indexer] = value instead

test_tanic.loc[test_tanic["Sex"]=="male","Sex"]=0
test_tanic.loc[test_tanic["Sex"]=="female","Sex"]=1
test_tanic["Sex"].unique()


#看如下结果，修改完成
test_tanic.head()
#test_tanic["Fare"].value_counts(dropna=False)


# In[39]:

#还有Embarked 列。代表登船地点，同样的方法处理
#test_tanic.head()
test_tanic["Embarked"].unique()#array(['S', 'C', 'Q', nan], dtype=object)
#发现有缺失值，首先进行填充，--看各其他取非nan值的分布--groupby
test_tanic["Embarked"].value_counts(dropna=False)#不要扔掉nan

#test_tanic["Embarked"]=test_tanic["Embarked"].fillna("S")#将填充后的列替换填充前的列
#填充完缺失值再进行数值映射，替换原来的值
test_tanic.loc[test_tanic["Embarked"]=="S","Embarked"]=0
test_tanic.loc[test_tanic["Embarked"]=="C","Embarked"]=1
test_tanic.loc[test_tanic["Embarked"]=="Q","Embarked"]=2
test_tanic["FamilySize"]=test_tanic["SibSp"]+test_tanic["Parch"]
test_tanic["Embarked"].unique()
#test_tanic.head()
#替换完成


# In[40]:

"""
------------------------------------------------------------------------------------------------------
以上是基于样本数据的原始特征应用线性回归、逻辑回归、随机森林等方法进行预测是否被救的可能性
但是实际问题中数据挖掘往往要建立以个特征工程：即在原始特征的基础上进行选择、抽取、组合出新的特征，更加综合，再进行预测
"""
#1.由兄弟姐妹、父母孩子的个数可知该家庭的总人数，可能也会影响最后获救与否，人多力量大？--生成一个家庭总人数的新特征：
#tanic["FamilySize"]=tanic["SibSp"]+tanic["Parch"]

#2.从样本名字中提取新特征--可能达官贵人的名字都比较长？-----生成一个样本名字长度的新特征
test_tanic["NameLength"]=test_tanic["Name"].apply(lambda x:len(x))#对该列的每一个值求名字长度

#3.样本名字中的称谓可能叶影响-----生成获取样本名称中对应称谓的新特征
'''import re
#----------------------------------------------------------------------------------
#定义函数，用正则表达式获取名字中的称谓
def gettitle(name):
    title_search=re.search('([A-Za-z]+)\.',name)#捕获一个子表达式
    #注意 search和findall 不一样，search是找到一个就好了。findall是找到模式匹配的全部
    title_findall=re.findall('([A-Za-z]+)\.',name)
    if title_search:
        return title_search.group(1)#返回捕获的表达式
    return ""
#----------------------------------------------------------------------------------
'''
test_tanic["Title"]=test_tanic["Name"].apply(gettitle)
test_tanic["Title"].value_counts(dropna=False)#查看该特征的取值
#将特征的取值做数值转换
test_title_mapping = {"Mr": 1, "Miss": 2, "Mrs": 3, "Master": 4, "Dr": 5, "Rev": 6, "Major": 7, "Col": 7, "Mlle": 8, "Mme": 8, "Dona": 9, "Lady": 10, "Countess": 10, "Jonkheer": 10, "Sir": 9, "Capt": 7, "Ms": 2}

for k,v in test_title_mapping.items():
    test_tanic["Title"][test_tanic["Title"]==k]=v
    #tanic.loc[tanic["Title"==k],"Title"]=v #会报错
print test_tanic["Title"].value_counts()


# In[46]:


ensemble_sysout=[]


#视频中的方法
for alg,fea in algorithm:
    alg.fit(tanic[fea],tanic["Survived"])
     # Predict using the test dataset.  We have to convert all the columns to floats to avoid an error.
    test_sysout=alg.predict_proba(test_tanic[fea].astype(float))[:,1]
    ensemble_sysout.append(test_sysout)
print len  (ensemble_sysout)#用了两种算法的原因
fina_sysout=(ensemble_sysout[0]*3+ensemble_sysout[1])/4
fina_proba=fina_sysout


# In[55]:

#将结果数组中的概率值映射为输出。0,1.在设置阈值为0.5
#threshold=0.5
fina_sysout[fina_sysout>threshold]=1
fina_sysout[fina_sysout<=threshold]=0
print type(fina_sysout)

test_label=pd.read_csv("gender_submission.csv")
test_label=np.array(test_label["Survived"])

from sklearn import metrics
print metrics.classification_report(test_label,fina_sysout)
print metrics.confusion_matrix(test_label,fina_sysout)
#accuracy=sum(fina_sysout[fina_sysout==test_label])/len(fina_sysout)

#accuracy=sum(pred_score[pred_score==tanic["Survived"]])/len(pred_score)#最后的结果为均值
#print "accuracy_linear_regression is :",accuracy


# In[52]:

#回头看看auc,roc的值的情况
from sklearn.metrics import roc_curve,auc,roc_auc_score

print "auc: ",roc_auc_score(test_label,fina_sysout)#
print "auc: ",roc_auc_score(test_label,fina_proba)


# In[51]:

help(roc_auc_score)


# In[44]:

help(auc)


# In[45]:

help(roc_curve)


# In[47]:

fina_proba


# In[54]:

fp,tp,thr=roc_curve(test_label,fina_proba)#参数为测试集样本的参考标签，以及系统输出的概率
fp1,tp1,thr1=roc_curve(test_label,fina_sysout)
#print fp,"\n",tp,"\n",thr
print "auc_proba: ",auc(fp,tp)
print "auc_sysout_label: ",auc(fp1,tp1)


# In[56]:

help(pd.get_dummies)#categorical variable：分类变量；dummies variables:虚拟变量


# In[ ]:



