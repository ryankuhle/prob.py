import collections #needed to count numbers in set, for frequency
import matplotlib.pyplot as plt #boxplot, histogram, qq
import scipy.stats as stats #qq

#Initial Data set
x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]

#Frequency
f = collections.Counter(x)
instances = sum(f.values())
print "There are %s total numbers in the data set." % (instances)
for k,v in f.iteritems():
    print "Frequency of number " + str(k) + " is " + str(float(v) / instances)

print "\nCreating: Boxplot.png, Histogram.png, QQ.png\n"
#Boxplot
plt.boxplot(x)
plt.savefig("boxplot.png")

#Histogram
plt.hist(x, histtype='bar')
plt.savefig('histogram.png')

#QQ
plt.figure()
qq = stats.probplot(x, dist="norm", plot=plt)
plt.savefig('qq.png')