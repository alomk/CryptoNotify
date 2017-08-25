import sys
import pickle
import time

volumes = pickle.load(open(sys.argv[1],'r'))
times = pickle.load(open(sys.argv[1] + "_times",'r'))

coin = str(sys.argv[2].upper())
print volumes
print times
print len(times)

for i in volumes[coin]:
    print i
