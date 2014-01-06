import scipy.stats 
import matplotlib 
matplotlib.use("GTK3Agg")
import matplotlib.pyplot as plt 
import numpy 

outputDir = "../Lecture6/Figures/"

#Now let's try the strong law of large numbers by simulating dice roll
numSamples = 5000
x = numpy.random.randint(1, 7, numSamples)
y = numpy.zeros(numSamples)

for i in range(numSamples): 
	y[i] = numpy.mean(x[0:i])

plt.figure(10)
plt.plot(numpy.arange(numSamples-1), y[1:])
plt.ylabel("value")
plt.xlabel("X_n")
plt.savefig(outputDir + "LawLargeNumbers" + ".eps") 

	
#Let's try to demonstrate the central limit theorem 
a = 1 
b = 2 
numBins = 100 

def plotCLT(n, plotInd, showPdf=False): 
    m = 1000000
    y = numpy.zeros(m)
    
    for i in range(m):
        x = numpy.random.rand(n)*(b-a)+a 
        y[i] = numpy.sum(x)

    mu = (a+b)/2.0
    sigmaSq = ((b-a)**2)/12.0

    y = (y - n*mu)/numpy.sqrt(sigmaSq*n)

    plt.figure(plotInd)
    plt.hist(y, normed=True, bins=numBins, stacked=True)
    plt.xlabel("y") 
    plt.ylabel("p(y)") 
    plt.title("n=" + str(n))
    
    if showPdf:
        x = numpy.linspace(-3, 3, 100)
        h = plt.plot(x, scipy.stats.norm().pdf(x))
    
    plt.savefig(outputDir + "clt" + str(plotInd) + ".eps") 
    
plotCLT(1, 0)
plotCLT(2, 1, True) 
plotCLT(3, 2, True) 
plotCLT(4, 3, True) 

plt.show() 


 

