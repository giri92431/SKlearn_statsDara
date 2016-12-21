import matplotlib.pyplot as plt 
import numpy 
import sklearn 
from sklearn import datasets 
from sklearn import svm

digits = datasets.load_digits()


clf = svm.SVC(gamma =0.1, C =100)

x,y =digits.data[:-10],digits.target[:-10]

clf.fit(x,y)

print ('predication :',clf.predict(digits.data[-3]))

plt.imshow(digits.images[-3],cmap =plt.cm.gray_r ,interpolation="nearest")

plt.show()