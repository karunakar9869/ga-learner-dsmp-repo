# --------------
# import the libraries
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')

# Code starts here



# Code ends here
df=pd.read_csv(path)
df.head(5)
X=df.iloc[:,0:7]
y=df['insuranceclaim']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=6)









# --------------
import matplotlib.pyplot as plt


# Code starts here



# Code ends here
plt.boxplot(X_train['bmi'])
plt.show()
q_value=X_train['bmi'].quantile(0.95)
q_value
y_train.value_counts()






# --------------
# Code starts here



# Code ends here
relation=relation=X_train.corr()

print(relation)
sns.pairplot(X_train)





# --------------
import seaborn as sns
import matplotlib.pyplot as plt

# Code starts here



# Code ends here
cols=['children','sex','region','smoker']
fig, axes=plt.subplots(2,2,figsize=(20,20))
for i in range (0,2):
    for j in range (0,2):
        col=cols[i*2+j]
        sns.countplot(x=X_train[col], hue=y_train, ax=axes[i,j])








# --------------
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# parameters for grid search
parameters = {'C':[0.1,0.5,1,5]}

# Code starts here



# Code ends here
lr=LogisticRegression(random_state=6)
grid=GridSearchCV(lr,param_grid=parameters)
grid.fit(X_train,y_train)
y_pred=grid.predict(X_test)
accuracy=grid.score(X_test,y_test)
print(accuracy)



























# --------------
from sklearn.metrics import roc_auc_score
from sklearn import metrics

# Code starts here



# Code ends here
score=roc_auc_score(y_test,y_pred)
a=grid.predict_proba(X_test)
y_pred_proba=a[:,1]
fpr,tpr,_ =metrics.roc_curve(y_test,y_pred)
print('fpr-',fpr)
print('tpr-',tpr)
roc_auc=roc_auc_score(y_test,y_pred_proba)
plt.plot(fpr,tpr,label="Logistic model, auc="+str(roc_auc))
plt.show()







