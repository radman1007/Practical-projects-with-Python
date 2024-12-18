import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as plt

data=pd.read_csv('heart.csv')
data.info()
data_corr=data.corr()
data_corr
sns.heatmap(data=data_corr,annot=True)
feature_value=np.array(data_corr['output'])
for i in range(len(feature_value)):
    if feature_value[i]<0:
        feature_value[i]=-feature_value[i]
feature_value
features_corr=pd.DataFrame(feature_value,index=data_corr['output'].index,columns=['correalation'])
feature_sorted=features_corr.sort_values(by=['correalation'],ascending=False)
feature_sorted
feature_selected=feature_sorted.index
feature_selected
clean_data=data[feature_selected]

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
X=clean_data.iloc[:,1:]
Y=clean_data['output']
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.25,random_state=0)
print(x_train.shape,y_train.shape,x_test.shape,y_test.shape)
x_test

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.transform(x_test)
dt=DecisionTreeClassifier(criterion='entropy',max_depth=6)
dt.fit(x_train,y_train)
y_pred=dt.predict(x_test)

from sklearn.metrics import confusion_matrix
conf_mat=confusion_matrix(y_test,y_pred)
print(conf_mat)
accuracy=dt.score(x_test,y_test)
print("\nThe accuracy of decisiontreelassifier on Heart disease prediction dataset is "+str(round(accuracy*100,2))+"%")
len(x_test[1])
input_data = {
    'age': 60,
    'sex': 1,
    'cp': 3,
    'trtbps':143,
    'chol': 233,
    'fbs': 1,
    'restecg': 0,
    'thalachh': 150,
    'exng': 0,
    'oldpeak': 2.4,
    'slp': 0,
    'caa': 0,
    'thall': 1
}
input_data = pd.DataFrame([input_data])
input_data = sc.fit_transform(input_data)
prediction = dt.predict(input_data)

if prediction[0] == 1:
    print("The Patient Is Likely To Have Heart Disease")
else:
    print("The Patient Is Okay")