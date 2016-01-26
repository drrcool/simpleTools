#This just quickly does some calculations for the prices of masks for MMIRS
from numpy import math

price_file = 'mask_costs'
f = open(price_file)

prices = []
for line in f.readlines():
    if line[0] != '#':
         prices.append(float(line.strip("")))

N = len(prices)
mean = sum(prices) / N
variance = 1.0/(N-1) * sum([(price - mean)**2 for price in prices])
std_dev = math.sqrt(variance)

print("%s +/- %s" % (mean, std_dev))
