
import numpy 
from sklearn import preprocessing 
from apgl.util.Latex import Latex 

numpy.set_printoptions(suppress=True, precision=3)

dataDir = "../data/"
dataFilename = dataDir + "pima-indians-diabetes.data" 

Xy = numpy.loadtxt(dataFilename, delimiter=",") 

X = Xy[:, 0:-1]
y = Xy[:, -1]

X = preprocessing.scale(X)

print(X)

n = X.shape[0]
d = X.shape[1]

correlations = numpy.zeros((X.shape[1], X.shape[1]))

for i in range(d): 
	for j in range(d): 
		correlations[i, j] = numpy.corrcoef(X[:, i], X[:, j])[0,1]
		
print(Latex.array2DToRows(correlations))
	
