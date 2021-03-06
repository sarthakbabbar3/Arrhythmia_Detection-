from sklearn.ensemble import ExtraTreesClassifier
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectFromModel
import pandas as pd
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
import numpy as np


url = "dataset.csv"


dataset = pd.read_csv(url)
dataset=dataset.dropna(axis=1,how='any')

X=dataset

y=np.array([6,10,1,7,14,1,1,1,10,3,1,10,6,1,1,10,1,1,1,1,1,1,1,1,16,14,10,2,2,6,1,1,1,4,1,1,10,1,6,1,1,1,1,1,4,5,1,6,1,1,1,10,16,16,6,1,1,6,1,5,5,1,1,1,1,2,1,6,1,6,16,1,1,1,10,3,2,1,1,1,1,2,4,6,9,2,4,9,9,1,4,1,5,10,1,10,1,1,1,4,1,1,1,6,4,6,1,2,1,1,1,1,1,6,1,16,1,1,1,1,1,1,1,1,1,1,10,1,1,1,1,1,1,10,1,1,10,1,1,1,5,1,1,10,10,10,1,1,10,1,1,1,6,16,1,1,2,1,1,1,1,1,1,1,1,1,1,5,4,1,1,1,10,15,6,1,1,1,2,1,16,1,4,2,4,2,2,14,9,1,1,2,2,1,1,1,16,16,1,2,1,1,1,3,1,1,9,1,10,10,1,2,2,4,1,2,15,3,16,1,1,6,1,10,3,1,16,1,1,1,4,1,1,1,2,1,2,1,1,1,1,1,15,1,2,1,1,4,1,10,4,3,3,1,1,2,3,5,2,1,16,1,1,1,1,10,1,1,1,1,1,6,1,1,2,1,2,10,1,1,1,1,6,10,3,1,1,1,1,1,10,1,10,2,2,2,10,10,1,15,1,6,3,2,1,16,6,2,7,1,1,10,10,1,1,5,1,1,10,5,1,2,2,10,1,10,7,1,2,1,1,16,1,10,1,10,1,1,1,16,10,1,6,10,1,10,1,5,1,1,2,1,10,16,1,3,2,6,2,2,3,16,10,6,1,2,2,2,1,9,1,2,1,5,2,8,1,1,10,16,3,1,1,6,1,16,5,9,1,1,1,1,1,1,9,1,10,3,1,10,14,1,5,1,1,1,1,1,16,4,2,16,1,1,1,1,10,1,1,15,1,1,1,9,1,1,10,1,16,10,6,10,3,1,1,1,1,1,1,1,1,1,10,1,1,1,1,10,2,1,1])

print(X.shape)

clf = ExtraTreesClassifier()
clf = clf.fit(X, y)

print(clf.feature_importances_)  
np.savetxt('treebased.csv',clf.feature_importances_, delimiter=',')

model = SelectFromModel(clf, prefit=True)
X_new = model.transform(X)
print(X_new.shape)               

