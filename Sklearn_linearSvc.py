import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm 
from sklearn.linear_model import LinearRegression
from matplotlib import style
style.use("ggplot")
from sklearn.svm import SVC


y = [55382.7,57923.1,61257.5,65717.6,71628.7,76946.6,83236.3,86095.2,84376.4]
X = [[1],[2],[3],[4],[5],[6],[7],[8],[9]]

clf = LinearRegression()
clf.fit(X, y) 
print(clf.predict([10]))
print(clf.score(X,y))

