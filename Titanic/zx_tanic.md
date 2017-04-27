

```python
import numpy as np
import pandas as pd
```


```python
tanic=pd.read_csv("titanic_train.csv")
tanic.head()#默认显示前5行
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>
      <td>female</td>
      <td>35.0</td>
      <td>1</td>
      <td>0</td>
      <td>113803</td>
      <td>53.1000</td>
      <td>C123</td>
      <td>S</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0</td>
      <td>3</td>
      <td>Allen, Mr. William Henry</td>
      <td>male</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>373450</td>
      <td>8.0500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
  </tbody>
</table>
</div>




```python
"""
数据预处理：包括数据清洗，丢掉脏数据，填充缺失值，数值转换（映射）等。
"""
#第一步：检查各列特征下是否有缺失值
print tanic.describe()#按列进行统计，由age看到，714<891，数据缺失了，而其他各列的count值都是891，即没有缺失。因此要对数据进行预处理，缺失值填充-选择均值-mean填充
```

           PassengerId    Survived      Pclass         Age       SibSp  \
    count   891.000000  891.000000  891.000000  714.000000  891.000000   
    mean    446.000000    0.383838    2.308642   29.699118    0.523008   
    std     257.353842    0.486592    0.836071   14.526497    1.102743   
    min       1.000000    0.000000    1.000000    0.420000    0.000000   
    25%     223.500000    0.000000    2.000000         NaN    0.000000   
    50%     446.000000    0.000000    3.000000         NaN    0.000000   
    75%     668.500000    1.000000    3.000000         NaN    1.000000   
    max     891.000000    1.000000    3.000000   80.000000    8.000000   
    
                Parch        Fare  
    count  891.000000  891.000000  
    mean     0.381594   32.204208  
    std      0.806057   49.693429  
    min      0.000000    0.000000  
    25%      0.000000    7.910400  
    50%      0.000000   14.454200  
    75%      0.000000   31.000000  
    max      6.000000  512.329200  


    /home/zzpp220/anaconda2/lib/python2.7/site-packages/numpy/lib/function_base.py:3834: RuntimeWarning: Invalid value encountered in percentile
      RuntimeWarning)



```python
tanic["Age"]=tanic["Age"].fillna(int(tanic["Age"].mean()))#这里age是int类型，可以选用中位数median，也可以选平均数近似为29
##！注意，fillna 并不是原地修改，而是返回一个新的值，因此要将新的赋值给原来旧的
print tanic.describe() #只会显示该列的取值为数值型的统计数据，字符型等其他非数值性的则不会显示
#由describe可知各列无缺失值，都是891
```

           PassengerId    Survived      Pclass         Age       SibSp  \
    count   891.000000  891.000000  891.000000  891.000000  891.000000   
    mean    446.000000    0.383838    2.308642   29.560236    0.523008   
    std     257.353842    0.486592    0.836071   13.005010    1.102743   
    min       1.000000    0.000000    1.000000    0.420000    0.000000   
    25%     223.500000    0.000000    2.000000   22.000000    0.000000   
    50%     446.000000    0.000000    3.000000   29.000000    0.000000   
    75%     668.500000    1.000000    3.000000   35.000000    1.000000   
    max     891.000000    1.000000    3.000000   80.000000    8.000000   
    
                Parch        Fare  
    count  891.000000  891.000000  
    mean     0.381594   32.204208  
    std      0.806057   49.693429  
    min      0.000000    0.000000  
    25%      0.000000    7.910400  
    50%      0.000000   14.454200  
    75%      0.000000   31.000000  
    max      6.000000  512.329200  



```python
print int(tanic["Age"].mean()),tanic["Age"].median()
```

    29 29.0



```python
help(tanic["Age"].mean)
```

    Help on method mean in module pandas.core.generic:
    
    mean(self, axis=None, skipna=None, level=None, numeric_only=None, **kwargs) method of pandas.core.series.Series instance
        Return the mean of the values for the requested axis
        
        Parameters
        ----------
        axis : {index (0)}
        skipna : boolean, default True
            Exclude NA/null values. If an entire row/column is NA, the result
            will be NA
        level : int or level name, default None
            If the axis is a MultiIndex (hierarchical), count along a
            particular level, collapsing into a scalar
        numeric_only : boolean, default None
            Include only float, int, boolean data. If None, will attempt to use
            everything, then use only numeric data
        
        Returns
        -------
        mean : scalar or Series (if level specified)
    



```python
help(tanic["Age"].median)
```

    Help on method median in module pandas.core.generic:
    
    median(self, axis=None, skipna=None, level=None, numeric_only=None, **kwargs) method of pandas.core.series.Series instance
        Return the median of the values for the requested axis
        
        Parameters
        ----------
        axis : {index (0)}
        skipna : boolean, default True
            Exclude NA/null values. If an entire row/column is NA, the result
            will be NA
        level : int or level name, default None
            If the axis is a MultiIndex (hierarchical), count along a
            particular level, collapsing into a scalar
        numeric_only : boolean, default None
            Include only float, int, boolean data. If None, will attempt to use
            everything, then use only numeric data
        
        Returns
        -------
        median : scalar or Series (if level specified)
    



```python
"""
接下来要研究哪些特征影响该样本能否获救，这些特征的影响程度是怎样的，那个最大？
显然，这是一个分类问题，二分类。
第二步：将案例中的各特征的样本值转化为可以用计算机语言、模型处理的值的形式，例如将str类型转换为int型，即数值转换。
先扫描一遍那些特征的取值是非数值，特征取值一共哟哪几种，为这些取值分别做一个非数值性到数值型的映射。
"""
```




    '\n\xe6\x8e\xa5\xe4\xb8\x8b\xe6\x9d\xa5\xe8\xa6\x81\xe7\xa0\x94\xe7\xa9\xb6\xe5\x93\xaa\xe4\xba\x9b\xe7\x89\xb9\xe5\xbe\x81\xe5\xbd\xb1\xe5\x93\x8d\xe8\xaf\xa5\xe6\xa0\xb7\xe6\x9c\xac\xe8\x83\xbd\xe5\x90\xa6\xe8\x8e\xb7\xe6\x95\x91\xef\xbc\x8c\xe8\xbf\x99\xe4\xba\x9b\xe7\x89\xb9\xe5\xbe\x81\xe7\x9a\x84\xe5\xbd\xb1\xe5\x93\x8d\xe7\xa8\x8b\xe5\xba\xa6\xe6\x98\xaf\xe6\x80\x8e\xe6\xa0\xb7\xe7\x9a\x84\xef\xbc\x8c\xe9\x82\xa3\xe4\xb8\xaa\xe6\x9c\x80\xe5\xa4\xa7\xef\xbc\x9f\n\xe6\x98\xbe\xe7\x84\xb6\xef\xbc\x8c\xe8\xbf\x99\xe6\x98\xaf\xe4\xb8\x80\xe4\xb8\xaa\xe5\x88\x86\xe7\xb1\xbb\xe9\x97\xae\xe9\xa2\x98\xef\xbc\x8c\xe4\xba\x8c\xe5\x88\x86\xe7\xb1\xbb\xe3\x80\x82\n\xe7\xac\xac\xe4\xba\x8c\xe6\xad\xa5\xef\xbc\x9a\xe5\xb0\x86\xe6\xa1\x88\xe4\xbe\x8b\xe4\xb8\xad\xe7\x9a\x84\xe5\x90\x84\xe7\x89\xb9\xe5\xbe\x81\xe7\x9a\x84\xe6\xa0\xb7\xe6\x9c\xac\xe5\x80\xbc\xe8\xbd\xac\xe5\x8c\x96\xe4\xb8\xba\xe5\x8f\xaf\xe4\xbb\xa5\xe7\x94\xa8\xe8\xae\xa1\xe7\xae\x97\xe6\x9c\xba\xe8\xaf\xad\xe8\xa8\x80\xe3\x80\x81\xe6\xa8\xa1\xe5\x9e\x8b\xe5\xa4\x84\xe7\x90\x86\xe7\x9a\x84\xe5\x80\xbc\xe7\x9a\x84\xe5\xbd\xa2\xe5\xbc\x8f\xef\xbc\x8c\xe4\xbe\x8b\xe5\xa6\x82\xe5\xb0\x86str\xe7\xb1\xbb\xe5\x9e\x8b\xe8\xbd\xac\xe6\x8d\xa2\xe4\xb8\xbaint\xe5\x9e\x8b\xef\xbc\x8c\xe5\x8d\xb3\xe6\x95\xb0\xe5\x80\xbc\xe8\xbd\xac\xe6\x8d\xa2\xe3\x80\x82\n\xe5\x85\x88\xe6\x89\xab\xe6\x8f\x8f\xe4\xb8\x80\xe9\x81\x8d\xe9\x82\xa3\xe4\xba\x9b\xe7\x89\xb9\xe5\xbe\x81\xe7\x9a\x84\xe5\x8f\x96\xe5\x80\xbc\xe6\x98\xaf\xe9\x9d\x9e\xe6\x95\xb0\xe5\x80\xbc\xef\xbc\x8c\xe7\x89\xb9\xe5\xbe\x81\xe5\x8f\x96\xe5\x80\xbc\xe4\xb8\x80\xe5\x85\xb1\xe5\x93\x9f\xe5\x93\xaa\xe5\x87\xa0\xe7\xa7\x8d\xef\xbc\x8c\xe4\xb8\xba\xe8\xbf\x99\xe4\xba\x9b\xe5\x8f\x96\xe5\x80\xbc\xe5\x88\x86\xe5\x88\xab\xe5\x81\x9a\xe4\xb8\x80\xe4\xb8\xaa\xe9\x9d\x9e\xe6\x95\xb0\xe5\x80\xbc\xe6\x80\xa7\xe5\x88\xb0\xe6\x95\xb0\xe5\x80\xbc\xe5\x9e\x8b\xe7\x9a\x84\xe6\x98\xa0\xe5\xb0\x84\xe3\x80\x82\n'




```python
#首先看性别,取值只有两种，且为str类型
print tanic["Sex"].unique()
#性别各取值的人数分布。男的比女的多
tanic["Sex"].groupby(tanic["Sex"]).value_counts()
```

    ['male' 'female']





    Sex     Sex   
    female  female    314
    male    male      577
    Name: Sex, dtype: int64




```python
#数值转化 
help(tanic.loc)
```

    Help on _LocIndexer in module pandas.core.indexing object:
    
    class _LocIndexer(_LocationIndexer)
     |  Purely label-location based indexer for selection by label.
     |  
     |  ``.loc[]`` is primarily label based, but may also be used with a
     |  boolean array.
     |  
     |  Allowed inputs are:
     |  
     |  - A single label, e.g. ``5`` or ``'a'``, (note that ``5`` is
     |    interpreted as a *label* of the index, and **never** as an
     |    integer position along the index).
     |  - A list or array of labels, e.g. ``['a', 'b', 'c']``.
     |  - A slice object with labels, e.g. ``'a':'f'`` (note that contrary
     |    to usual python slices, **both** the start and the stop are included!).
     |  - A boolean array.
     |  - A ``callable`` function with one argument (the calling Series, DataFrame
     |    or Panel) and that returns valid output for indexing (one of the above)
     |  
     |  ``.loc`` will raise a ``KeyError`` when the items are not found.
     |  
     |  See more at :ref:`Selection by Label <indexing.label>`
     |  
     |  Method resolution order:
     |      _LocIndexer
     |      _LocationIndexer
     |      _NDFrameIndexer
     |      __builtin__.object
     |  
     |  Methods inherited from _LocationIndexer:
     |  
     |  __getitem__(self, key)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from _NDFrameIndexer:
     |  
     |  __call__(self, axis=None)
     |  
     |  __init__(self, obj, name)
     |  
     |  __iter__(self)
     |  
     |  __setitem__(self, key, value)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from _NDFrameIndexer:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from _NDFrameIndexer:
     |  
     |  axis = None
    



```python
#定位SEX属性的行，并且做数值映射 ，替换原来的值.loc[row_indexer,col_indexer] = value instead

tanic.loc[tanic["Sex"]=="male","Sex"]=0
tanic.loc[tanic["Sex"]=="female","Sex"]=1
tanic["Sex"].unique()
#看如下结果，修改完成
```




    array([0, 1], dtype=object)




```python
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
```




    array([0, 1, 2], dtype=object)




```python
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
```

    (891, 7)
    5


    /home/zzpp220/anaconda2/lib/python2.7/site-packages/sklearn/cross_validation.py:44: DeprecationWarning: This module was deprecated in version 0.18 in favor of the model_selection module into which all the refactored classes and functions are moved. Also note that the interface of the new CV iterators are different from that of this module. This module will be removed in 0.20.
      "This module will be removed in 0.20.", DeprecationWarning)



```python
help(tanic.iloc)#按照下标进行定位
```

    Help on _iLocIndexer in module pandas.core.indexing object:
    
    class _iLocIndexer(_LocationIndexer)
     |  Purely integer-location based indexing for selection by position.
     |  
     |  ``.iloc[]`` is primarily integer position based (from ``0`` to
     |  ``length-1`` of the axis), but may also be used with a boolean
     |  array.
     |  
     |  Allowed inputs are:
     |  
     |  - An integer, e.g. ``5``.
     |  - A list or array of integers, e.g. ``[4, 3, 0]``.
     |  - A slice object with ints, e.g. ``1:7``.
     |  - A boolean array.
     |  - A ``callable`` function with one argument (the calling Series, DataFrame
     |    or Panel) and that returns valid output for indexing (one of the above)
     |  
     |  ``.iloc`` will raise ``IndexError`` if a requested indexer is
     |  out-of-bounds, except *slice* indexers which allow out-of-bounds
     |  indexing (this conforms with python/numpy *slice* semantics).
     |  
     |  See more at :ref:`Selection by Position <indexing.integer>`
     |  
     |  Method resolution order:
     |      _iLocIndexer
     |      _LocationIndexer
     |      _NDFrameIndexer
     |      __builtin__.object
     |  
     |  Methods inherited from _LocationIndexer:
     |  
     |  __getitem__(self, key)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from _NDFrameIndexer:
     |  
     |  __call__(self, axis=None)
     |  
     |  __init__(self, obj, name)
     |  
     |  __iter__(self)
     |  
     |  __setitem__(self, key, value)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from _NDFrameIndexer:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from _NDFrameIndexer:
     |  
     |  axis = None
    



```python
print tanic[features]
```

         Pclass Sex   Age  SibSp  Parch      Fare Embarked
    0         3   0  22.0      1      0    7.2500        0
    1         1   1  38.0      1      0   71.2833        1
    2         3   1  26.0      0      0    7.9250        0
    3         1   1  35.0      1      0   53.1000        0
    4         3   0  35.0      0      0    8.0500        0
    5         3   0  29.0      0      0    8.4583        2
    6         1   0  54.0      0      0   51.8625        0
    7         3   0   2.0      3      1   21.0750        0
    8         3   1  27.0      0      2   11.1333        0
    9         2   1  14.0      1      0   30.0708        1
    10        3   1   4.0      1      1   16.7000        0
    11        1   1  58.0      0      0   26.5500        0
    12        3   0  20.0      0      0    8.0500        0
    13        3   0  39.0      1      5   31.2750        0
    14        3   1  14.0      0      0    7.8542        0
    15        2   1  55.0      0      0   16.0000        0
    16        3   0   2.0      4      1   29.1250        2
    17        2   0  29.0      0      0   13.0000        0
    18        3   1  31.0      1      0   18.0000        0
    19        3   1  29.0      0      0    7.2250        1
    20        2   0  35.0      0      0   26.0000        0
    21        2   0  34.0      0      0   13.0000        0
    22        3   1  15.0      0      0    8.0292        2
    23        1   0  28.0      0      0   35.5000        0
    24        3   1   8.0      3      1   21.0750        0
    25        3   1  38.0      1      5   31.3875        0
    26        3   0  29.0      0      0    7.2250        1
    27        1   0  19.0      3      2  263.0000        0
    28        3   1  29.0      0      0    7.8792        2
    29        3   0  29.0      0      0    7.8958        0
    ..      ...  ..   ...    ...    ...       ...      ...
    861       2   0  21.0      1      0   11.5000        0
    862       1   1  48.0      0      0   25.9292        0
    863       3   1  29.0      8      2   69.5500        0
    864       2   0  24.0      0      0   13.0000        0
    865       2   1  42.0      0      0   13.0000        0
    866       2   1  27.0      1      0   13.8583        1
    867       1   0  31.0      0      0   50.4958        0
    868       3   0  29.0      0      0    9.5000        0
    869       3   0   4.0      1      1   11.1333        0
    870       3   0  26.0      0      0    7.8958        0
    871       1   1  47.0      1      1   52.5542        0
    872       1   0  33.0      0      0    5.0000        0
    873       3   0  47.0      0      0    9.0000        0
    874       2   1  28.0      1      0   24.0000        1
    875       3   1  15.0      0      0    7.2250        1
    876       3   0  20.0      0      0    9.8458        0
    877       3   0  19.0      0      0    7.8958        0
    878       3   0  29.0      0      0    7.8958        0
    879       1   1  56.0      0      1   83.1583        1
    880       2   1  25.0      0      1   26.0000        0
    881       3   0  33.0      0      0    7.8958        0
    882       3   1  22.0      0      0   10.5167        0
    883       2   0  28.0      0      0   10.5000        0
    884       3   0  25.0      0      0    7.0500        0
    885       3   1  39.0      0      5   29.1250        2
    886       2   0  27.0      0      0   13.0000        0
    887       1   1  19.0      0      0   30.0000        0
    888       3   1  29.0      1      2   23.4500        0
    889       1   0  26.0      0      0   30.0000        1
    890       3   0  32.0      0      0    7.7500        2
    
    [891 rows x 7 columns]



```python
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
    
```


```python
print [i.shape for i in pred_score]#每一组都是平均178个样本的概率值
```

    [(179,), (178,), (178,), (178,), (178,)]



```python
import numpy as np

help(np.concatenate)
```

    Help on built-in function concatenate in module numpy.core.multiarray:
    
    concatenate(...)
        concatenate((a1, a2, ...), axis=0)
        
        Join a sequence of arrays along an existing axis.
        
        Parameters
        ----------
        a1, a2, ... : sequence of array_like
            The arrays must have the same shape, except in the dimension
            corresponding to `axis` (the first, by default).
        axis : int, optional
            The axis along which the arrays will be joined.  Default is 0.
        
        Returns
        -------
        res : ndarray
            The concatenated array.
        
        See Also
        --------
        ma.concatenate : Concatenate function that preserves input masks.
        array_split : Split an array into multiple sub-arrays of equal or
                      near-equal size.
        split : Split array into a list of multiple sub-arrays of equal size.
        hsplit : Split array into multiple sub-arrays horizontally (column wise)
        vsplit : Split array into multiple sub-arrays vertically (row wise)
        dsplit : Split array into multiple sub-arrays along the 3rd axis (depth).
        stack : Stack a sequence of arrays along a new axis.
        hstack : Stack arrays in sequence horizontally (column wise)
        vstack : Stack arrays in sequence vertically (row wise)
        dstack : Stack arrays in sequence depth wise (along third dimension)
        
        Notes
        -----
        When one or more of the arrays to be concatenated is a MaskedArray,
        this function will return a MaskedArray object instead of an ndarray,
        but the input masks are *not* preserved. In cases where a MaskedArray
        is expected as input, use the ma.concatenate function from the masked
        array module instead.
        
        Examples
        --------
        >>> a = np.array([[1, 2], [3, 4]])
        >>> b = np.array([[5, 6]])
        >>> np.concatenate((a, b), axis=0)
        array([[1, 2],
               [3, 4],
               [5, 6]])
        >>> np.concatenate((a, b.T), axis=1)
        array([[1, 2, 5],
               [3, 4, 6]])
        
        This function will not preserve masking of MaskedArray inputs.
        
        >>> a = np.ma.arange(3)
        >>> a[1] = np.ma.masked
        >>> b = np.arange(2, 5)
        >>> a
        masked_array(data = [0 -- 2],
                     mask = [False  True False],
               fill_value = 999999)
        >>> b
        array([2, 3, 4])
        >>> np.concatenate([a, b])
        masked_array(data = [0 1 2 2 3 4],
                     mask = False,
               fill_value = 999999)
        >>> np.ma.concatenate([a, b])
        masked_array(data = [0 -- 2 2 3 4],
                     mask = [False  True False False False False],
               fill_value = 999999)
    



```python
pred_score=np.concatenate(pred_score,axis=0)

pred_score
```




    array([  1.02592107e-01,   9.44255295e-01,   5.91815855e-01,
             9.15870978e-01,   5.52881039e-02,   1.69428484e-01,
             3.49092646e-01,   1.41787102e-01,   5.35692777e-01,
             8.76262616e-01,   6.70944170e-01,   7.98001884e-01,
             1.44847994e-01,  -1.17936142e-01,   6.63435658e-01,
             6.16798986e-01,   1.93140481e-01,   2.88003623e-01,
             5.35965583e-01,   6.12703123e-01,   2.57340928e-01,
             2.58150327e-01,   7.35688798e-01,   4.97833548e-01,
             5.88804591e-01,   3.70920627e-01,   1.29861679e-01,
             5.00474505e-01,   6.52040014e-01,   9.10508394e-02,
             4.62174298e-01,   1.02786202e+00,   6.51988719e-01,
             6.60966784e-02,   5.25442999e-01,   3.90798196e-01,
             1.29863346e-01,   1.38877334e-01,   5.83587202e-01,
             6.73860772e-01,   4.78845054e-01,   7.55965595e-01,
             1.30128000e-01,   8.95082755e-01,   7.11746607e-01,
             9.11120598e-02,   1.42227227e-01,   6.51988719e-01,
             7.56063813e-02,   6.13504751e-01,   8.93263885e-02,
             1.38778079e-01,   8.80740174e-01,   7.46009377e-01,
             3.00795997e-01,   4.91862889e-01,   8.17617793e-01,
             1.32848676e-01,   8.38573807e-01,   1.25972167e-02,
             1.71657961e-01,   9.38635791e-01,   3.85382424e-01,
             1.06842355e-01,   5.27851551e-01,   7.73360553e-02,
             7.69852518e-01,   1.50861650e-01,   4.74137802e-01,
             4.92733083e-02,   2.69099095e-01,   4.65585365e-01,
             3.59788610e-01,   1.20646842e-01,   9.24340352e-02,
             1.14835889e-01,   9.10508394e-02,   9.11120598e-02,
             4.11123238e-01,   5.69739659e-01,   1.33283844e-01,
             9.16877389e-02,   6.52003607e-01,   5.02438980e-01,
             8.41500430e-01,   4.63176767e-01,   7.20459632e-02,
             9.11120598e-02,   9.59433313e-01,   1.20965356e-01,
             9.11120598e-02,   1.44770257e-01,   3.70558218e-01,
             3.25735829e-02,  -8.83253359e-02,   9.11120598e-02,
             2.79836558e-01,   5.52111219e-01,   7.19248883e-01,
             2.33314635e-01,   5.79862944e-01,   9.10508394e-02,
             5.30505549e-01,   6.74693021e-02,  -1.66967465e-02,
             9.70214987e-02,   6.21559971e-01,   9.10028793e-02,
             3.73149055e-02,   6.28502896e-01,   3.90941852e-01,
             6.72150869e-01,   1.32906675e-01,   5.98397197e-01,
             6.87222800e-01,   1.38827707e-01,  -7.86350876e-02,
             2.61182832e-01,   6.19256762e-01,   5.72968110e-01,
             2.99794706e-01,   9.11120598e-02,   2.82963974e-01,
             7.49947761e-01,   3.33473791e-01,   2.02960645e-01,
             1.69147274e-01,   1.20604743e-01,   5.63001305e-01,
            -4.84528585e-03,   1.06245362e-01,   1.44450974e-01,
             4.39045464e-01,   7.46009377e-01,   3.11886261e-01,
             3.63716963e-01,   9.79325534e-01,   4.21088215e-01,
             1.69193834e-01,   5.78143121e-01,   5.64461363e-01,
             6.15629014e-01,   5.76906606e-01,   2.28456847e-01,
             3.53085346e-01,   3.01429401e-01,   1.02952456e-01,
             5.92398161e-01,   1.96958760e-01,   2.10385052e-01,
             1.56460534e-01,   9.98849320e-01,  -6.71104122e-02,
            -2.64159219e-02,   9.08192576e-02,   3.84147015e-01,
             7.29600660e-01,   8.51414005e-02,   9.13552346e-02,
            -1.75873004e-01,  -2.09649081e-02,   7.06259621e-01,
             1.08914857e-01,   1.63003146e-01,   1.25150344e-01,
             1.64051892e-01,   9.56733135e-01,   3.53454494e-01,
             4.88061422e-01,   1.16316673e-01,   3.00007750e-01,
             1.81199163e-01,   6.86646056e-01,   1.38827707e-01,
             3.67824884e-01,   1.01001534e-01,  -1.76771070e-02,
             8.85702875e-01,   2.82032964e-01,   4.48313063e-02,
             1.44419756e-01,   3.14129689e-01,  -3.59057354e-02,
             3.28010323e-01,   7.13002619e-01,   4.80987622e-01,
             6.07805185e-01,   3.79881886e-01,   2.29026880e-02,
             4.71584434e-02,   7.66842635e-01,   3.38849127e-01,
             5.97327570e-01,   3.66830955e-01,   9.24188270e-01,
             8.76782306e-01,   1.55421069e-01,  -3.63212383e-03,
             6.59947441e-01,   8.13939782e-01,   9.47283977e-02,
            -3.60106615e-01,   5.85201067e-02,   2.45806730e-02,
             1.53172471e-01,   7.36986627e-01,   1.86249449e-02,
             1.42787796e-01,   7.36480304e-01,   4.44176953e-01,
             1.17554880e-01,   7.51539053e-01,   1.29388113e-01,
             2.74090551e-01,   1.00994648e-01,   9.71510187e-01,
             6.04677711e-01,   1.53144643e-01,   1.00914934e+00,
             2.73353723e-01,   1.64946758e-01,   2.91751981e-01,
            -4.11032594e-02,   8.83684468e-02,   3.85366151e-01,
             1.30007048e-01,   3.38112300e-01,   1.38218828e-01,
             3.44736271e-01,   4.19176695e-01,   9.05630833e-01,
             8.83328433e-02,   1.03510759e-01,   4.92169210e-01,
             3.08676583e-01,   5.92792900e-01,   1.41075625e-01,
             8.80804165e-01,   3.38112300e-01,   2.56215441e-01,
             5.73949158e-01,   6.07805185e-01,   2.79240866e-01,
             1.29351272e-01,   1.15831395e-01,   3.62712464e-01,
             6.16407788e-01,   7.83146782e-01,   3.64599308e-01,
             8.22041919e-02,   8.81781096e-02,   5.23607335e-01,
             2.79800449e-01,   3.04729144e-02,   4.94644115e-01,
             5.97373792e-01,   1.02766794e+00,   9.90384532e-01,
             1.12000168e+00,   6.49088010e-01,   1.55421069e-01,
            -5.82875297e-04,   2.84278130e-01,   4.01492495e-01,
             6.59947441e-01,   2.38030863e-01,  -5.90519232e-02,
             5.74549955e-02,   8.29662895e-01,   9.75429922e-01,
             4.75387733e-01,   1.09589883e-01,   7.00156548e-01,
             4.45837685e-01,   6.59947441e-01,   7.39164876e-01,
             4.98657553e-01,   2.76146191e-01,   5.79148648e-02,
             4.91169155e-01,  -5.65160915e-02,   9.42433294e-02,
             1.65374118e-01,   1.47285328e-01,   4.73914078e-01,
             9.85936407e-02,   8.29541110e-02,   1.29578450e-01,
             2.03444830e-01,   7.01157444e-01,   1.01167841e+00,
             1.03561412e+00,   2.72278646e-01,   6.22611768e-01,
             1.17804164e-01,   5.07969048e-01,   1.54099065e-01,
             1.08873528e+00,   4.75240368e-01,   9.38029736e-01,
             6.59947441e-01,   5.11365573e-02,   1.44912743e-01,
             8.51408084e-01,   8.84138944e-02,   5.90567023e-01,
             1.03700599e+00,   1.05264075e+00,   2.56453967e-01,
             1.01521690e+00,   1.05827029e+00,   1.00632593e+00,
             7.35953029e-01,   9.42555902e-02,   1.31418903e-01,
             6.10543988e-01,   7.63344864e-01,   1.33093841e-01,
             9.76359388e-01,   9.09164014e-01,   1.29388113e-01,
             1.00142734e-01,   8.45520941e-01,   7.60385795e-01,
            -3.60106615e-01,   1.00309058e+00,  -1.00508893e-01,
             7.43294062e-01,   5.14798779e-01,   1.08232882e+00,
             5.55662929e-01,   3.77513040e-01,   4.42879390e-01,
             5.90264890e-02,   9.55741821e-01,   8.83684468e-02,
             4.31453736e-01,   9.73320841e-01,  -5.78039925e-03,
             3.82519729e-01,   3.72718098e-01,   8.83213054e-01,
             2.85864837e-01,   3.03526267e-01,   2.38767690e-01,
             8.13939782e-01,   7.19745489e-01,   5.40886429e-01,
             1.73749290e-01,   1.20615535e-02,   1.24083063e-01,
             4.76566657e-01,   1.34095814e-01,   6.04096738e-02,
             1.21718538e-01,   9.47283977e-02,   1.01258010e+00,
             7.13838337e-01,   6.90298332e-01,   6.90298332e-01,
            -8.65031059e-02,   2.72590314e-01,   5.31519673e-01,
             6.29917880e-02,   1.47210886e-01,   9.37956324e-02,
             7.76851745e-01,   6.47602172e-01,   6.90219914e-01,
             1.03648592e+00,   4.74225179e-01,   1.24643877e-01,
             1.61782593e-01,   5.83639069e-01,   6.23973519e-01,
             9.71283559e-01,   6.48268592e-01,   5.54436375e-01,
             1.95497170e-01,   1.61615681e-01,   1.02206424e+00,
             7.80022836e-01,   8.19323442e-02,   8.73850715e-01,
             1.00324093e-01,   3.67907778e-01,   3.95923865e-02,
             7.26111318e-01,   1.84826255e-01,   8.84399330e-01,
             3.59038233e-01,   1.49355324e-01,   2.18145467e-02,
             1.02698129e+00,   5.97163552e-01,   1.43218833e-01,
             5.93406896e-01,   1.67255767e-01,   2.98987282e-01,
             7.74990811e-01,   3.89769089e-02,   1.18827158e-01,
             6.13636107e-01,   6.89565300e-02,   6.61398895e-01,
             1.95527010e-01,  -3.47671970e-02,   3.62108697e-01,
             1.49342700e-01,   4.67090315e-01,   1.00324093e-01,
             1.84297660e-01,   9.93791193e-01,   2.55795330e-01,
             8.29445507e-03,   6.05798719e-01,   6.85604121e-01,
             7.92000386e-01,   2.57549229e-01,   6.87596222e-01,
             1.42625733e-01,   2.33920670e-01,   1.00311469e-01,
             5.51173599e-01,   1.10685388e-01,   9.99321231e-02,
             7.40761754e-01,   8.38322051e-01,   1.84838880e-01,
             8.20082133e-02,   4.38310041e-01,   5.68352811e-01,
             6.54850883e-01,   1.73494143e-01,   2.78789437e-01,
             9.99422063e-01,   5.41637159e-01,   6.51723779e-01,
             2.29443014e-01,   2.49895356e-01,   6.14309267e-01,
             1.56526184e-01,   8.24648563e-02,   7.75203244e-01,
             1.00455620e-01,   5.74587596e-01,   8.48911918e-01,
             4.01491097e-01,   6.95231406e-01,   2.93431728e-01,
             1.42783196e-01,   6.53186829e-02,   4.69067044e-01,
             3.47380958e-01,   1.00417686e-01,   1.42625733e-01,
             2.11259883e-01,   9.10586203e-01,   6.38683065e-01,
             1.84838880e-01,   3.15580226e-01,   6.97352318e-02,
             3.28969806e-01,   1.47092395e-01,   1.00417686e-01,
             4.45823157e-02,   2.55795330e-01,   2.66488300e-01,
             1.84823706e-01,   7.21311492e-01,   9.99321231e-02,
             4.55610275e-02,   6.66573702e-01,   8.48667863e-01,
             6.49839083e-01,   4.47620506e-01,   1.95527010e-01,
             5.74763031e-02,   1.43051921e-01,   7.51772051e-01,
            -9.49953962e-03,   2.55795330e-01,  -2.84486204e-02,
             3.98091224e-01,   4.95855469e-01,   4.67090315e-01,
             8.96914931e-01,   2.98428861e-01,   9.42811948e-02,
             1.63296319e-01,   6.53186829e-02,   1.49024049e-01,
             2.75022255e-01,   2.30674701e-01,   1.49509612e-01,
             1.46608863e-01,   8.15501684e-01,   1.04696705e-01,
             9.51070034e-01,   1.30945852e-01,   1.74427333e-01,
             7.39311840e-01,   6.90146594e-01,   5.57639984e-01,
             1.05371580e+00,   5.49627293e-01,   7.07843415e-01,
             4.32173551e-01,   1.15339822e-01,   1.48231484e-01,
             1.84838880e-01,   1.00417686e-01,   3.89058790e-01,
             8.04050483e-01,   1.30763766e-01,   3.26251142e-01,
             7.36866917e-01,   1.94792910e-01,   6.91669828e-01,
             8.19146212e-02,   9.72053601e-01,   1.43279529e-01,
             1.42218589e-01,   8.84601029e-01,   1.42221139e-01,
             1.14269236e-01,   6.38683065e-01,   5.50668511e-01,
             3.89769089e-02,   1.92646592e-01,   8.78026631e-01,
             1.42221139e-01,   1.51243265e-01,   6.12217060e-01,
             6.00033987e-01,   9.47176968e-01,   2.94461486e-01,
             9.83004018e-01,   8.68403310e-02,   1.05679855e+00,
             9.23971544e-01,   5.69657781e-01,   5.56715548e-01,
             1.71378948e-01,   2.74694147e-01,   1.71384198e-01,
             7.81508360e-01,   2.88052606e-01,   2.69920391e-02,
             3.46687725e-01,   5.77220915e-01,   2.56617174e-01,
             1.79631299e-01,   1.77630501e-01,   6.56601387e-01,
             1.84452513e-01,   7.98322118e-01,   4.91231560e-01,
             8.36120873e-01,   5.15329581e-01,   1.79613143e-01,
             1.41440878e-02,   2.47280521e-01,   8.53617135e-02,
             6.11366617e-01,   1.56428140e-02,   1.50037525e-01,
             6.84503024e-01,   1.32333652e-01,   6.59034796e-02,
             2.65748463e-02,   6.68647014e-01,   3.52664278e-01,
             7.05618047e-01,   1.69486222e-01,   1.51551491e-01,
             7.34344106e-01,   8.13138722e-01,   6.07113130e-01,
             6.59197100e-02,   7.61136265e-01,   8.90440990e-01,
             8.18970414e-02,   4.02973606e-01,   1.32673688e-01,
             1.04243459e+00,   1.24673180e-01,   2.21279475e-01,
             1.30659526e-01,   8.53617135e-02,   4.63229675e-02,
             7.81301725e-01,  -3.13017696e-02,   7.40693305e-01,
             1.39023368e-01,   8.40969695e-03,   7.71284547e-01,
            -4.59060135e-02,   1.32332689e-01,   2.69818697e-01,
             7.14037006e-01,   8.53263642e-02,   4.01632844e-01,
            -1.17050270e-02,   4.06332748e-01,  -1.10994223e-02,
             7.88552482e-02,   4.11847084e-01,   8.47901794e-01,
             8.81915775e-01,   5.86785126e-01,   8.51324704e-02,
             6.54512034e-01,   1.79613143e-01,   4.65350173e-02,
             7.93168516e-01,   1.91168095e-02,   5.79742725e-01,
             8.46210243e-01,   2.59535024e-01,   9.40495188e-02,
             2.66953469e-01,   1.57180111e-01,   1.37085756e-01,
             1.38976048e-01,   1.92246545e-01,   1.53674729e-01,
             9.87558168e-01,   1.04739712e-01,   1.79609315e-01,
             6.87633132e-02,  -5.72311195e-02,   4.26651606e-01,
             3.91912940e-01,   6.21766731e-01,   7.73170802e-01,
             6.59197100e-02,   1.95445004e-01,   6.28654047e-01,
             3.43244736e-02,   1.43556872e-01,   1.01332007e+00,
             6.67064544e-01,   9.64675751e-02,   7.55677508e-01,
             2.80828824e-01,   1.50037525e-01,   2.72491036e-01,
             8.52470919e-02,   6.50078692e-01,   8.53263642e-02,
             8.57712022e-01,   1.37218511e-01,   7.05636203e-01,
             7.76571080e-01,   1.81154274e-01,   8.53263642e-02,
             6.52636315e-01,   2.79521479e-01,   3.12453438e-01,
             1.80892541e-01,   6.11504129e-02,   2.81298607e-01,
             3.99368547e-02,   9.06904562e-02,   1.29385345e-01,
             2.66579247e-01,   8.52986716e-02,  -5.23391101e-03,
             8.76955835e-01,   6.66132712e-01,   3.38008699e-01,
            -2.51940819e-02,   2.27752551e-01,   2.37714624e-01,
             1.56480948e-01,   1.14481736e-01,   6.82959628e-01,
             5.82020213e-01,   5.28760753e-01,   7.05706878e-01,
             4.69604907e-01,   1.43871118e-01,  -3.80034270e-02,
             1.07054876e-02,   3.02483543e-01,  -4.31182533e-03,
             1.50559052e-01,   1.56485716e-01,   1.07449874e+00,
             3.39154914e-01,   8.39072527e-01,   9.64675751e-02,
             1.58217153e-01,   1.97394745e-01,   9.19737357e-02,
            -1.17050270e-02,   7.05614218e-01,   2.99724927e-01,
             1.14550782e-03,   1.03553609e+00,   3.59112470e-01,
             7.48714742e-01,   2.05495705e-01,   5.18475296e-02,
             1.78963782e-01,   6.63276451e-01,   3.13814658e-01,
             9.97957436e-01,   9.88263847e-02,   1.00878202e+00,
             3.97999342e-01,   2.27999727e-01,   9.98546543e-02,
             1.59432735e-01,   1.51487612e-01,   9.67647877e-01,
             7.94440674e-01,   1.82354398e-01,   7.90818617e-02,
             8.78743984e-01,   1.28889968e-01,   2.52533715e-01,
             1.69777288e-01,   4.36159222e-01,   1.46364935e-01,
             6.80699186e-01,   6.87797621e-01,   2.66808037e-01,
             5.93377905e-01,   9.72302878e-01,   2.34513926e-01,
             2.77758257e-01,   3.09428759e-01,   3.09428759e-01,
             1.02764930e-01,   3.99461089e-01,   4.91293149e-01,
             9.97768862e-02,   9.97768862e-02,   4.57596060e-01,
             3.90870168e-01,   9.40624333e-01,   9.31271655e-02,
             8.94337632e-02,   1.89211480e-01,   1.09291952e-01,
             7.79046313e-01,   4.77537436e-01,   1.71630189e-01,
             8.55685649e-01,   1.93546849e-01,   7.91663657e-02,
             1.30810546e-01,   6.04746236e-01,   3.66669443e-01,
             1.04944264e-01,   3.35216661e-01,   7.39230566e-02,
             9.45498256e-01,   1.00100411e-01,   3.76718061e-02,
             1.87397220e-01,   8.47876055e-01,   1.67010565e-01,
             8.19065826e-01,   4.99168842e-01,   6.80039818e-01,
             1.49865132e-01,   8.42829187e-02,   1.25716856e-01,
             1.50159113e-03,   6.39272373e-01,   1.40846524e-01,
             5.46238362e-01,   1.56664787e-01,   1.81974742e-01,
             7.29959343e-01,   1.81974130e-01,   8.74474278e-01,
             7.29426648e-01,   9.93896533e-01,   4.57596060e-01,
             1.67923897e-02,   1.20424559e-01,   1.20434357e-01,
             6.62475826e-01,   1.34570901e-01,   1.61475297e-01,
             4.13180056e-01,   1.81974742e-01,   3.46271537e-01,
             2.94483149e-01,   4.98732645e-01,   1.20465993e-01,
             2.26672332e-01,   8.59774598e-01,   5.95294402e-01,
             1.35674453e-01,   5.42894622e-01,   2.52533715e-01,
             7.16193389e-01,   4.71359481e-01,   2.63316743e-01,
             1.10076332e-01,   8.94264151e-02,   4.04403659e-01,
             6.62489503e-01,   2.26672332e-01,   9.10949053e-01,
             1.15293310e-01,   4.88503769e-02,   2.47238969e-01,
             5.43222545e-01,   9.20260251e-02,   4.56126426e-01,
             6.36635468e-01,   2.51999221e-01,   2.72941859e-02,
             4.94576227e-02,   7.89238177e-01,   1.10158999e-01,
             4.09575936e-01,   5.90752529e-01,   8.39169965e-02,
             1.81935552e-01,   1.02157694e-01,   4.14663806e-01,
             1.81974742e-01,   7.95183811e-01,   6.86523022e-01,
             3.66050077e-01,   1.40846730e-01,   1.30808508e-01,
             1.56691731e-01,   8.97073656e-01,   1.41192659e-01,
             9.97844401e-02,   8.66408635e-02,   4.98683863e-01,
             1.46328807e-01,   3.45512226e-01,   9.99398762e-01,
             1.12360425e-01,   1.61881765e-01,   3.25203492e-02,
            -2.11340342e-01,   1.09845725e-01,   2.59130405e-01,
             9.74504426e-01,   4.77436068e-02,  -1.32981483e-01,
             6.92178735e-01,   1.00570291e+00,   6.74358271e-01,
             6.37149933e-01,   8.28940212e-01,   3.43636965e-01,
             5.96870705e-01,   1.40846730e-01,  -2.78121172e-02,
             2.86786821e-01,   8.64946875e-01,   2.94483149e-01,
             3.04256482e-01,   7.16978993e-01,   8.02794679e-01,
             4.48255551e-01,   9.98554724e-02,   1.70912665e-01,
             1.15293716e-01,   8.13093716e-01,   4.35682258e-01,
             6.72999806e-03,   7.98119222e-01,   7.19081889e-01,
             1.46422903e-01,   1.51499653e-01,   9.97768862e-02,
             8.42057962e-01,   7.80127812e-01,   7.90877794e-02,
             6.41934706e-01,   2.83444906e-01,   1.20424559e-01,
             5.10038949e-01,   2.88739652e-01,   1.01514232e+00,
             5.22615881e-01,   5.14215390e-01,   1.66457912e-01])




```python
#将结果数组中的概率值映射为输出。0,1.在设置阈值为0.5
threshold=0.5
pred_score[pred_score>threshold]=1
pred_score[pred_score<=threshold]=0
print pred_score.shape
print pred_score[pred_score==tanic["Survived"]].shape

accuracy=sum(pred_score[pred_score==tanic["Survived"]])/len(pred_score)#最后的结果为均值
print "accuracy_linear_regression is :",accuracy
```

    (891,)
    (891,)
    accuracy_linear_regression is : 0.787878787879


    /home/zzpp220/anaconda2/lib/python2.7/site-packages/ipykernel/__main__.py:6: FutureWarning: in the future, boolean array-likes will be handled as a boolean array index
    /home/zzpp220/anaconda2/lib/python2.7/site-packages/ipykernel/__main__.py:8: FutureWarning: in the future, boolean array-likes will be handled as a boolean array index



```python
"""用逻辑回归，同时交叉验证用更方便的表示"""
from sklearn.cross_validation import cross_val_score
#cross_val_score(estimator, X, y=None, scoring=None, cv=None, n_jobs=1, verbose=0, fit_params=None, pre_dispatch='2*n_jobs')
from sklearn.linear_model import LogisticRegression

log_model=LogisticRegression()
# Compute the accuracy score for all the cross validation folds.  (much simpler than what we did before!)
log_sysout=cross_val_score(log_model,tanic[features],tanic["Survived"],cv=5)#同样有5个元素
print "accuracy_logistic_regression is :{0:.3f}%".format(log_sysout.mean())
```

    accuracy_logistic_regression is :0.789%



```python
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
```

    accuracy_random_forest is :81.157% 



```python
"""
在上述随机森林的分类器中调节参数,加大加深随机森林，结点分裂的终止条件宽松一点
"""
ranforest2_model=RandomForestClassifier(n_estimators=100,min_samples_split=5,min_samples_leaf=2)
ranforest2_sysout=cross_val_score(ranforest2_model,tanic[features],tanic["Survived"],cv=5,scoring="accuracy")
print "accuracy_random_forest--paramenter-modified is :{0:.3f}%".format(ranforest2_sysout.mean()*100)
```

    accuracy_random_forest--paramenter-modified is :82.163%



```python
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
```

    /home/zzpp220/anaconda2/lib/python2.7/site-packages/ipykernel/__main__.py:29: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy


    1     517
    2     183
    3     125
    4      40
    5       7
    6       6
    7       5
    10      3
    8       3
    9       2
    Name: Title, dtype: int64



```python
features.extend(["FamilySize","NameLength","Title"])
"""#现在有的所有的特征如下:features 
features=['Pclass','Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked', 'FamilySize', 'NameLength', 'Title']

接下来要对特征进行衡量，那些特征有用，有用的程度是多少，那些没用？对特征进行选择，选出影响最大的几个特征，都用feature_importance量化查看
"""
```




    "#\xe7\x8e\xb0\xe5\x9c\xa8\xe6\x9c\x89\xe7\x9a\x84\xe6\x89\x80\xe6\x9c\x89\xe7\x9a\x84\xe7\x89\xb9\xe5\xbe\x81\xe5\xa6\x82\xe4\xb8\x8b:features \nfeatures=['Pclass','Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked', 'FamilySize', 'NameLength', 'Title']\n\n\xe6\x8e\xa5\xe4\xb8\x8b\xe6\x9d\xa5\xe8\xa6\x81\xe5\xaf\xb9\xe7\x89\xb9\xe5\xbe\x81\xe8\xbf\x9b\xe8\xa1\x8c\xe8\xa1\xa1\xe9\x87\x8f\xef\xbc\x8c\xe9\x82\xa3\xe4\xba\x9b\xe7\x89\xb9\xe5\xbe\x81\xe6\x9c\x89\xe7\x94\xa8\xef\xbc\x8c\xe6\x9c\x89\xe7\x94\xa8\xe7\x9a\x84\xe7\xa8\x8b\xe5\xba\xa6\xe6\x98\xaf\xe5\xa4\x9a\xe5\xb0\x91\xef\xbc\x8c\xe9\x82\xa3\xe4\xba\x9b\xe6\xb2\xa1\xe7\x94\xa8\xef\xbc\x9f\xe5\xaf\xb9\xe7\x89\xb9\xe5\xbe\x81\xe8\xbf\x9b\xe8\xa1\x8c\xe9\x80\x89\xe6\x8b\xa9\xef\xbc\x8c\xe9\x80\x89\xe5\x87\xba\xe5\xbd\xb1\xe5\x93\x8d\xe6\x9c\x80\xe5\xa4\xa7\xe7\x9a\x84\xe5\x87\xa0\xe4\xb8\xaa\xe7\x89\xb9\xe5\xbe\x81\xef\xbc\x8c\xe9\x83\xbd\xe7\x94\xa8feature_importance\xe9\x87\x8f\xe5\x8c\x96\xe6\x9f\xa5\xe7\x9c\x8b\n"




```python
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
```

    [  2.53704739e-25   1.40606613e-69   4.30004011e-02   2.92243929e-01
       1.47992454e-02   6.12018934e-15   1.40831242e-03   6.19891122e-01
       2.02679507e-24   1.03899613e-27] [  1.15031272e+02   3.72405724e+02   4.10714781e+00   1.11057220e+00
       5.96346384e+00   6.30307642e+01   1.02593551e+01   2.46193112e-01
       1.10388690e+02   1.27425897e+02]
    [ 24.59567142  68.85199425   1.36652749   0.5342545    1.82976043
      14.21323514   2.85130099   0.20768458  23.69319016  26.98338607]



```python
#scores反映了每个特征在该分类问题的中的影响程度，用画图的方式开看更直观些
# Plot the scores.
plt.bar(range(len(features)),scores)#选择条形图。横坐标定为1-10，纵坐标对应为特征取值
plt.xticks(range(len(features)), features, rotation='vertical')#更改横坐标各个点代表的标签值
plt.show()
```


```python
# from the chart,Pick only the top5 features.
top5_fea = [ "Sex","Pclass", "Title","NameLength","Fare"]
#重新用该特征组合 运用随机森林
top_ranforest_model=RandomForestClassifier(n_estimators=100,min_samples_split=4,min_samples_leaf=2,random_state=1)
top_ranforest_sysout=cross_val_score(top_ranforest_model,tanic[top5_fea],tanic["Survived"],cv=5,scoring="accuracy")
print "accuracy_top_random_forest--paramenter-modified is :{0:.3f}%".format(top_ranforest_sysout.mean()*100)
#由结果可知，和之前的随机森林结果82.724相比，虽然差一点但很微小，但是特征的维度减低了一半啊，计算复杂度降低了，很实用的一个功能！！
```

    accuracy_top_random_forest--paramenter-modified is :81.710%



```python
"""
使用集成学习的迭代决策树
特征不仅可以组合，也可以考虑将分类算法进行集成，综合多个分类器的优缺点

"""

from sklearn.ensemble import GradientBoostingClassifier
```


```python
help(GradientBoostingClassifier)
ensemble_fea=["Pclass","Sex","Age","Fare","Title","NameLength","Embarked"]
#选定特征都要永在两种算法。
gbrt_model=GradientBoostingClassifier(random_state=1,n_estimators=25,max_depth=3)
lg_model=LogisticRegression(random_state=1)
algorithm=[[gbrt_model,ensemble_fea],[lg_model,ensemble_fea]]#一行写不下分两行
```

    Help on class GradientBoostingClassifier in module sklearn.ensemble.gradient_boosting:
    
    class GradientBoostingClassifier(BaseGradientBoosting, sklearn.base.ClassifierMixin)
     |  Gradient Boosting for classification.
     |  
     |  GB builds an additive model in a
     |  forward stage-wise fashion; it allows for the optimization of
     |  arbitrary differentiable loss functions. In each stage ``n_classes_``
     |  regression trees are fit on the negative gradient of the
     |  binomial or multinomial deviance loss function. Binary classification
     |  is a special case where only a single regression tree is induced.
     |  
     |  Read more in the :ref:`User Guide <gradient_boosting>`.
     |  
     |  Parameters
     |  ----------
     |  loss : {'deviance', 'exponential'}, optional (default='deviance')
     |      loss function to be optimized. 'deviance' refers to
     |      deviance (= logistic regression) for classification
     |      with probabilistic outputs. For loss 'exponential' gradient
     |      boosting recovers the AdaBoost algorithm.
     |  
     |  learning_rate : float, optional (default=0.1)
     |      learning rate shrinks the contribution of each tree by `learning_rate`.
     |      There is a trade-off between learning_rate and n_estimators.
     |  
     |  n_estimators : int (default=100)
     |      The number of boosting stages to perform. Gradient boosting
     |      is fairly robust to over-fitting so a large number usually
     |      results in better performance.
     |  
     |  max_depth : integer, optional (default=3)
     |      maximum depth of the individual regression estimators. The maximum
     |      depth limits the number of nodes in the tree. Tune this parameter
     |      for best performance; the best value depends on the interaction
     |      of the input variables.
     |  
     |  criterion : string, optional (default="friedman_mse")
     |      The function to measure the quality of a split. Supported criteria
     |      are "friedman_mse" for the mean squared error with improvement
     |      score by Friedman, "mse" for mean squared error, and "mae" for
     |      the mean absolute error. The default value of "friedman_mse" is
     |      generally the best as it can provide a better approximation in
     |      some cases.
     |  
     |      .. versionadded:: 0.18
     |  
     |  min_samples_split : int, float, optional (default=2)
     |      The minimum number of samples required to split an internal node:
     |  
     |      - If int, then consider `min_samples_split` as the minimum number.
     |      - If float, then `min_samples_split` is a percentage and
     |        `ceil(min_samples_split * n_samples)` are the minimum
     |        number of samples for each split.
     |  
     |      .. versionchanged:: 0.18
     |         Added float values for percentages.
     |  
     |  min_samples_leaf : int, float, optional (default=1)
     |      The minimum number of samples required to be at a leaf node:
     |  
     |      - If int, then consider `min_samples_leaf` as the minimum number.
     |      - If float, then `min_samples_leaf` is a percentage and
     |        `ceil(min_samples_leaf * n_samples)` are the minimum
     |        number of samples for each node.
     |  
     |      .. versionchanged:: 0.18
     |         Added float values for percentages.
     |  
     |  min_weight_fraction_leaf : float, optional (default=0.)
     |      The minimum weighted fraction of the sum total of weights (of all
     |      the input samples) required to be at a leaf node. Samples have
     |      equal weight when sample_weight is not provided.
     |  
     |  subsample : float, optional (default=1.0)
     |      The fraction of samples to be used for fitting the individual base
     |      learners. If smaller than 1.0 this results in Stochastic Gradient
     |      Boosting. `subsample` interacts with the parameter `n_estimators`.
     |      Choosing `subsample < 1.0` leads to a reduction of variance
     |      and an increase in bias.
     |  
     |  max_features : int, float, string or None, optional (default=None)
     |      The number of features to consider when looking for the best split:
     |  
     |      - If int, then consider `max_features` features at each split.
     |      - If float, then `max_features` is a percentage and
     |        `int(max_features * n_features)` features are considered at each
     |        split.
     |      - If "auto", then `max_features=sqrt(n_features)`.
     |      - If "sqrt", then `max_features=sqrt(n_features)`.
     |      - If "log2", then `max_features=log2(n_features)`.
     |      - If None, then `max_features=n_features`.
     |  
     |      Choosing `max_features < n_features` leads to a reduction of variance
     |      and an increase in bias.
     |  
     |      Note: the search for a split does not stop until at least one
     |      valid partition of the node samples is found, even if it requires to
     |      effectively inspect more than ``max_features`` features.
     |  
     |  max_leaf_nodes : int or None, optional (default=None)
     |      Grow trees with ``max_leaf_nodes`` in best-first fashion.
     |      Best nodes are defined as relative reduction in impurity.
     |      If None then unlimited number of leaf nodes.
     |  
     |  min_impurity_split : float, optional (default=1e-7)
     |      Threshold for early stopping in tree growth. A node will split
     |      if its impurity is above the threshold, otherwise it is a leaf.
     |  
     |      .. versionadded:: 0.18
     |  
     |  init : BaseEstimator, None, optional (default=None)
     |      An estimator object that is used to compute the initial
     |      predictions. ``init`` has to provide ``fit`` and ``predict``.
     |      If None it uses ``loss.init_estimator``.
     |  
     |  verbose : int, default: 0
     |      Enable verbose output. If 1 then it prints progress and performance
     |      once in a while (the more trees the lower the frequency). If greater
     |      than 1 then it prints progress and performance for every tree.
     |  
     |  warm_start : bool, default: False
     |      When set to ``True``, reuse the solution of the previous call to fit
     |      and add more estimators to the ensemble, otherwise, just erase the
     |      previous solution.
     |  
     |  random_state : int, RandomState instance or None, optional (default=None)
     |      If int, random_state is the seed used by the random number generator;
     |      If RandomState instance, random_state is the random number generator;
     |      If None, the random number generator is the RandomState instance used
     |      by `np.random`.
     |  
     |  presort : bool or 'auto', optional (default='auto')
     |      Whether to presort the data to speed up the finding of best splits in
     |      fitting. Auto mode by default will use presorting on dense data and
     |      default to normal sorting on sparse data. Setting presort to true on
     |      sparse data will raise an error.
     |  
     |      .. versionadded:: 0.17
     |         *presort* parameter.
     |  
     |  Attributes
     |  ----------
     |  feature_importances_ : array, shape = [n_features]
     |      The feature importances (the higher, the more important the feature).
     |  
     |  oob_improvement_ : array, shape = [n_estimators]
     |      The improvement in loss (= deviance) on the out-of-bag samples
     |      relative to the previous iteration.
     |      ``oob_improvement_[0]`` is the improvement in
     |      loss of the first stage over the ``init`` estimator.
     |  
     |  train_score_ : array, shape = [n_estimators]
     |      The i-th score ``train_score_[i]`` is the deviance (= loss) of the
     |      model at iteration ``i`` on the in-bag sample.
     |      If ``subsample == 1`` this is the deviance on the training data.
     |  
     |  loss_ : LossFunction
     |      The concrete ``LossFunction`` object.
     |  
     |  init : BaseEstimator
     |      The estimator that provides the initial predictions.
     |      Set via the ``init`` argument or ``loss.init_estimator``.
     |  
     |  estimators_ : ndarray of DecisionTreeRegressor, shape = [n_estimators, ``loss_.K``]
     |      The collection of fitted sub-estimators. ``loss_.K`` is 1 for binary
     |      classification, otherwise n_classes.
     |  
     |  
     |  See also
     |  --------
     |  sklearn.tree.DecisionTreeClassifier, RandomForestClassifier
     |  AdaBoostClassifier
     |  
     |  References
     |  ----------
     |  J. Friedman, Greedy Function Approximation: A Gradient Boosting
     |  Machine, The Annals of Statistics, Vol. 29, No. 5, 2001.
     |  
     |  J. Friedman, Stochastic Gradient Boosting, 1999
     |  
     |  T. Hastie, R. Tibshirani and J. Friedman.
     |  Elements of Statistical Learning Ed. 2, Springer, 2009.
     |  
     |  Method resolution order:
     |      GradientBoostingClassifier
     |      BaseGradientBoosting
     |      abc.NewBase
     |      sklearn.ensemble.base.BaseEnsemble
     |      sklearn.base.BaseEstimator
     |      sklearn.base.MetaEstimatorMixin
     |      sklearn.feature_selection.from_model._LearntSelectorMixin
     |      sklearn.base.TransformerMixin
     |      sklearn.base.ClassifierMixin
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, loss='deviance', learning_rate=0.1, n_estimators=100, subsample=1.0, criterion='friedman_mse', min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_depth=3, min_impurity_split=1e-07, init=None, random_state=None, max_features=None, verbose=0, max_leaf_nodes=None, warm_start=False, presort='auto')
     |  
     |  decision_function(self, X)
     |      Compute the decision function of ``X``.
     |      
     |      Parameters
     |      ----------
     |      X : array-like of shape = [n_samples, n_features]
     |          The input samples.
     |      
     |      Returns
     |      -------
     |      score : array, shape = [n_samples, n_classes] or [n_samples]
     |          The decision function of the input samples. The order of the
     |          classes corresponds to that in the attribute `classes_`.
     |          Regression and binary classification produce an array of shape
     |          [n_samples].
     |  
     |  predict(self, X)
     |      Predict class for X.
     |      
     |      Parameters
     |      ----------
     |      X : array-like of shape = [n_samples, n_features]
     |          The input samples.
     |      
     |      Returns
     |      -------
     |      y: array of shape = ["n_samples]
     |          The predicted values.
     |  
     |  predict_log_proba(self, X)
     |      Predict class log-probabilities for X.
     |      
     |      Parameters
     |      ----------
     |      X : array-like of shape = [n_samples, n_features]
     |          The input samples.
     |      
     |      Raises
     |      ------
     |      AttributeError
     |          If the ``loss`` does not support probabilities.
     |      
     |      Returns
     |      -------
     |      p : array of shape = [n_samples]
     |          The class log-probabilities of the input samples. The order of the
     |          classes corresponds to that in the attribute `classes_`.
     |  
     |  predict_proba(self, X)
     |      Predict class probabilities for X.
     |      
     |      Parameters
     |      ----------
     |      X : array-like of shape = [n_samples, n_features]
     |          The input samples.
     |      
     |      Raises
     |      ------
     |      AttributeError
     |          If the ``loss`` does not support probabilities.
     |      
     |      Returns
     |      -------
     |      p : array of shape = [n_samples]
     |          The class probabilities of the input samples. The order of the
     |          classes corresponds to that in the attribute `classes_`.
     |  
     |  staged_decision_function(self, X)
     |      Compute decision function of ``X`` for each iteration.
     |      
     |      This method allows monitoring (i.e. determine error on testing set)
     |      after each stage.
     |      
     |      Parameters
     |      ----------
     |      X : array-like of shape = [n_samples, n_features]
     |          The input samples.
     |      
     |      Returns
     |      -------
     |      score : generator of array, shape = [n_samples, k]
     |          The decision function of the input samples. The order of the
     |          classes corresponds to that in the attribute `classes_`.
     |          Regression and binary classification are special cases with
     |          ``k == 1``, otherwise ``k==n_classes``.
     |  
     |  staged_predict(self, X)
     |      Predict class at each stage for X.
     |      
     |      This method allows monitoring (i.e. determine error on testing set)
     |      after each stage.
     |      
     |      Parameters
     |      ----------
     |      X : array-like of shape = [n_samples, n_features]
     |          The input samples.
     |      
     |      Returns
     |      -------
     |      y : generator of array of shape = [n_samples]
     |          The predicted value of the input samples.
     |  
     |  staged_predict_proba(self, X)
     |      Predict class probabilities at each stage for X.
     |      
     |      This method allows monitoring (i.e. determine error on testing set)
     |      after each stage.
     |      
     |      Parameters
     |      ----------
     |      X : array-like of shape = [n_samples, n_features]
     |          The input samples.
     |      
     |      Returns
     |      -------
     |      y : generator of array of shape = [n_samples]
     |          The predicted value of the input samples.
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  __abstractmethods__ = frozenset([])
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseGradientBoosting:
     |  
     |  apply(self, X)
     |      Apply trees in the ensemble to X, return leaf indices.
     |      
     |      .. versionadded:: 0.17
     |      
     |      Parameters
     |      ----------
     |      X : array-like or sparse matrix, shape = [n_samples, n_features]
     |          The input samples. Internally, its dtype will be converted to
     |          ``dtype=np.float32``. If a sparse matrix is provided, it will
     |          be converted to a sparse ``csr_matrix``.
     |      
     |      Returns
     |      -------
     |      X_leaves : array_like, shape = [n_samples, n_estimators, n_classes]
     |          For each datapoint x in X and for each tree in the ensemble,
     |          return the index of the leaf x ends up in each estimator.
     |          In the case of binary classification n_classes is 1.
     |  
     |  fit(self, X, y, sample_weight=None, monitor=None)
     |      Fit the gradient boosting model.
     |      
     |      Parameters
     |      ----------
     |      X : array-like, shape = [n_samples, n_features]
     |          Training vectors, where n_samples is the number of samples
     |          and n_features is the number of features.
     |      
     |      y : array-like, shape = [n_samples]
     |          Target values (integers in classification, real numbers in
     |          regression)
     |          For classification, labels must correspond to classes.
     |      
     |      sample_weight : array-like, shape = [n_samples] or None
     |          Sample weights. If None, then samples are equally weighted. Splits
     |          that would create child nodes with net zero or negative weight are
     |          ignored while searching for a split in each node. In the case of
     |          classification, splits are also ignored if they would result in any
     |          single class carrying a negative weight in either child node.
     |      
     |      monitor : callable, optional
     |          The monitor is called after each iteration with the current
     |          iteration, a reference to the estimator and the local variables of
     |          ``_fit_stages`` as keyword arguments ``callable(i, self,
     |          locals())``. If the callable returns ``True`` the fitting procedure
     |          is stopped. The monitor can be used for various things such as
     |          computing held-out estimates, early stopping, model introspect, and
     |          snapshoting.
     |      
     |      Returns
     |      -------
     |      self : object
     |          Returns self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseGradientBoosting:
     |  
     |  feature_importances_
     |      Return the feature importances (the higher, the more important the
     |         feature).
     |      
     |      Returns
     |      -------
     |      feature_importances_ : array, shape = [n_features]
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from sklearn.ensemble.base.BaseEnsemble:
     |  
     |  __getitem__(self, index)
     |      Returns the index'th estimator in the ensemble.
     |  
     |  __iter__(self)
     |      Returns iterator over estimators in the ensemble.
     |  
     |  __len__(self)
     |      Returns the number of estimators in the ensemble.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from sklearn.base.BaseEstimator:
     |  
     |  __getstate__(self)
     |  
     |  __repr__(self)
     |  
     |  __setstate__(self, state)
     |  
     |  get_params(self, deep=True)
     |      Get parameters for this estimator.
     |      
     |      Parameters
     |      ----------
     |      deep : boolean, optional
     |          If True, will return the parameters for this estimator and
     |          contained subobjects that are estimators.
     |      
     |      Returns
     |      -------
     |      params : mapping of string to any
     |          Parameter names mapped to their values.
     |  
     |  set_params(self, **params)
     |      Set the parameters of this estimator.
     |      
     |      The method works on simple estimators as well as on nested objects
     |      (such as pipelines). The latter have parameters of the form
     |      ``<component>__<parameter>`` so that it's possible to update each
     |      component of a nested object.
     |      
     |      Returns
     |      -------
     |      self
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from sklearn.base.BaseEstimator:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from sklearn.feature_selection.from_model._LearntSelectorMixin:
     |  
     |  transform(*args, **kwargs)
     |      DEPRECATED: Support to use estimators as feature selectors will be removed in version 0.19. Use SelectFromModel instead.
     |      
     |      Reduce X to its most important features.
     |      
     |              Uses ``coef_`` or ``feature_importances_`` to determine the most
     |              important features.  For models with a ``coef_`` for each class, the
     |              absolute sum over the classes is used.
     |      
     |              Parameters
     |              ----------
     |              X : array or scipy sparse matrix of shape [n_samples, n_features]
     |                  The input samples.
     |      
     |              threshold : string, float or None, optional (default=None)
     |                  The threshold value to use for feature selection. Features whose
     |                  importance is greater or equal are kept while the others are
     |                  discarded. If "median" (resp. "mean"), then the threshold value is
     |                  the median (resp. the mean) of the feature importances. A scaling
     |                  factor (e.g., "1.25*mean") may also be used. If None and if
     |                  available, the object attribute ``threshold`` is used. Otherwise,
     |                  "mean" is used by default.
     |      
     |              Returns
     |              -------
     |              X_r : array of shape [n_samples, n_selected_features]
     |                  The input samples with only the selected features.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from sklearn.base.TransformerMixin:
     |  
     |  fit_transform(self, X, y=None, **fit_params)
     |      Fit to data, then transform it.
     |      
     |      Fits transformer to X and y with optional parameters fit_params
     |      and returns a transformed version of X.
     |      
     |      Parameters
     |      ----------
     |      X : numpy array of shape [n_samples, n_features]
     |          Training set.
     |      
     |      y : numpy array of shape [n_samples]
     |          Target values.
     |      
     |      Returns
     |      -------
     |      X_new : numpy array of shape [n_samples, n_features_new]
     |          Transformed array.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from sklearn.base.ClassifierMixin:
     |  
     |  score(self, X, y, sample_weight=None)
     |      Returns the mean accuracy on the given test data and labels.
     |      
     |      In multi-label classification, this is the subset accuracy
     |      which is a harsh metric since you require for each sample that
     |      each label set be correctly predicted.
     |      
     |      Parameters
     |      ----------
     |      X : array-like, shape = (n_samples, n_features)
     |          Test samples.
     |      
     |      y : array-like, shape = (n_samples) or (n_samples, n_outputs)
     |          True labels for X.
     |      
     |      sample_weight : array-like, shape = [n_samples], optional
     |          Sample weights.
     |      
     |      Returns
     |      -------
     |      score : float
     |          Mean accuracy of self.predict(X) wrt. y.
    



```python
#自己的方法
score_gbrt=cross_val_score(gbrt_model,tanic[ensemble_fea],tanic["Survived"],cv=5,scoring="accuracy")
score_lg=cross_val_score(lg_model,tanic[ensemble_fea],tanic["Survived"],cv=5,scoring="accuracy")
score_ensemble=(score_gbrt+score_lg)/2
print "accuracy_semble_gbrt_lg is :{0:.3f}%".format(score_ensemble.mean()*100)
```

    accuracy_semble_gbrt_lg is :80.415%



```python
test_tanic=pd.read_csv("test.csv")
test_tanic.describe()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Pclass</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Fare</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>418.000000</td>
      <td>418.000000</td>
      <td>332.000000</td>
      <td>418.000000</td>
      <td>418.000000</td>
      <td>417.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>1100.500000</td>
      <td>2.265550</td>
      <td>30.272590</td>
      <td>0.447368</td>
      <td>0.392344</td>
      <td>35.627188</td>
    </tr>
    <tr>
      <th>std</th>
      <td>120.810458</td>
      <td>0.841838</td>
      <td>14.181209</td>
      <td>0.896760</td>
      <td>0.981429</td>
      <td>55.907576</td>
    </tr>
    <tr>
      <th>min</th>
      <td>892.000000</td>
      <td>1.000000</td>
      <td>0.170000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>996.250000</td>
      <td>1.000000</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>1100.500000</td>
      <td>3.000000</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>1204.750000</td>
      <td>3.000000</td>
      <td>NaN</td>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>max</th>
      <td>1309.000000</td>
      <td>3.000000</td>
      <td>76.000000</td>
      <td>8.000000</td>
      <td>9.000000</td>
      <td>512.329200</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>892</td>
      <td>3</td>
      <td>Kelly, Mr. James</td>
      <td>0</td>
      <td>34.5</td>
      <td>0</td>
      <td>0</td>
      <td>330911</td>
      <td>7.8292</td>
      <td>NaN</td>
      <td>Q</td>
    </tr>
    <tr>
      <th>1</th>
      <td>893</td>
      <td>3</td>
      <td>Wilkes, Mrs. James (Ellen Needs)</td>
      <td>1</td>
      <td>47.0</td>
      <td>1</td>
      <td>0</td>
      <td>363272</td>
      <td>7.0000</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>2</th>
      <td>894</td>
      <td>2</td>
      <td>Myles, Mr. Thomas Francis</td>
      <td>0</td>
      <td>62.0</td>
      <td>0</td>
      <td>0</td>
      <td>240276</td>
      <td>9.6875</td>
      <td>NaN</td>
      <td>Q</td>
    </tr>
    <tr>
      <th>3</th>
      <td>895</td>
      <td>3</td>
      <td>Wirz, Mr. Albert</td>
      <td>0</td>
      <td>27.0</td>
      <td>0</td>
      <td>0</td>
      <td>315154</td>
      <td>8.6625</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>4</th>
      <td>896</td>
      <td>3</td>
      <td>Hirvonen, Mrs. Alexander (Helga E Lindqvist)</td>
      <td>1</td>
      <td>22.0</td>
      <td>1</td>
      <td>1</td>
      <td>3101298</td>
      <td>12.2875</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
```




    array([2, 0, 1], dtype=object)




```python
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
```

    /home/zzpp220/anaconda2/lib/python2.7/site-packages/ipykernel/__main__.py:31: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy


    1    240
    2     79
    3     72
    4     21
    7      2
    6      2
    9      1
    5      1
    Name: Title, dtype: int64



```python

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
```

    2



```python
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
```

    <type 'numpy.ndarray'>
                 precision    recall  f1-score   support
    
              0       0.93      0.95      0.94       266
              1       0.91      0.88      0.89       152
    
    avg / total       0.92      0.92      0.92       418
    
    [[252  14]
     [ 18 134]]



```python
#回头看看auc,roc的值的情况
from sklearn.metrics import roc_curve,auc,roc_auc_score

print "auc: ",roc_auc_score(test_label,fina_sysout)#
print "auc: ",roc_auc_score(test_label,fina_proba)
```

    auc:  0.977715670756
    auc:  0.977715670756



```python
help(roc_auc_score)
```

    Help on function roc_auc_score in module sklearn.metrics.ranking:
    
    roc_auc_score(y_true, y_score, average='macro', sample_weight=None)
        Compute Area Under the Curve (AUC) from prediction scores
        
        Note: this implementation is restricted to the binary classification task
        or multilabel classification task in label indicator format.
        
        Read more in the :ref:`User Guide <roc_metrics>`.
        
        Parameters
        ----------
        y_true : array, shape = [n_samples] or [n_samples, n_classes]
            True binary labels in binary label indicators.
        
        y_score : array, shape = [n_samples] or [n_samples, n_classes]
            Target scores, can either be probability estimates of the positive
            class, confidence values, or non-thresholded measure of decisions
            (as returned by "decision_function" on some classifiers).
        
        average : string, [None, 'micro', 'macro' (default), 'samples', 'weighted']
            If ``None``, the scores for each class are returned. Otherwise,
            this determines the type of averaging performed on the data:
        
            ``'micro'``:
                Calculate metrics globally by considering each element of the label
                indicator matrix as a label.
            ``'macro'``:
                Calculate metrics for each label, and find their unweighted
                mean.  This does not take label imbalance into account.
            ``'weighted'``:
                Calculate metrics for each label, and find their average, weighted
                by support (the number of true instances for each label).
            ``'samples'``:
                Calculate metrics for each instance, and find their average.
        
        sample_weight : array-like of shape = [n_samples], optional
            Sample weights.
        
        Returns
        -------
        auc : float
        
        References
        ----------
        .. [1] `Wikipedia entry for the Receiver operating characteristic
                <https://en.wikipedia.org/wiki/Receiver_operating_characteristic>`_
        
        See also
        --------
        average_precision_score : Area under the precision-recall curve
        
        roc_curve : Compute Receiver operating characteristic (ROC)
        
        Examples
        --------
        >>> import numpy as np
        >>> from sklearn.metrics import roc_auc_score
        >>> y_true = np.array([0, 0, 1, 1])
        >>> y_scores = np.array([0.1, 0.4, 0.35, 0.8])
        >>> roc_auc_score(y_true, y_scores)
        0.75
    



```python
help(auc)
```

    Help on function auc in module sklearn.metrics.ranking:
    
    auc(x, y, reorder=False)
        Compute Area Under the Curve (AUC) using the trapezoidal rule
        
        This is a general function, given points on a curve.  For computing the
        area under the ROC-curve, see :func:`roc_auc_score`.
        
        Parameters
        ----------
        x : array, shape = [n]
            x coordinates.
        
        y : array, shape = [n]
            y coordinates.
        
        reorder : boolean, optional (default=False)
            If True, assume that the curve is ascending in the case of ties, as for
            an ROC curve. If the curve is non-ascending, the result will be wrong.
        
        Returns
        -------
        auc : float
        
        Examples
        --------
        >>> import numpy as np
        >>> from sklearn import metrics
        >>> y = np.array([1, 1, 2, 2])
        >>> pred = np.array([0.1, 0.4, 0.35, 0.8])
        >>> fpr, tpr, thresholds = metrics.roc_curve(y, pred, pos_label=2)
        >>> metrics.auc(fpr, tpr)
        0.75
        
        See also
        --------
        roc_auc_score : Computes the area under the ROC curve
        
        precision_recall_curve :
            Compute precision-recall pairs for different probability thresholds
    



```python
help(roc_curve)
```

    Help on function roc_curve in module sklearn.metrics.ranking:
    
    roc_curve(y_true, y_score, pos_label=None, sample_weight=None, drop_intermediate=True)
        Compute Receiver operating characteristic (ROC)
        
        Note: this implementation is restricted to the binary classification task.
        
        Read more in the :ref:`User Guide <roc_metrics>`.
        
        Parameters
        ----------
        
        y_true : array, shape = [n_samples]
            True binary labels in range {0, 1} or {-1, 1}.  If labels are not
            binary, pos_label should be explicitly given.
        
        y_score : array, shape = [n_samples]
            Target scores, can either be probability estimates of the positive
            class, confidence values, or non-thresholded measure of decisions
            (as returned by "decision_function" on some classifiers).
        
        pos_label : int or str, default=None
            Label considered as positive and others are considered negative.
        
        sample_weight : array-like of shape = [n_samples], optional
            Sample weights.
        
        drop_intermediate : boolean, optional (default=True)
            Whether to drop some suboptimal thresholds which would not appear
            on a plotted ROC curve. This is useful in order to create lighter
            ROC curves.
        
            .. versionadded:: 0.17
               parameter *drop_intermediate*.
        
        Returns
        -------
        fpr : array, shape = [>2]
            Increasing false positive rates such that element i is the false
            positive rate of predictions with score >= thresholds[i].
        
        tpr : array, shape = [>2]
            Increasing true positive rates such that element i is the true
            positive rate of predictions with score >= thresholds[i].
        
        thresholds : array, shape = [n_thresholds]
            Decreasing thresholds on the decision function used to compute
            fpr and tpr. `thresholds[0]` represents no instances being predicted
            and is arbitrarily set to `max(y_score) + 1`.
        
        See also
        --------
        roc_auc_score : Compute Area Under the Curve (AUC) from prediction scores
        
        Notes
        -----
        Since the thresholds are sorted from low to high values, they
        are reversed upon returning them to ensure they correspond to both ``fpr``
        and ``tpr``, which are sorted in reversed order during their calculation.
        
        References
        ----------
        .. [1] `Wikipedia entry for the Receiver operating characteristic
                <https://en.wikipedia.org/wiki/Receiver_operating_characteristic>`_
        
        
        Examples
        --------
        >>> import numpy as np
        >>> from sklearn import metrics
        >>> y = np.array([1, 1, 2, 2])
        >>> scores = np.array([0.1, 0.4, 0.35, 0.8])
        >>> fpr, tpr, thresholds = metrics.roc_curve(y, scores, pos_label=2)
        >>> fpr
        array([ 0. ,  0.5,  0.5,  1. ])
        >>> tpr
        array([ 0.5,  0.5,  1. ,  1. ])
        >>> thresholds
        array([ 0.8 ,  0.4 ,  0.35,  0.1 ])
    



```python
fina_proba
```




    array([ 0.12162225,  0.48772383,  0.11891431,  0.11772443,  0.54349687,
            0.1310479 ,  0.61331407,  0.19454212,  0.7063859 ,  0.12441115,
            0.11634258,  0.21853977,  0.91259616,  0.09742088,  0.90448876,
            0.87754648,  0.15955972,  0.12949051,  0.49644922,  0.62813377,
            0.22590665,  0.36896991,  0.90049095,  0.50201624,  0.91460642,
            0.10482728,  0.91460807,  0.12834476,  0.29502843,  0.12340609,
            0.12471476,  0.19846706,  0.51801514,  0.35212278,  0.35131959,
            0.38329979,  0.46361052,  0.47936358,  0.1183162 ,  0.33074008,
            0.11156452,  0.42045143,  0.10720293,  0.84605224,  0.90882524,
            0.12577294,  0.31089926,  0.13715631,  0.90513413,  0.52121475,
            0.33927603,  0.1609439 ,  0.84256592,  0.8960059 ,  0.20085515,
            0.22363499,  0.10764952,  0.1246951 ,  0.11992135,  0.90884923,
            0.12268923,  0.14598626,  0.12911936,  0.6699288 ,  0.77911605,
            0.86691585,  0.66995049,  0.33735539,  0.468842  ,  0.88403002,
            0.66266916,  0.12173245,  0.49566405,  0.47364208,  0.88805614,
            0.34359421,  0.11634403,  0.85441117,  0.15322165,  0.65855782,
            0.60126994,  0.17952625,  0.20892281,  0.1178083 ,  0.17877033,
            0.12381207,  0.61591424,  0.49753535,  0.64928832,  0.70351295,
            0.58005734,  0.11705835,  0.90242623,  0.11669865,  0.26918305,
            0.12316559,  0.87040198,  0.12036785,  0.52458433,  0.11317022,
            0.92261736,  0.14562565,  0.13282153,  0.15542603,  0.66016833,
            0.12110002,  0.14221404,  0.13147958,  0.13004522,  0.15467759,
            0.14257822,  0.6536086 ,  0.89507601,  0.69380935,  0.8742181 ,
            0.13937869,  0.12271082,  0.66057653,  0.33431053,  0.86477286,
            0.8434386 ,  0.13214429,  0.9125068 ,  0.12003622,  0.13214429,
            0.51151839,  0.12405255,  0.56682155,  0.12582171,  0.12093001,
            0.11799974,  0.44642305,  0.26156989,  0.12526776,  0.10677553,
            0.12329204,  0.1301852 ,  0.14737398,  0.48010222,  0.14674583,
            0.28494191,  0.88592081,  0.21491352,  0.15206412,  0.69698659,
            0.11941386,  0.36391718,  0.12027005,  0.37060775,  0.30681216,
            0.91986628,  0.12475615,  0.08658898,  0.5210638 ,  0.17634026,
            0.12092396,  0.88877919,  0.51258013,  0.3478582 ,  0.52342965,
            0.61034442,  0.4892634 ,  0.82279001,  0.1170507 ,  0.29669576,
            0.51484851,  0.29791596,  0.1643153 ,  0.91407495,  0.49293006,
            0.11705613,  0.12624252,  0.12350001,  0.12272118,  0.17724697,
            0.85825666,  0.84578636,  0.31192677,  0.87017074,  0.898133  ,
            0.14830188,  0.50669869,  0.92482538,  0.13214429,  0.92310615,
            0.13128587,  0.84834564,  0.12419292,  0.22130105,  0.12418653,
            0.13348742,  0.24079596,  0.4380721 ,  0.11379983,  0.6567145 ,
            0.14035593,  0.81581944,  0.52689383,  0.16266857,  0.50688285,
            0.58387796,  0.64377053,  0.50081154,  0.85429696,  0.15342466,
            0.23698041,  0.64151644,  0.15900745,  0.89332269,  0.11951703,
            0.11977936,  0.11668899,  0.19642245,  0.80908911,  0.50514535,
            0.2911707 ,  0.65361244,  0.21005122,  0.91179155,  0.12255022,
            0.85313512,  0.12367567,  0.83777797,  0.12747165,  0.90110325,
            0.66429942,  0.12443871,  0.64783005,  0.10867301,  0.16836236,
            0.20332319,  0.87919392,  0.12416475,  0.1342167 ,  0.33603574,
            0.12431456,  0.20131977,  0.13157356,  0.83622703,  0.91120049,
            0.88928541,  0.82742547,  0.37539388,  0.11705946,  0.22427919,
            0.29579909,  0.85559915,  0.16339017,  0.85053327,  0.63899319,
            0.81211   ,  0.16182376,  0.36044377,  0.12281877,  0.10997327,
            0.12025311,  0.13082728,  0.119203  ,  0.83707596,  0.12470358,
            0.13983694,  0.12747257,  0.86635665,  0.65645976,  0.20733813,
            0.11819497,  0.33571692,  0.1206923 ,  0.47581703,  0.12369046,
            0.37112024,  0.13147958,  0.92127308,  0.58387796,  0.12527917,
            0.84872204,  0.15367126,  0.12850514,  0.14393732,  0.15846549,
            0.48167704,  0.58087443,  0.61479412,  0.64314871,  0.65370863,
            0.10849022,  0.15248981,  0.34327682,  0.12637686,  0.11634403,
            0.48642569,  0.56349821,  0.12321217,  0.4562885 ,  0.11054824,
            0.11983246,  0.82934437,  0.12340609,  0.31956083,  0.11790498,
            0.11878685,  0.15788999,  0.13005191,  0.11963211,  0.66331831,
            0.87503505,  0.50552024,  0.5612116 ,  0.21300133,  0.46762088,
            0.12458987,  0.13059299,  0.11742664,  0.59854978,  0.90387981,
            0.63611528,  0.26924251,  0.16383979,  0.12149156,  0.2001776 ,
            0.12304029,  0.12886813,  0.14644862,  0.35504988,  0.88285515,
            0.15525557,  0.86479699,  0.50610103,  0.15384048,  0.15350674,
            0.86095478,  0.37076657,  0.1242247 ,  0.6514729 ,  0.15297506,
            0.24374948,  0.14689178,  0.11188783,  0.1877126 ,  0.45574163,
            0.16891891,  0.11919252,  0.1476362 ,  0.91808224,  0.41721849,
            0.53071499,  0.15426318,  0.69704934,  0.14692785,  0.81741993,
            0.91276813,  0.15445592,  0.18802684,  0.14738105,  0.67188733,
            0.18448538,  0.8846729 ,  0.11742971,  0.13421423,  0.55693783,
            0.16671143,  0.88613254,  0.85179649,  0.11810927,  0.92713048,
            0.25688178,  0.12330899,  0.28750724,  0.91050784,  0.17099599,
            0.15045861,  0.9052104 ,  0.17749892,  0.12548342,  0.88788583,
            0.89653278,  0.47588181,  0.1632835 ,  0.23752109,  0.23594666,
            0.13492996,  0.13567074,  0.50200084,  0.53634002,  0.15321821,
            0.83181342,  0.12590977,  0.09830351,  0.14306865,  0.48433558,
            0.34568052,  0.89154912,  0.41722998,  0.12181593,  0.12009865,
            0.91452435,  0.13991194,  0.91834099,  0.12732449,  0.13621139,
            0.89098271,  0.1259753 ,  0.91532638,  0.33845956,  0.36306226,
            0.46486264,  0.15710574,  0.2873392 ,  0.66059926,  0.64897117,
            0.64783005,  0.92179878,  0.51216431,  0.11706107,  0.83271699,
            0.1104782 ,  0.11743143,  0.43041973])




```python
fp,tp,thr=roc_curve(test_label,fina_proba)#参数为测试集样本的参考标签，以及系统输出的概率
fp1,tp1,thr1=roc_curve(test_label,fina_sysout)
#print fp,"\n",tp,"\n",thr
print "auc_proba: ",auc(fp,tp)
print "auc_sysout_label: ",auc(fp1,tp1)
```

     auc_proba:  0.977715670756
    auc_sysout_label:  0.977715670756



```python
help(pd.get_dummies)#categorical variable：分类变量；dummies variables:虚拟变量
```

    Help on function get_dummies in module pandas.core.reshape:
    
    get_dummies(data, prefix=None, prefix_sep='_', dummy_na=False, columns=None, sparse=False, drop_first=False)
        Convert categorical variable into dummy/indicator variables
        
        Parameters
        ----------
        data : array-like, Series, or DataFrame
        prefix : string, list of strings, or dict of strings, default None
            String to append DataFrame column names
            Pass a list with length equal to the number of columns
            when calling get_dummies on a DataFrame. Alternativly, `prefix`
            can be a dictionary mapping column names to prefixes.
        prefix_sep : string, default '_'
            If appending prefix, separator/delimiter to use. Or pass a
            list or dictionary as with `prefix.`
        dummy_na : bool, default False
            Add a column to indicate NaNs, if False NaNs are ignored.
        columns : list-like, default None
            Column names in the DataFrame to be encoded.
            If `columns` is None then all the columns with
            `object` or `category` dtype will be converted.
        sparse : bool, default False
            Whether the dummy columns should be sparse or not.  Returns
            SparseDataFrame if `data` is a Series or if all columns are included.
            Otherwise returns a DataFrame with some SparseBlocks.
        
            .. versionadded:: 0.16.1
        drop_first : bool, default False
            Whether to get k-1 dummies out of n categorical levels by removing the
            first level.
        
            .. versionadded:: 0.18.0
        Returns
        -------
        dummies : DataFrame or SparseDataFrame
        
        Examples
        --------
        >>> import pandas as pd
        >>> s = pd.Series(list('abca'))
        
        >>> pd.get_dummies(s)
           a  b  c
        0  1  0  0
        1  0  1  0
        2  0  0  1
        3  1  0  0
        
        >>> s1 = ['a', 'b', np.nan]
        
        >>> pd.get_dummies(s1)
           a  b
        0  1  0
        1  0  1
        2  0  0
        
        >>> pd.get_dummies(s1, dummy_na=True)
           a  b  NaN
        0  1  0    0
        1  0  1    0
        2  0  0    1
        
        >>> df = pd.DataFrame({'A': ['a', 'b', 'a'], 'B': ['b', 'a', 'c'],
                            'C': [1, 2, 3]})
        
        >>> pd.get_dummies(df, prefix=['col1', 'col2'])
           C  col1_a  col1_b  col2_a  col2_b  col2_c
        0  1       1       0       0       1       0
        1  2       0       1       1       0       0
        2  3       1       0       0       0       1
        
        >>> pd.get_dummies(pd.Series(list('abcaa')))
           a  b  c
        0  1  0  0
        1  0  1  0
        2  0  0  1
        3  1  0  0
        4  1  0  0
        
        >>> pd.get_dummies(pd.Series(list('abcaa')), drop_first=True))
           b  c
        0  0  0
        1  1  0
        2  0  1
        3  0  0
        4  0  0
        
        See Also
        --------
        Series.str.get_dummies
    



```python

```
