import numpy
import matplotlib 
matplotlib.use("GTK3Agg")
import matplotlib.pyplot as plt 

"""
Code to generate figures for lecture 1. 
"""


numpy.random.seed(21)

outputDir = "/home/charanpal/Documents/Postdoc/Documents/stats-notes/Lecture1/Figures/"
outputFilename = outputDir + "DiscreteHist.eps" 

X = numpy.random.randint(1, 7, 100)
plt.figure(0)
n, bins, patches = plt.hist(X, bins=6, rwidth=0.5)
plt.ylabel("Frequency")
plt.xlabel("x")
plt.savefig(outputFilename)

print(numpy.bincount(X))
print(n, bins, patches)




#Continuous histogram 
outputFilename = outputDir + "ContinuousHist.eps" 

X = numpy.random.randn(100)
plt.figure(1)
n, bins, patches = plt.hist(X, bins=10)
plt.ylabel("Frequency")
plt.xlabel("x")
plt.savefig(outputFilename)

print(n, bins, patches)

outputFilename = outputDir + "ContinuousCDF.eps" 
plt.figure(2)
plt.plot(bins[1:], numpy.cumsum(n)/numpy.sum(n))
plt.ylabel("F(x)")
plt.xlabel("x")
plt.savefig(outputFilename)


#Box plot 
spread= numpy.random.rand(50) * 100
center = numpy.ones(25) * 50
flier_high = numpy.random.rand(10) * 100 + 100
flier_low = numpy.random.rand(10) * -100
data = numpy.concatenate((spread, center, flier_high, flier_low), 0)

outputFilename = outputDir + "BoxPlot.eps" 
plt.figure(3)
plt.boxplot(data)
plt.savefig(outputFilename)

#Scatter plot 
outputFilename = outputDir + "ScatterPlot.eps" 
x = numpy.random.rand(50) 
y = x**2 + numpy.random.randn(50)*0.2 
plt.figure(4)
plt.scatter(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.savefig(outputFilename)

#QQ plot 
outputFilename = outputDir + "QQPlot.eps" 
x = numpy.random.randn(1000) 
y = numpy.random.randn(1000)*0.2 
x = numpy.sort(x)
y = numpy.sort(y)
plt.figure(5)
plt.scatter(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.savefig(outputFilename)



plt.show()
