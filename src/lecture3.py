
import numpy 
import numpy.linalg
import matplotlib 
matplotlib.use("GTK3Agg")
import matplotlib.pyplot as plt 
from sklearn.decomposition import PCA 
from sklearn import preprocessing 
from apgl.util.Latex import Latex 

numpy.set_printoptions(suppress=True, precision=3)

#Let's create a simple example for PCA 


mean = numpy.zeros(2)
cov = numpy.array([[1, 2], [2, 1]])
X = numpy.random.multivariate_normal(mean, cov, 100) 

print(X)
fig = plt.figure(1, figsize=(10, 10))
plt.scatter(X[:, 0], X[:, 1]) 
plt.plot([0, 1], [0, 1], color='k', linestyle='-', linewidth=2)
plt.plot([0, -1], [0, 1], color='r', linestyle='-', linewidth=2)
plt.xlim([-4, 4])
plt.ylim([-4, 4])
plt.savefig("../Lecture3/Figures/PCA.eps")
plt.show()

