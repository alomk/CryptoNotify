import sys
import pickle
import time

volumes = pickle.load(open(sys.argv[1],'r'))
times = pickle.load(open(sys.argv[1] + "_times",'r'))

coin = str(sys.argv[2].upper())

deriv = []

for i in range(1,len(times)):
    deriv.append((volumes[coin][i]-volumes[coin][i-1])/(times[i]-times[i-1]))

for i in volumes[coin]:
    print i
for i in deriv:
    print i
