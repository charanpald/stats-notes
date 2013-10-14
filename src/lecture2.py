
import numpy 
import matplotlib.pyplot as plt 
from sklearn.decomposition import PCA 
from sklearn import preprocessing 
from apgl.util.Latex import Latex 

numpy.set_printoptions(suppress=True, precision=3)

dataDir = "../data/"
dataFilename = dataDir + "data_banknote_authentication.txt"

Xy = numpy.loadtxt(dataFilename, delimiter=",")

X = Xy[:, 0:-1]
y = Xy[:, -1]



X = preprocessing.scale(X)

print(X.mean(0), X.std(0))
print(numpy.unique(y))

k = 0

posLabel = 1

plt.figure(k)
plt.scatter(X[y!=posLabel, 0], X[y!=posLabel, 1], c="b") 
plt.scatter(X[y==posLabel, 0], X[y==posLabel, 1], c="r") 
plt.xlabel("X_(1)")
plt.ylabel("X_(2)")
plt.savefig("../Lecture2/Figures/X12.eps")
k += 1

plt.figure(k)
plt.scatter(X[y!=posLabel, 0], X[y!=posLabel, 2], c="b") 
plt.scatter(X[y==posLabel, 0], X[y==posLabel, 2], c="r") 
plt.xlabel("X_(1)")
plt.ylabel("X_(3)")
plt.savefig("../Lecture2/Figures/X13.eps")
k += 1

plt.figure(k)
plt.scatter(X[y!=posLabel, 0], X[y!=posLabel, 3], c="b") 
plt.scatter(X[y==posLabel, 0], X[y==posLabel, 3], c="r") 
plt.xlabel("X_(1)")
plt.ylabel("X_(3)")
plt.savefig("../Lecture2/Figures/X14.eps")
k += 1

plt.figure(k)
plt.scatter(X[y!=posLabel, 1], X[y!=posLabel, 2], c="b") 
plt.scatter(X[y==posLabel, 1], X[y==posLabel, 2], c="r") 
plt.xlabel("X_(2)")
plt.ylabel("X_(3)")
plt.savefig("../Lecture2/Figures/X23.eps")
k += 1

plt.figure(k)
plt.scatter(X[y!=posLabel, 1], X[y!=posLabel, 3], c="b") 
plt.scatter(X[y==posLabel, 1], X[y==posLabel, 3], c="r") 
plt.xlabel("X_(2)")
plt.ylabel("X_(3)")
plt.savefig("../Lecture2/Figures/X24.eps")
k += 1

plt.figure(k)
plt.scatter(X[y!=posLabel, 2], X[y!=posLabel, 3], c="b") 
plt.scatter(X[y==posLabel, 2], X[y==posLabel, 3], c="r") 
plt.xlabel("X_(2)")
plt.ylabel("X_(3)")
plt.savefig("../Lecture2/Figures/X34.eps")
k += 1

n = X.shape[0]
d = X.shape[1]

correlations = numpy.zeros((X.shape[1], X.shape[1]))

for i in range(d): 
	for j in range(d): 
		correlations[i, j] = numpy.corrcoef(X[:, i], X[:, j])[0,1]
		
print(Latex.array2DToRows(correlations))

#Run PCA and find first directions 
pca = PCA(n_components=3)
newX = pca.fit_transform(X)

print(pca.explained_variance_ratio_) 
print(pca.components_[0, :])

plt.figure(k)
plt.scatter(newX[y!=1, 0], newX[y!=1, 1], c="b") 
plt.scatter(newX[y==1, 0], newX[y==1, 1], c="r") 
plt.xlabel("Z_(1)")
plt.ylabel("Z_(2)")
plt.savefig("../Lecture2/Figures/Z12.eps")
k += 1

plt.figure(k)
plt.scatter(newX[y!=1, 0], newX[y!=1, 2], c="b") 
plt.scatter(newX[y==1, 0], newX[y==1, 2], c="r") 
plt.xlabel("Z_(1)")
plt.ylabel("Z_(3)")
plt.savefig("../Lecture2/Figures/Z13.eps")
k += 1

plt.figure(k)
plt.scatter(newX[y!=1, 1], newX[y!=1, 2], c="b") 
plt.scatter(newX[y==1, 1], newX[y==1, 2], c="r") 
plt.xlabel("Z_(2)")
plt.ylabel("Z_(3)")
plt.savefig("../Lecture2/Figures/Z23.eps")
plt.show()
