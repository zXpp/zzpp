

```python
import pandas #ipython notebook
titanic = pandas.read_csv("titanic_train.csv")
#titanic.head(3)
print titanic.describe()
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
    
                Parch          Fare  
    count  891.000000  8.910000e+02  
    mean     0.381594  6.207701e+04  
    std      0.806057  4.128041e+05  
    min      0.000000  0.000000e+00  
    25%      0.000000  8.050000e+00  
    50%      0.000000  2.415000e+01  
    75%      0.000000  1.515500e+02  
    max      6.000000  3.101317e+06  



```python
titanic["Age"] = titanic["Age"].fillna(titanic["Age"].median())#数据预处理 数据缺失，进行填充--该列 的均值填充
print titanic.describe()
```

           PassengerId    Survived      Pclass         Age       SibSp  \
    count   891.000000  891.000000  891.000000  891.000000  891.000000   
    mean    446.000000    0.383838    2.308642   29.361582    0.523008   
    std     257.353842    0.486592    0.836071   13.019697    1.102743   
    min       1.000000    0.000000    1.000000    0.420000    0.000000   
    25%     223.500000    0.000000    2.000000   22.000000    0.000000   
    50%     446.000000    0.000000    3.000000   28.000000    0.000000   
    75%     668.500000    1.000000    3.000000   35.000000    1.000000   
    max     891.000000    1.000000    3.000000   80.000000    8.000000   
    
                Parch          Fare  
    count  891.000000  8.910000e+02  
    mean     0.381594  6.207701e+04  
    std      0.806057  4.128041e+05  
    min      0.000000  0.000000e+00  
    25%      0.000000  8.050000e+00  
    50%      0.000000  2.415000e+01  
    75%      0.000000  1.515500e+02  
    max      6.000000  3.101317e+06  



```python
print titanic["Sex"].unique()

# Replace all the occurences of male with the number 0.#数值处理，将str类型转换为0,1 变成机器学习可以处理的值--二值化处理
titanic.loc[titanic["Sex"] == "male", "Sex"] = 0
titanic.loc[titanic["Sex"] == "female", "Sex"] = 1
print titanic["Sex"].unique()

```

    ['male' 'female']
    [0 1]



```python
help(titanic.loc)
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
print titanic["Embarked"].unique()#先看看该列的取值都有哪一些？
titanic["Embarked"] = titanic["Embarked"].fillna('S') #填充缺失值
titanic.loc[titanic["Embarked"] == "S", "Embarked"] = 0#一下都是进行数值转化
titanic.loc[titanic["Embarked"] == "C", "Embarked"] = 1
titanic.loc[titanic["Embarked"] == "Q", "Embarked"] = 2
print titanic["Embarked"].unique()
```

    ['S' 'C' 'Q' nan]
    [0 1 2]



```python

```


```python
# Import the linear regression class
from sklearn.linear_model import LinearRegression
# Sklearn also has a helper that makes it easy to do cross validation
from sklearn.cross_validation import KFold

# The columns we'll use to predict the target
predictors = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]#选取的样本数据的特征，目标是预测能否存活

# Initialize our algorithm class
alg = LinearRegression() #建立线性回归模型的
# Generate cross validation folds for the titanic dataset.  It return the row indices corresponding to train and test.
# We set random_state to ensure we get the same splits every time we run this.
print titanic.shape
kf = KFold(titanic.shape[0], n_folds=5, random_state=1)#，输入样本数，做5层的交叉验证
kf
```

    (891, 12)





    sklearn.cross_validation.KFold(n=891, n_folds=5, shuffle=False, random_state=1)




```python
print [titanic[i].unique() for i in predictors]
```

    [array([3, 1, 2]), array([0, 1], dtype=object), array([ 22.  ,  38.  ,  26.  ,  35.  ,  28.  ,  54.  ,   2.  ,  27.  ,
            14.  ,   4.  ,  58.  ,  20.  ,  39.  ,  55.  ,  31.  ,  34.  ,
            15.  ,   8.  ,  19.  ,  40.  ,  66.  ,  42.  ,  21.  ,  18.  ,
             3.  ,   7.  ,  49.  ,  29.  ,  65.  ,  28.5 ,   5.  ,  11.  ,
            45.  ,  17.  ,  32.  ,  16.  ,  25.  ,   0.83,  30.  ,  33.  ,
            23.  ,  24.  ,  46.  ,  59.  ,  71.  ,  37.  ,  47.  ,  14.5 ,
            70.5 ,  32.5 ,  12.  ,   9.  ,  36.5 ,  51.  ,  55.5 ,  40.5 ,
            44.  ,   1.  ,  61.  ,  56.  ,  50.  ,  36.  ,  45.5 ,  20.5 ,
            62.  ,  41.  ,  52.  ,  63.  ,  23.5 ,   0.92,  43.  ,  60.  ,
            10.  ,  64.  ,  13.  ,  48.  ,   0.75,  53.  ,  57.  ,  80.  ,
            70.  ,  24.5 ,   6.  ,   0.67,  30.5 ,   0.42,  34.5 ,  74.  ]), array([1, 0, 3, 4, 2, 5, 8]), array([0, 1, 2, 5, 3, 4, 6]), array([  7.25000000e+00,   7.12833000e+01,   3.10128200e+06,
             5.31000000e+01,   8.05000000e+00,   8.45830000e+00,
             5.18625000e+01,   2.10750000e+01,   1.11333000e+01,
             3.00708000e+01,   9.54900000e+03,   2.65500000e+01,
             2.15100000e+03,   3.12750000e+01,   7.85420000e+00,
             1.60000000e+01,   2.91250000e+01,   1.30000000e+01,
             1.80000000e+01,   7.22500000e+00,   2.60000000e+01,
             8.02920000e+00,   3.55000000e+01,   3.13875000e+01,
             2.63000000e+02,   7.87920000e+00,   7.89580000e+00,
             1.76010000e+04,   1.75690000e+04,   7.75000000e+00,
             2.45790000e+04,   1.76040000e+04,   5.20000000e+01,
             7.22920000e+00,   2.15200000e+03,   1.12417000e+01,
             9.47500000e+00,   2.10000000e+01,   2.12300000e+03,
             2.35670000e+04,   1.55000000e+01,   2.16792000e+01,
             1.78000000e+01,   3.96875000e+01,   3.98860000e+04,
             1.75720000e+04,   6.19792000e+01,   3.10260000e+04,
             3.46510000e+04,   2.14400000e+03,   8.00000000e+01,
             8.34750000e+01,   2.79000000e+01,   1.76050000e+04,
             1.52458000e+01,   2.93950000e+04,   3.46400000e+03,
             7.92500000e+00,   8.66250000e+00,   3.31110000e+04,
             1.48790000e+04,   1.44542000e+01,   5.64958000e+01,
             7.65000000e+00,   2.90000000e+01,   1.24750000e+01,
             9.00000000e+00,   9.50000000e+00,   7.78750000e+00,
             4.71000000e+01,   1.48850000e+04,   1.58500000e+01,
             6.60800000e+03,   3.92086000e+05,   5.73400000e+03,
             2.31500000e+03,   1.77540000e+04,   1.77590000e+04,
             2.30000000e+01,   7.72875000e+01,   8.65420000e+00,
             7.77500000e+00,   2.41500000e+01,   9.82500000e+00,
             1.44583000e+01,   2.00000000e+00,   1.75580000e+04,
             5.45100000e+04,   1.73690000e+04,   2.23583000e+01,
             6.97500000e+00,   3.10130700e+06,   3.33700000e+03,
             2.91780000e+04,   2.13300000e+03,   2.62833000e+01,
             9.21670000e+00,   1.75930000e+04,   3.10127900e+06,
             6.75000000e+00,   1.15000000e+01,   3.31120000e+04,
             7.79580000e+00,   1.16600000e+03,   6.66000000e+01,
             1.12060000e+04,   8.51000000e+02,   2.65302000e+05,
             1.75970000e+04,   7.73330000e+00,   3.92090000e+05,
             2.34300000e+03,   1.61000000e+01,   3.35950000e+04,
             2.05250000e+01,   5.50000000e+01,   1.73180000e+04,
             3.35000000e+01,   3.06958000e+01,   2.54667000e+01,
             1.75950000e+04,   0.00000000e+00,   2.13100000e+03,
             3.90000000e+01,   2.20250000e+01,   5.00000000e+01,
             1.76100000e+04,   8.40420000e+00,   6.49580000e+00,
             3.54000000e+03,   1.04625000e+01,   1.87875000e+01,
             3.10000000e+01,   3.10131100e+06,   1.35280000e+04,
             2.11740000e+04,   1.13275000e+02,   3.10128300e+06,
             2.70000000e+01,   7.62917000e+01,   1.42080000e+04,
             3.92089000e+05,   9.00000000e+01,   4.34800000e+03,
             7.51000000e+02,   2.11730000e+04,   1.35000000e+01,
             2.95660000e+04,   6.60900000e+03,   3.19210000e+04,
             1.05000000e+01,   1.58500000e+03,   1.42630000e+04,
             1.45000000e+01,   5.25542000e+01,   3.33600000e+03,
             2.02125000e+01,   1.75850000e+04,   8.65000000e+01,
             1.77550000e+04,   7.96500000e+01,   1.72480000e+04,
             1.75820000e+04,   1.77600000e+04,   1.95000000e+01,
             1.75960000e+04,   7.79583000e+01,   2.67300000e+03,
             1.04820000e+04,   7.88500000e+01,   9.10792000e+01,
             2.16300000e+03,   8.85000000e+00,   1.76120000e+04,
             1.51550000e+02,   3.05000000e+01,   2.32500000e+01,
             1.23500000e+01,   2.46600000e+03,   1.10883300e+02,
             1.77580000e+04,   3.38100000e+03,   1.74850000e+04,
             8.31583000e+01,   1.76080000e+04,   1.35290000e+04,
             1.40000000e+01,   1.64866700e+02,   1.34500000e+02,
             2.11720000e+04,   6.23750000e+00,   5.79792000e+01,
             2.85000000e+01,   1.76110000e+04,   3.76710000e+04,
             9.22500000e+00,   3.50000000e+01,   2.16700000e+03,
             3.10131000e+06,   7.07600000e+03,   7.52500000e+01,
             1.74770000e+04,   5.54417000e+01,   7.07700000e+03,
             2.11500000e+02,   4.01250000e+00,   1.77570000e+04,
             1.57417000e+01,   7.72920000e+00,   1.74800000e+03,
             1.20000000e+02,   1.26500000e+01,   1.87500000e+01,
             6.85830000e+00,   3.25000000e+01,   1.30320000e+04,
             7.87500000e+00,   1.44000000e+01,   3.42440000e+04,
             3.92078000e+05,   3.08500000e+03,   5.59000000e+01,
             1.87230000e+04,   8.11250000e+00,   8.18583000e+01,
             1.92583000e+01,   1.99667000e+01,   2.77500000e+01,
             8.91042000e+01,   2.81700000e+03,   1.35310000e+04,
             3.85000000e+01,   2.81600000e+03,   3.10130600e+06,
             7.72500000e+00,   5.41000000e+02,   9.83750000e+00,
             7.04580000e+00,   7.52080000e+00,   1.22875000e+01,
             3.59400000e+03,   9.58750000e+00,   2.97000000e+01,
             1.85090000e+04,   3.10131700e+06,   1.76090000e+04,
             4.53800000e+04,   7.82667000e+01,   6.21200000e+03,
             7.62920000e+00,   4.00100000e+03,   3.10131600e+06,
             1.74730000e+04,   1.76030000e+04,   7.49580000e+00,
             3.40208000e+01,   3.42600000e+04,   9.35000000e+01,
             1.42580000e+04,   1.74830000e+04,   1.77610000e+04,
             4.95000000e+01,   5.73500000e+03,   2.14600000e+03,
             7.82920000e+00,   3.96000000e+01,   1.74000000e+01,
             3.92082000e+05,   3.92087000e+05,   4.88710000e+04,
             7.52000000e+02,   5.14792000e+01,   1.74740000e+04,
             2.05890000e+04,   3.00000000e+01,   4.01250000e+01,
             8.71250000e+00,   1.50000000e+01,   7.92000000e+01,
             3.23500000e+03,   3.90200000e+03,   2.90370000e+04,
             3.30000000e+01,   4.24000000e+01,   1.55500000e+01,
             3.10130500e+06,   6.50000000e+01,   3.23208000e+01,
             7.05420000e+00,   2.31400000e+03,   8.43330000e+00,
             2.55875000e+01,   3.53600000e+03,   1.27500000e+04,
             2.45800000e+04,   9.84170000e+00,   8.13750000e+00,
             1.01708000e+01,   2.11337500e+02,   5.70000000e+01,
             1.34167000e+01,   1.74750000e+04,   7.74170000e+00,
             1.74760000e+04,   1.74820000e+04,   9.48330000e+00,
             7.73750000e+00,   3.10127100e+06,   3.10127200e+06,
             8.36250000e+00,   3.00000000e+00,   6.60700000e+03,
             3.10131200e+06,   1.76000000e+04,   2.59292000e+01,
             8.68330000e+00,   8.51670000e+00,   7.88750000e+00,
             3.10129000e+06,   2.07900000e+03,   7.07500000e+03,
             6.95000000e+00,   8.30000000e+00,   1.77560000e+04,
             3.10128700e+06,   6.43750000e+00,   5.54700000e+03,
             1.75920000e+04,   9.35000000e+00,   1.41083000e+01,
             2.14900000e+03,   1.75900000e+04,   5.00000000e+00,
             9.84580000e+00,   1.05167000e+01,   3.40680000e+04,
             3.92076000e+05]), array([0, 1, 2], dtype=object)]



```python
predictions = []
for train, test in kf:#5次的循环，每次都要建立模型
    # The predictors we're using the train the algorithm.  Note how we only take the rows in the train folds.
    train_predictors = (titanic[predictors].iloc[train,:])#先取出训练数据的上述特征
    # The target we're using to train the algorithm.
    train_target = titanic["Survived"].iloc[train]#取出训练数据的对应的标签
    # Training the algorithm using the predictors and target.
    alg.fit(train_predictors, train_target)#训练回归模型
    # We can now make predictions on the test fold
    test_predictions = alg.predict(titanic[predictors].iloc[test,:])#在已将训练号的模型上应用测试集
    #test_predictions得到的是概率值【0,1】
    predictions.append(test_predictions)#保存测试集样本的模型输出结果
```


```python
print predictions
```

    [array([ 0.10369162,  0.94737356,  0.47769332,  0.92596391,  0.05541592,
            0.17502751,  0.35596294,  0.14257445,  0.54450313,  0.8827522 ,
            0.6737144 ,  0.8186193 ,  0.14393988, -0.10785823,  0.6657462 ,
            0.62994989,  0.19232152,  0.30315549,  0.53681164,  0.62217961,
            0.26180603,  0.26771352,  0.73810184,  0.50954542,  0.59341587,
            0.38433214,  0.13589623,  0.43270197,  0.66131091,  0.09676489,
            0.47712917,  1.00578243,  0.66131091,  0.07776156,  0.51949772,
            0.39833161,  0.13589623,  0.13803285,  0.58508731,  0.67636212,
            0.48364901,  0.76683029,  0.13589621,  0.90319806,  0.71447386,
            0.09587481,  0.14651198,  0.66131091,  0.07886516,  0.61360258,
            0.08452351,  0.13660722,  0.88173542,  0.75501611,  0.30789093,
            0.50954542,  0.82961613,  0.13294274,  0.85102381,  0.01007476,
            0.1713382 ,  0.93675718,  0.38060943,  0.1085342 ,  0.54801295,
            0.08515466,  0.78242179,  0.14979727,  0.48951214,  0.05154832,
            0.27827703,  0.46682317,  0.3439428 ,  0.11919469,  0.07313507,
            0.11448588,  0.09676489,  0.09676488,  0.41919592,  0.57123411,
            0.13220682,  0.09085783,  0.66131091,  0.50954499,  0.85385393,
            0.4679672 ,  0.07220619,  0.08195182,  0.89535738,  0.12039286,
            0.09085789,  0.14402085,  0.37448896,  0.03552444, -0.08635192,
            0.09676488,  0.29400655,  0.5553161 ,  0.73177051,  0.23919776,
            0.58304827,  0.09676489,  0.5286668 ,  0.06722989, -0.0134286 ,
            0.09676489,  0.62439724,  0.09676489,  0.03769494,  0.63279503,
            0.3973119 ,  0.67340851,  0.13220685,  0.60178889,  0.68715628,
            0.1772454 , -0.07601974,  0.26873292,  0.5494167 ,  0.57811618,
            0.28691227,  0.09470575,  0.28718942,  0.76285739,  0.33373598,
            0.20189273,  0.17502753,  0.11973695,  0.57143777, -0.00365399,
            0.10636124,  0.02685096,  0.44217433,  0.75501611,  0.31977459,
            0.37174168,  1.00454009,  0.42786654,  0.16764878,  0.57164138,
            0.5777273 ,  0.61849024,  0.46099216,  0.22819052,  0.36222549,
            0.30432666,  0.10267189,  0.59354927,  0.20849353,  0.22045756,
            0.16725104,  1.00275433, -0.06610054, -0.02155641,  0.08674184,
            0.38992637,  0.73219485,  0.07013768,  0.09676486, -0.17589747,
           -0.01997334,  0.71728617,  0.10857888,  0.1617418 ,  0.11996548,
            0.1645453 ,  0.97360206,  0.36520932,  0.50889248,  0.09676305,
            0.31461467,  0.18050753,  0.69179574,  0.13811408,  0.38328107,
            0.10509357, -0.01100758,  0.90434282,  0.2913415 ]), array([ 0.04789862,  0.14798354,  0.32533278, -0.03227049,  0.33304098,
            0.71543415,  0.49143226,  0.61156575,  0.3909289 ,  0.02170238,
            0.04789839,  0.77506271,  0.34652182,  0.60061249,  0.37440421,
            0.93380578,  0.85103894,  0.15935591, -0.00109606,  0.66475283,
            0.82235873,  0.09519436, -0.35741338,  0.05972243,  0.02381513,
            0.15421143,  0.74078091,  0.01835931,  0.13909884,  0.73569686,
            0.45256953,  0.02839818,  0.75693256,  0.13004915,  0.28148979,
            0.10616905,  0.95798521,  0.51605991,  0.15735849,  1.00526115,
            0.28107582,  0.15470406,  0.2992258 , -0.04078166,  0.09519441,
            0.3791242 ,  0.13053985,  0.3465003 ,  0.13891718,  0.35243382,
            0.42750783,  0.90225732,  0.08928241,  0.1100417 ,  0.49677444,
            0.31609994,  0.60039882,  0.14553452,  0.8889754 ,  0.34652189,
            0.26370794,  0.57948503,  0.61156575,  0.28698622,  0.1306666 ,
            0.11545117,  0.35462683,  0.61832734,  0.79531386,  0.37151489,
            0.08641449,  0.09519443,  0.52796998,  0.29042485,  0.03008649,
            0.49669011,  0.59971504,  0.9963178 ,  0.98500411,  0.95492882,
            0.65512387,  0.15935591,  0.00320153,  0.28283406,  0.42048968,
            0.66475283,  0.24551515, -0.06013233,  0.05974356,  0.8054354 ,
            0.95492868,  0.49143281,  0.11293065,  0.70833208,  0.45627087,
            0.66475283,  0.73672141,  0.50008729,  0.29331418,  0.05723749,
            0.49242032, -0.05938819,  0.09519441,  0.16613839,  0.14809697,
            0.49143296,  0.09771512,  0.08337036,  0.13066642,  0.21054576,
            0.70022485,  1.00865234,  1.02892989,  0.27803582,  0.62423931,
            0.11884242,  0.52300084,  0.15387919,  1.0703066 ,  0.49143282,
            0.88481286,  0.66475283,  0.05298174,  0.14840266,  0.86287223,
            0.09512272,  0.57129464,  1.02890815,  1.04023867,  0.26028546,
            1.01657746,  1.05255697,  0.95409936,  0.74382507,  0.09519441,
            0.13753032,  0.61241534,  0.76917149,  0.1396017 ,  0.95204499,
            0.89125416,  0.13004921,  0.10110641,  0.85104823,  0.767473  ,
           -0.35741338,  0.98109742, -0.09990163,  0.7514147 ,  0.51614568,
            1.08633131,  0.55837866,  0.38797284,  0.41827853,  0.05976443,
            0.94313018,  0.09519441,  0.43233291,  0.95205143, -0.00530964,
            0.39092863,  0.38031621,  0.83386557,  0.2933138 ,  0.3110498 ,
            0.24601778,  0.82235873,  0.72776669,  0.54740423,  0.17518682,
            0.01242635,  0.12475438,  0.49143269,  0.13742194,  0.05974327,
            0.12727518,  0.09519436,  1.01877863]), array([ 0.73124938,  0.7004941 ,  0.7004941 , -0.0817545 ,  0.28045022,
            0.53384599, -0.01338736,  0.1501547 ,  0.088824  ,  0.78021952,
            0.65668163,  0.7004941 ,  1.04177935,  0.48564368,  0.12450458,
            0.15715879,  0.54268025,  0.6337717 ,  0.97813487,  0.6498912 ,
            0.47713967,  0.1947739 ,  0.15715879,  0.93021856,  0.78905575,
            0.0765919 ,  0.89134416,  0.10138162,  0.34336894,  0.03944823,
            0.74364431,  0.18900659,  0.90516866,  0.33870042,  0.14476387,
            0.0236782 ,  1.00952479,  0.60248218,  0.1385664 ,  0.59427675,
            0.17018186,  0.31272387,  0.79322402,  0.03320966,  0.11377654,
            0.61739963, -0.00885611,  0.66244883,  0.20569982, -0.04116003,
            0.38034264,  0.14476387,  0.47883501,  0.10138162,  0.18900661,
            0.99136317,  0.2817368 ,  0.00222234,  0.61286913,  0.69970848,
            0.82024145,  0.26934157,  0.68946591,  0.1451941 ,  0.23208903,
            0.09518416,  0.55653868,  0.10702567,  0.10059356,  0.75437201,
            0.84900088,  0.18900659,  0.06756697,  0.46209118,  0.57401724,
            0.66753711,  0.16955385,  0.2868946 ,  0.98653213,  0.54343885,
            0.68787453,  0.13021096,  0.26271343,  0.63122571,  0.15096129,
            0.08112231,  0.79322401,  0.10138162,  0.57587183,  0.86870722,
            0.4249064 ,  0.704041  ,  0.31335197,  0.15755058,  0.06252963,
            0.49350871,  0.33690378,  0.10131696,  0.13899664,  0.23278503,
            0.93472641,  0.65656866,  0.18900659,  0.33814191,  0.06419684,
            0.3443391 ,  0.15778723,  0.10131698, -0.03197966,  0.2817368 ,
            0.2885622 ,  0.18900659,  0.73038022,  0.10138164,  0.03940697,
            0.68763048,  0.86801166,  0.65005387,  0.46209059,  0.20569982,
            0.05633247,  0.13856641,  0.75652449, -0.01013148,  0.2817368 ,
           -0.03504512,  0.39595788,  0.48564286,  0.47883501,  0.89134328,
            0.31997969,  0.08856083,  0.16193618,  0.06252963,  0.07337697,
            0.29475958,  0.23900802,  0.14371947,  0.14519395,  0.81740423,
            0.10123881,  0.91835931,  0.12617148,  0.1695537 ,  0.74387635,
            0.70049411,  0.55709193,  1.04794688,  0.52861844,  0.7272792 ,
            0.46209118,  0.10128971,  0.11377543,  0.18280912,  0.02999474,
            0.41210988,  0.81700084,  0.12617148,  0.3443392 ,  0.75525093,
            0.18900621,  0.7047923 ,  0.07659177,  0.96118223,  0.1385664 ,
            0.14519412,  0.90075244,  0.14519412,  0.11153829,  0.65655192,
            0.46168936,  0.03320952,  0.21754183,  0.89802746,  0.14519412,
            0.15703591,  0.62172409,  0.60047419]), array([  9.55358258e-01,   3.03477416e-01,   9.74212977e-01,
             9.08190305e-02,   1.06539654e+00,   9.29419989e-01,
             5.73710219e-01,   5.60793386e-01,   1.74278390e-01,
             2.64420894e-01,   1.80767516e-01,   7.86928944e-01,
             2.97473230e-01,   2.62046720e-02,   3.48339081e-01,
             5.68996455e-01,   2.58503087e-01,   1.81746966e-01,
             1.75033562e-01,   6.58260783e-01,   1.93684339e-01,
             8.06324389e-01,   4.58438734e-01,   8.38595994e-01,
             5.15910179e-01,   1.81746968e-01,   1.33181452e-02,
             2.52044879e-01,   8.42809550e-02,   6.12972014e-01,
             1.19727390e-02,   1.48944887e-01,   6.91493402e-01,
             1.36283064e-01,   6.49854762e-02,   3.24464099e-02,
             6.76635581e-01,   3.61312211e-01,   7.10438110e-01,
             1.67976928e-01,   1.48944777e-01,   7.41985532e-01,
             8.18985951e-01,   6.13041471e-01,   6.49855738e-02,
             7.67788818e-01,   8.84059385e-01,   8.41258469e-02,
             4.07066848e-01,   1.36283039e-01,   1.04576579e+00,
             1.29334944e-01,   2.19742029e-01,   1.29569636e-01,
             9.07653258e-02,   4.56103249e-02,   7.80490079e-01,
            -3.19557064e-02,   7.49658988e-01,   1.41502524e-01,
             6.82936269e-03,   7.80735696e-01,  -4.48074697e-02,
             1.36283064e-01,   2.70883912e-01,   7.22314669e-01,
             9.08191406e-02,   4.13270228e-01,  -1.25155225e-02,
             4.13525491e-01,  -1.27809327e-02,   7.79023080e-02,
             4.19728843e-01,   8.52203516e-01,   8.64167887e-01,
             5.94586893e-01,   3.91022440e-02,   6.58505366e-01,
             1.81746968e-01,   4.56102240e-02,   7.93857090e-01,
             1.97463578e-02,   5.80439001e-01,   8.51482795e-01,
             2.64961761e-01,   9.08087444e-02,   2.70919616e-01,
             1.55628076e-01,   1.36028055e-01,   1.36027918e-01,
             2.00142659e-01,   1.55678650e-01,   9.87169692e-01,
             1.03735973e-01,   1.81746968e-01,   7.74327884e-02,
            -5.77244199e-02,   4.32900674e-01,   4.13270935e-01,
             6.25642890e-01,   7.80736030e-01,   6.49855738e-02,
             1.99815367e-01,   6.33602535e-01,   3.88863884e-02,
             1.42486472e-01,   1.01296821e+00,   6.70851804e-01,
             9.08183301e-02,   7.56711058e-01,   2.77340878e-01,
             1.48944887e-01,   2.77898600e-01,   9.08067487e-02,
             6.51763908e-01,   9.08191406e-02,   8.64930464e-01,
             1.36028046e-01,   7.10438109e-01,   7.75022290e-01,
             1.73765417e-01,   9.08191406e-02,   6.52282139e-01,
             2.84336968e-01,   3.04201348e-01,   1.67026867e-01,
             5.87820687e-02,   2.90560599e-01,   3.91518170e-02,
             9.05539537e-02,   1.22098087e-01,   2.71420136e-01,
             9.08191426e-02,  -6.11593793e-03,   8.90028595e-01,
             6.70912424e-01,   3.41750453e-01,  -1.96182735e-02,
             2.32669638e-01,   2.52045104e-01,   1.55403305e-01,
             1.13423595e-01,   6.84094413e-01,   5.88328435e-01,
             4.26381876e-01,   7.10438104e-01,   4.64900235e-01,
             1.42486449e-01,  -3.92408524e-02,   1.30529558e-02,
             3.04137124e-01,  -6.88358449e-03,   1.48944849e-01,
             1.55403305e-01,   1.04552840e+00,   3.41962121e-01,
             8.39586533e-01,   9.08183301e-02,   1.55658313e-01,
             2.06601172e-01,   9.70428879e-02,  -1.25155225e-02,
             7.10438110e-01,   2.90784080e-01,   4.01316741e-04,
             9.99781424e-01,   3.67770610e-01,   7.49168688e-01,
             2.01122217e-01,   5.18033584e-02,   1.81002091e-01,
             6.70942944e-01,   3.22561679e-01,   9.80710048e-01,
             1.03960754e-01,   1.01296813e+00,   4.13270493e-01,
             2.32169127e-01]), array([ 0.09639295,  0.15952532,  0.14772938,  0.96005539,  0.79456364,
            0.18254067,  0.07585834,  0.87810913,  0.12559466,  0.25193094,
            0.16979261,  0.4366712 ,  0.14259575,  0.68195684,  0.68923777,
            0.26573194,  0.63468145,  0.96550534,  0.2293057 ,  0.28273264,
            0.30840105,  0.30840105,  0.09895986,  0.40045718,  0.46875909,
            0.10152657,  0.10152657,  0.46393923,  0.39046875,  0.9339985 ,
            0.08965927,  0.08612555,  0.19174265,  0.10650428,  0.77916274,
            0.47774037,  0.16713962,  0.85597428,  0.19020546,  0.07585836,
            0.1271948 ,  0.60583306,  0.36637199,  0.10152657,  0.33406926,
            0.0707247 ,  0.94496901,  0.10152666,  0.07824793,  0.18310273,
            0.84864376,  0.16313032,  0.82016126,  0.50444636,  0.67640366,
            0.15013879,  0.08099199,  0.12206118, -0.00114635,  0.64055416,
            0.14203356,  0.5507692 ,  0.15286303,  0.18254056,  0.7262977 ,
            0.18254056,  0.86937291,  0.72573546,  0.99470493,  0.45880559,
            0.02069426,  0.16038682,  0.1169275 ,  0.65956024,  0.13134437,
            0.15924256,  0.41228672,  0.18254056,  0.34433675,  0.30051769,
            0.50469244,  0.11692751,  0.22626271,  0.86282982,  0.59282286,
            0.13176627,  0.54129332,  0.25193094,  0.71781283,  0.47028769,
            0.25935814,  0.1066602 ,  0.08612563,  0.40746871,  0.65956024,
            0.22626271,  0.91256654,  0.11179386,  0.0457412 ,  0.24679726,
            0.54303353,  0.08869246,  0.46393881,  0.67735102,  0.25120443,
            0.02462091,  0.04820369,  0.79076644,  0.10666023,  0.41260235,
            0.5890961 ,  0.08113241,  0.18254055,  0.10152725,  0.41335443,
            0.18254056,  0.79609318,  0.68306626,  0.36555067,  0.14203356,
            0.1271948 ,  0.15286304,  0.89825834,  0.1374621 ,  0.10152657,
            0.08099267,  0.50444623,  0.1860547 ,  0.34433643,  1.00087616,
            0.10866485,  0.15799669,  0.02973315, -0.20617952,  0.10609804,
            0.25847171,  0.97874227,  0.04660361, -0.13462115,  0.68960676,
            1.00822491,  0.67488987,  0.63529887,  0.82670296,  0.34586533,
            0.59648135,  0.14203356, -0.03001475,  0.28626632,  0.86796347,
            0.30051769,  0.3032674 ,  0.71755899,  0.8026986 ,  0.44878437,
            0.10152659,  0.16807073,  0.11179386,  0.81643409,  0.43827065,
            0.00398731,  0.79758222,  0.71546817,  0.14259577,  0.14772939,
            0.10152657,  0.84314071,  0.78056976,  0.07585834,  0.6390257 ,
            0.28321004,  0.12242165,  0.51146102,  0.28786647,  1.01683926,
            0.52739147,  0.51471352,  0.16200598])]



```python
import numpy as np

# The predictions are in three separate numpy arrays.  Concatenate them into one.  
# We concatenate them on axis 0, as they only have one axis.
predictions = np.concatenate(predictions, axis=0)

# Map predictions to outcomes (only possible outcomes are 1 and 0)
predictions[predictions > .5] = 1
predictions[predictions <=.5] = 0
accuracy = sum(predictions[predictions == titanic["Survived"]]) / len(predictions)
print accuracy
```

    0.786756453423


    /home/zzpp220/anaconda2/lib/python2.7/site-packages/ipykernel/__main__.py:10: FutureWarning: in the future, boolean array-likes will be handled as a boolean array index



```python
help(cross_validation.cross_val_score)
```

    Help on function cross_val_score in module sklearn.cross_validation:
    
    cross_val_score(estimator, X, y=None, scoring=None, cv=None, n_jobs=1, verbose=0, fit_params=None, pre_dispatch='2*n_jobs')
        Evaluate a score by cross-validation
        
        .. deprecated:: 0.18
            This module will be removed in 0.20.
            Use :func:`sklearn.model_selection.cross_val_score` instead.
        
        Read more in the :ref:`User Guide <cross_validation>`.
        
        Parameters
        ----------
        estimator : estimator object implementing 'fit'
            The object to use to fit the data.
        
        X : array-like
            The data to fit. Can be, for example a list, or an array at least 2d.
        
        y : array-like, optional, default: None
            The target variable to try to predict in the case of
            supervised learning.
        
        scoring : string, callable or None, optional, default: None
            A string (see model evaluation documentation) or
            a scorer callable object / function with signature
            ``scorer(estimator, X, y)``.
        
        cv : int, cross-validation generator or an iterable, optional
            Determines the cross-validation splitting strategy.
            Possible inputs for cv are:
        
            - None, to use the default 3-fold cross-validation,
            - integer, to specify the number of folds.
            - An object to be used as a cross-validation generator.
            - An iterable yielding train/test splits.
        
            For integer/None inputs, if the estimator is a classifier and ``y`` is
            either binary or multiclass, :class:`StratifiedKFold` is used. In all
            other cases, :class:`KFold` is used.
        
            Refer :ref:`User Guide <cross_validation>` for the various
            cross-validation strategies that can be used here.
        
        n_jobs : integer, optional
            The number of CPUs to use to do the computation. -1 means
            'all CPUs'.
        
        verbose : integer, optional
            The verbosity level.
        
        fit_params : dict, optional
            Parameters to pass to the fit method of the estimator.
        
        pre_dispatch : int, or string, optional
            Controls the number of jobs that get dispatched during parallel
            execution. Reducing this number can be useful to avoid an
            explosion of memory consumption when more jobs get dispatched
            than CPUs can process. This parameter can be:
        
                - None, in which case all the jobs are immediately
                  created and spawned. Use this for lightweight and
                  fast-running jobs, to avoid delays due to on-demand
                  spawning of the jobs
        
                - An int, giving the exact number of total jobs that are
                  spawned
        
                - A string, giving an expression as a function of n_jobs,
                  as in '2*n_jobs'
        
        Returns
        -------
        scores : array of float, shape=(len(list(cv)),)
            Array of scores of the estimator for each run of the cross validation.
        
        Examples
        --------
        >>> from sklearn import datasets, linear_model
        >>> from sklearn.cross_validation import cross_val_score
        >>> diabetes = datasets.load_diabetes()
        >>> X = diabetes.data[:150]
        >>> y = diabetes.target[:150]
        >>> lasso = linear_model.Lasso()
        >>> print(cross_val_score(lasso, X, y))  # doctest:  +ELLIPSIS
        [ 0.33150734  0.08022311  0.03531764]
        
        See Also
        ---------
        :func:`sklearn.metrics.make_scorer`:
            Make a scorer from a performance metric or loss function.
    



```python
from sklearn import cross_validation
from sklearn.linear_model import LogisticRegression
# Initialize our algorithm
alg = LogisticRegression(random_state=1)
# Compute the accuracy score for all the cross validation folds.  (much simpler than what we did before!)
scores = cross_validation.cross_val_score(alg, titanic[predictors], titanic["Survived"], cv=3)#将模型、训练样本特征、训练样本标签传入
# Take the mean of the scores (because we have one for each fold)
#得到的score有3个，因为分了3个文件夹。
print(scores.mean())
help(cross_validation.cross_val_score)
```

    0.616161616162
    Help on function cross_val_score in module sklearn.cross_validation:
    
    cross_val_score(estimator, X, y=None, scoring=None, cv=None, n_jobs=1, verbose=0, fit_params=None, pre_dispatch='2*n_jobs')
        Evaluate a score by cross-validation
        
        .. deprecated:: 0.18
            This module will be removed in 0.20.
            Use :func:`sklearn.model_selection.cross_val_score` instead.
        
        Read more in the :ref:`User Guide <cross_validation>`.
        
        Parameters
        ----------
        estimator : estimator object implementing 'fit'
            The object to use to fit the data.
        
        X : array-like
            The data to fit. Can be, for example a list, or an array at least 2d.
        
        y : array-like, optional, default: None
            The target variable to try to predict in the case of
            supervised learning.
        
        scoring : string, callable or None, optional, default: None
            A string (see model evaluation documentation) or
            a scorer callable object / function with signature
            ``scorer(estimator, X, y)``.
        
        cv : int, cross-validation generator or an iterable, optional
            Determines the cross-validation splitting strategy.
            Possible inputs for cv are:
        
            - None, to use the default 3-fold cross-validation,
            - integer, to specify the number of folds.
            - An object to be used as a cross-validation generator.
            - An iterable yielding train/test splits.
        
            For integer/None inputs, if the estimator is a classifier and ``y`` is
            either binary or multiclass, :class:`StratifiedKFold` is used. In all
            other cases, :class:`KFold` is used.
        
            Refer :ref:`User Guide <cross_validation>` for the various
            cross-validation strategies that can be used here.
        
        n_jobs : integer, optional
            The number of CPUs to use to do the computation. -1 means
            'all CPUs'.
        
        verbose : integer, optional
            The verbosity level.
        
        fit_params : dict, optional
            Parameters to pass to the fit method of the estimator.
        
        pre_dispatch : int, or string, optional
            Controls the number of jobs that get dispatched during parallel
            execution. Reducing this number can be useful to avoid an
            explosion of memory consumption when more jobs get dispatched
            than CPUs can process. This parameter can be:
        
                - None, in which case all the jobs are immediately
                  created and spawned. Use this for lightweight and
                  fast-running jobs, to avoid delays due to on-demand
                  spawning of the jobs
        
                - An int, giving the exact number of total jobs that are
                  spawned
        
                - A string, giving an expression as a function of n_jobs,
                  as in '2*n_jobs'
        
        Returns
        -------
        scores : array of float, shape=(len(list(cv)),)
            Array of scores of the estimator for each run of the cross validation.
        
        Examples
        --------
        >>> from sklearn import datasets, linear_model
        >>> from sklearn.cross_validation import cross_val_score
        >>> diabetes = datasets.load_diabetes()
        >>> X = diabetes.data[:150]
        >>> y = diabetes.target[:150]
        >>> lasso = linear_model.Lasso()
        >>> print(cross_val_score(lasso, X, y))  # doctest:  +ELLIPSIS
        [ 0.33150734  0.08022311  0.03531764]
        
        See Also
        ---------
        :func:`sklearn.metrics.make_scorer`:
            Make a scorer from a performance metric or loss function.
    



```python
titanic_test = pandas.read_csv("test.csv")
titanic_test["Age"] = titanic_test["Age"].fillna(titanic["Age"].median())
titanic_test["Fare"] = titanic_test["Fare"].fillna(titanic_test["Fare"].median())
titanic_test.loc[titanic_test["Sex"] == "male", "Sex"] = 0 
titanic_test.loc[titanic_test["Sex"] == "female", "Sex"] = 1
titanic_test["Embarked"] = titanic_test["Embarked"].fillna("S")

titanic_test.loc[titanic_test["Embarked"] == "S", "Embarked"] = 0
titanic_test.loc[titanic_test["Embarked"] == "C", "Embarked"] = 1
titanic_test.loc[titanic_test["Embarked"] == "Q", "Embarked"] = 2
```


    ---------------------------------------------------------------------------

    IOError                                   Traceback (most recent call last)

    <ipython-input-63-0a222fc477a4> in <module>()
    ----> 1 titanic_test = pandas.read_csv("test.csv")
          2 titanic_test["Age"] = titanic_test["Age"].fillna(titanic["Age"].median())
          3 titanic_test["Fare"] = titanic_test["Fare"].fillna(titanic_test["Fare"].median())
          4 titanic_test.loc[titanic_test["Sex"] == "male", "Sex"] = 0
          5 titanic_test.loc[titanic_test["Sex"] == "female", "Sex"] = 1


    /home/zzpp220/anaconda2/lib/python2.7/site-packages/pandas/io/parsers.pyc in parser_f(filepath_or_buffer, sep, delimiter, header, names, index_col, usecols, squeeze, prefix, mangle_dupe_cols, dtype, engine, converters, true_values, false_values, skipinitialspace, skiprows, skipfooter, nrows, na_values, keep_default_na, na_filter, verbose, skip_blank_lines, parse_dates, infer_datetime_format, keep_date_col, date_parser, dayfirst, iterator, chunksize, compression, thousands, decimal, lineterminator, quotechar, quoting, escapechar, comment, encoding, dialect, tupleize_cols, error_bad_lines, warn_bad_lines, skip_footer, doublequote, delim_whitespace, as_recarray, compact_ints, use_unsigned, low_memory, buffer_lines, memory_map, float_precision)
        560                     skip_blank_lines=skip_blank_lines)
        561 
    --> 562         return _read(filepath_or_buffer, kwds)
        563 
        564     parser_f.__name__ = name


    /home/zzpp220/anaconda2/lib/python2.7/site-packages/pandas/io/parsers.pyc in _read(filepath_or_buffer, kwds)
        313 
        314     # Create the parser.
    --> 315     parser = TextFileReader(filepath_or_buffer, **kwds)
        316 
        317     if (nrows is not None) and (chunksize is not None):


    /home/zzpp220/anaconda2/lib/python2.7/site-packages/pandas/io/parsers.pyc in __init__(self, f, engine, **kwds)
        643             self.options['has_index_names'] = kwds['has_index_names']
        644 
    --> 645         self._make_engine(self.engine)
        646 
        647     def close(self):


    /home/zzpp220/anaconda2/lib/python2.7/site-packages/pandas/io/parsers.pyc in _make_engine(self, engine)
        797     def _make_engine(self, engine='c'):
        798         if engine == 'c':
    --> 799             self._engine = CParserWrapper(self.f, **self.options)
        800         else:
        801             if engine == 'python':


    /home/zzpp220/anaconda2/lib/python2.7/site-packages/pandas/io/parsers.pyc in __init__(self, src, **kwds)
       1211         kwds['allow_leading_cols'] = self.index_col is not False
       1212 
    -> 1213         self._reader = _parser.TextReader(src, **kwds)
       1214 
       1215         # XXX


    pandas/parser.pyx in pandas.parser.TextReader.__cinit__ (pandas/parser.c:3427)()


    pandas/parser.pyx in pandas.parser.TextReader._setup_parser_source (pandas/parser.c:6861)()


    IOError: File test.csv does not exist



```python
from sklearn import cross_validation
from sklearn.ensemble import RandomForestClassifier

predictors = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]

# Initialize our algorithm with the default paramters
# n_estimators is the number of trees we want to make
# min_samples_split is the minimum number of rows we need to make a split#每棵树结点分裂的终止条件
# min_samples_leaf is the minimum number of samples we can have at the place where a tree branch ends (the bottom points of the tree)
alg = RandomForestClassifier(random_state=1, n_estimators=10, min_samples_split=2, min_samples_leaf=1)
# Compute the accuracy score for all the cross validation folds.  (much simpler than what we did before!)
kf = cross_validation.KFold(titanic.shape[0], n_folds=3, random_state=1)
scores = cross_validation.cross_val_score(alg, titanic[predictors], titanic["Survived"], cv=kf)

# Take the mean of the scores (because we have one for each fold)
print(scores.mean())#结果不太好的一个原因，默认参数----调参
```

    0.777777777778



```python
#增加决策树的个数同时决策树更深一些，分裂的终止条件更松一些
alg = RandomForestClassifier(random_state=1, n_estimators=100, min_samples_split=4, min_samples_leaf=2)
# Compute the accuracy score for all the cross validation folds.  (much simpler than what we did before!)
kf = cross_validation.KFold(titanic.shape[0], 5, random_state=1)
scores = cross_validation.cross_val_score(alg, titanic[predictors], titanic["Survived"], cv=kf)

# Take the mean of the scores (because we have one for each fold)
print(scores.mean())
```

    0.81933337518



```python
"""
数据挖掘旺旺要建立一个特征工程，从直接的特征中进行提取、组合 挖掘出新的特征  特征选择 进行预测
"""
```


```python
# Generating a familysize column
titanic["FamilySize"] = titanic["SibSp"] + titanic["Parch"]#由原有特征产生新特征--家庭人数--人多力量大，好逃生？

# The .apply method generates a new series
titanic["NameLength"] = titanic["Name"].apply(lambda x: len(x))#对该列的每一个值应用函数
```


```python
import re

# A function to get the title from a name.
def get_title(name):
    # Use a regular expression to search for a title.  Titles always consist of capital and lowercase letters, and end with a period.
    title_search = re.search(' ([A-Za-z]+)\.', name)
    # If the title exists, extract and return it.
    if title_search:
        return title_search.group(1)
    return ""

# Get all the titles and print how often each one occurs.
titles = titanic["Name"].apply(get_title)
print(pandas.value_counts(titles))
#数值转化 每个人的前缀
# Map each title to an integer.  Some titles are very rare, and are compressed into the same codes as other titles.
title_mapping = {"Mr": 1, "Miss": 2, "Mrs": 3, "Master": 4, "Dr": 5, "Rev": 6, "Major": 7, "Col": 7, "Mlle": 8, "Mme": 8, "Don": 9, "Lady": 10, "Countess": 10, "Jonkheer": 10, "Sir": 9, "Capt": 7, "Ms": 2}
for k,v in title_mapping.items():
    titles[titles == k] = v

# Verify that we converted everything.
print(pandas.value_counts(titles))

# Add in the title column.
titanic["Title"] = titles
```

    Mr          517
    Miss        182
    Mrs         125
    Master       40
    Dr            7
    Rev           6
    Col           2
    Major         2
    Mlle          2
    Countess      1
    Ms            1
    Lady          1
    Jonkheer      1
    Don           1
    Mme           1
    Capt          1
    Sir           1
    Name: Name, dtype: int64
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
    Name: Name, dtype: int64



```python
import numpy as np
from sklearn.feature_selection import SelectKBest, f_classif#
import matplotlib.pyplot as plt
#查看每个特征的重要程度，对特征进行衡量,哪些特征有用、哪些没用。很实用的方法。feature_importance,从而选择出重要成程度更高的特征
predictors = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked", "FamilySize", "Title", "NameLength"]

# Perform feature selection
selector = SelectKBest(f_classif, k=5)
selector.fit(titanic[predictors], titanic["Survived"])

# Get the raw p-values for each feature, and transform from p-values into scores
scores = -np.log10(selector.pvalues_)

# Plot the scores.  See how "Pclass", "Sex", "Title", and "Fare" are the best?
plt.bar(range(len(predictors)), scores)
plt.xticks(range(len(predictors)), predictors, rotation='vertical')
plt.show()

# from the chart,Pick only the four best features.
predictors = ["Pclass", "Sex", "Fare", "Title"]

alg = RandomForestClassifier(random_state=1, n_estimators=50, min_samples_split=8, min_samples_leaf=4)
```


```python
print scores
```


```python
from sklearn.ensemble import GradientBoostingClassifier
import numpy as np
#进行一个算法的集成，最后的结果是多个分类方法的平均值
# The algorithms we want to ensemble.
# We're using the more linear predictors for the logistic regression, and everything with the gradient boosting classifier.
algorithms = [
    [GradientBoostingClassifier(random_state=1, n_estimators=25, max_depth=3), ["Pclass", "Sex", "Age", "Fare", "Embarked", "FamilySize", "Title",]],
    [LogisticRegression(random_state=1), ["Pclass", "Sex", "Fare", "FamilySize", "Title", "Age", "Embarked"]]
]

# Initialize the cross validation folds
kf = KFold(titanic.shape[0], n_folds=3, random_state=1)

predictions = []
for train, test in kf:
    train_target = titanic["Survived"].iloc[train]
    full_test_predictions = []
    # Make predictions for each algorithm on each fold
    for alg, predictors in algorithms:
        # Fit the algorithm on the training data.
        alg.fit(titanic[predictors].iloc[train,:], train_target)
        # Select and predict on the test fold.  
        # The .astype(float) is necessary to convert the dataframe to all floats and avoid an sklearn error.
        test_predictions = alg.predict_proba(titanic[predictors].iloc[test,:].astype(float))[:,1]
        full_test_predictions.append(test_predictions)
    # Use a simple ensembling scheme -- just average the predictions to get the final classification.
    test_predictions = (full_test_predictions[0] + full_test_predictions[1]) / 2
    # Any value over .5 is assumed to be a 1 prediction, and below .5 is a 0 prediction.
    test_predictions[test_predictions <= .5] = 0
    test_predictions[test_predictions > .5] = 1
    predictions.append(test_predictions)

# Put all the predictions together into one array.
predictions = np.concatenate(predictions, axis=0)

# Compute accuracy by comparing to the training data.
accuracy = sum(predictions[predictions == titanic["Survived"]]) / len(predictions)
print(accuracy)

```


```python
titles = titanic_test["Name"].apply(get_title)
# We're adding the Dona title to the mapping, because it's in the test set, but not the training set
title_mapping = {"Mr": 1, "Miss": 2, "Mrs": 3, "Master": 4, "Dr": 5, "Rev": 6, "Major": 7, "Col": 7, "Mlle": 8, "Mme": 8, "Don": 9, "Lady": 10, "Countess": 10, "Jonkheer": 10, "Sir": 9, "Capt": 7, "Ms": 2, "Dona": 10}
for k,v in title_mapping.items():
    titles[titles == k] = v
titanic_test["Title"] = titles
# Check the counts of each unique title.
print(pandas.value_counts(titanic_test["Title"]))

# Now, we add the family size column.
titanic_test["FamilySize"] = titanic_test["SibSp"] + titanic_test["Parch"]


```

    1     240
    2      79
    3      72
    4      21
    7       2
    6       2
    10      1
    5       1
    Name: Title, dtype: int64



```python
predictors = ["Pclass", "Sex", "Age", "Fare", "Embarked", "FamilySize", "Title"]

algorithms = [
    [GradientBoostingClassifier(random_state=1, n_estimators=25, max_depth=3), predictors],
    [LogisticRegression(random_state=1), ["Pclass", "Sex", "Fare", "FamilySize", "Title", "Age", "Embarked"]]
]

full_predictions = []
for alg, predictors in algorithms:
    # Fit the algorithm using the full training data.
    alg.fit(titanic[predictors], titanic["Survived"])
    # Predict using the test dataset.  We have to convert all the columns to floats to avoid an error.
    predictions = alg.predict_proba(titanic_test[predictors].astype(float))[:,1]
    full_predictions.append(predictions)

# The gradient boosting classifier generates better predictions, so we weight it higher.，取不同分类器的权重
predictions = (full_predictions[0] * 3 + full_predictions[1]) / 4
predictions
```




    array([ 0.11682912,  0.47835566,  0.12614824,  0.13098157,  0.52105874,
            0.1435209 ,  0.64085331,  0.18003152,  0.67801353,  0.12111118,
            0.12105181,  0.20902118,  0.91068381,  0.1089127 ,  0.89142102,
            0.87713474,  0.16349859,  0.13907791,  0.54103238,  0.55661006,
            0.22420875,  0.5372079 ,  0.90572223,  0.38890588,  0.88384752,
            0.10357315,  0.90909441,  0.13746454,  0.31046249,  0.12665718,
            0.11663767,  0.18274855,  0.55220994,  0.49648575,  0.42415297,
            0.14191051,  0.50973638,  0.52452209,  0.13270506,  0.28366691,
            0.11145281,  0.46618807,  0.09996501,  0.83420617,  0.89959119,
            0.14983417,  0.31593419,  0.13789623,  0.89104185,  0.54189565,
            0.35666363,  0.17718135,  0.8307195 ,  0.87995521,  0.1755907 ,
            0.13741805,  0.10667279,  0.1234385 ,  0.12099736,  0.91285169,
            0.13099159,  0.15341948,  0.12993967,  0.66573206,  0.66343836,
            0.87272604,  0.67238712,  0.288265  ,  0.35236574,  0.85565507,
            0.6622414 ,  0.12701993,  0.55390065,  0.36740462,  0.91110312,
            0.41201902,  0.13014004,  0.83671279,  0.15614414,  0.6622414 ,
            0.68129213,  0.20605719,  0.20382623,  0.12105181,  0.18486634,
            0.13130212,  0.65680539,  0.53029858,  0.65489631,  0.79881212,
            0.53764546,  0.12104028,  0.8913725 ,  0.13014004,  0.28406245,
            0.12345367,  0.86792484,  0.14666337,  0.58599461,  0.12260781,
            0.90433464,  0.14730817,  0.13789623,  0.12262433,  0.62257491,
            0.13155874,  0.14607753,  0.13789623,  0.13020336,  0.17473033,
            0.14286392,  0.65490316,  0.89528117,  0.67146758,  0.88346017,
            0.13992078,  0.11805064,  0.69612515,  0.36668939,  0.86241698,
            0.87649291,  0.12609327,  0.90276371,  0.12099027,  0.13789623,
            0.56971935,  0.12608181,  0.63733743,  0.13339996,  0.13340574,
            0.12723637,  0.51609607,  0.23921874,  0.10791695,  0.09896737,
            0.12431124,  0.13346495,  0.16214099,  0.52029433,  0.12232635,
            0.20712059,  0.90529649,  0.19747926,  0.16153716,  0.42927593,
            0.10487176,  0.33642492,  0.13518414,  0.46618807,  0.34478758,
            0.91431377,  0.13214999,  0.10690998,  0.48983645,  0.11274825,
            0.12427868,  0.9107016 ,  0.57991631,  0.42927593,  0.51274048,
            0.65489239,  0.57884522,  0.82113381,  0.12096648,  0.28979611,
            0.58587108,  0.30130471,  0.14606803,  0.9025041 ,  0.52257377,
            0.12101884,  0.13299498,  0.12418534,  0.13207486,  0.1319655 ,
            0.8729358 ,  0.87633414,  0.29670328,  0.83389526,  0.85558679,
            0.15614414,  0.33352246,  0.90219082,  0.13789623,  0.91718918,
            0.13603003,  0.85482389,  0.12241402,  0.14217314,  0.13560687,
            0.1348803 ,  0.25547183,  0.49950989,  0.12729496,  0.71980831,
            0.10795469,  0.85516508,  0.58990449,  0.16645668,  0.53980354,
            0.64867969,  0.66329187,  0.60981573,  0.87333314,  0.16322638,
            0.25696649,  0.63083524,  0.16482591,  0.88984707,  0.12346408,
            0.12849653,  0.12097124,  0.24675029,  0.80199995,  0.41248342,
            0.29768148,  0.65492663,  0.21860346,  0.90027407,  0.13014004,
            0.8137002 ,  0.13611142,  0.84275393,  0.12700828,  0.87789288,
            0.59807994,  0.12518087,  0.65489631,  0.11487493,  0.1441311 ,
            0.25075165,  0.89266286,  0.11622683,  0.1379133 ,  0.34224639,
            0.12796773,  0.19365861,  0.14018901,  0.80948189,  0.89790832,
            0.87598967,  0.82598174,  0.33036559,  0.12105101,  0.33258156,
            0.28710745,  0.8790295 ,  0.16058987,  0.86241698,  0.59133092,
            0.74586492,  0.15434326,  0.39647431,  0.13354268,  0.12701864,
            0.12101884,  0.13789623,  0.13014004,  0.83005787,  0.12700585,
            0.10894954,  0.12701508,  0.85003763,  0.64929875,  0.16619539,
            0.12105181,  0.21821016,  0.12101884,  0.50973638,  0.14016481,
            0.34495861,  0.13789623,  0.91564   ,  0.6332826 ,  0.13207439,
            0.85713531,  0.15861636,  0.12500116,  0.14267175,  0.16811853,
            0.52045075,  0.66231856,  0.65489631,  0.64136782,  0.71198852,
            0.10601085,  0.12099027,  0.3627808 ,  0.13207486,  0.13014004,
            0.33304456,  0.59319589,  0.13207486,  0.50584352,  0.12081676,
            0.12263655,  0.77903176,  0.12665718,  0.33024483,  0.12028976,
            0.11813957,  0.17547887,  0.1216941 ,  0.13347145,  0.65489631,
            0.82133626,  0.33497525,  0.67696014,  0.20916505,  0.42575111,
            0.13912869,  0.13799529,  0.12102122,  0.61904744,  0.90111957,
            0.67393647,  0.23919457,  0.17328806,  0.12182854,  0.18522951,
            0.12262433,  0.13491478,  0.16214099,  0.45541306,  0.90601333,
            0.12509883,  0.86563776,  0.34598576,  0.14469719,  0.17034218,
            0.82147627,  0.32823572,  0.13207439,  0.64322911,  0.12183262,
            0.25111398,  0.15333425,  0.09370087,  0.20950803,  0.35411806,
            0.17507148,  0.118123  ,  0.1469565 ,  0.91556464,  0.33657652,
            0.618368  ,  0.16214099,  0.62462682,  0.1654289 ,  0.85157883,
            0.89603825,  0.16322638,  0.24472808,  0.16066609,  0.70031025,
            0.15642457,  0.85672648,  0.12105022,  0.13789623,  0.57255235,
            0.10418822,  0.87672475,  0.86918839,  0.13098157,  0.91914163,
            0.15715004,  0.1313025 ,  0.53322127,  0.89562968,  0.17356053,
            0.15319843,  0.90891499,  0.16307942,  0.13130575,  0.87654859,
            0.90969185,  0.48853359,  0.17002326,  0.19866966,  0.13510974,
            0.13789623,  0.14010265,  0.54133852,  0.5949924 ,  0.15905635,
            0.83276875,  0.12430276,  0.12019388,  0.14606637,  0.18789784,
            0.38579307,  0.87750065,  0.56459193,  0.12807839,  0.10318132,
            0.91169572,  0.14231524,  0.88773179,  0.12607946,  0.12971145,
            0.90753797,  0.12635163,  0.90891637,  0.35988713,  0.30442425,
            0.18966803,  0.1501521 ,  0.26822399,  0.65488945,  0.64585313,
            0.65489631,  0.90711865,  0.56933478,  0.13014004,  0.86010063,
            0.10126674,  0.13014004,  0.41850311])




```python

```


```python

```
