import sys
import pickle

volumes = pickle.load(open(sys.argv[1],'r'))
times = pickle.load(open(sys.argv[1] + "_times",'r'))

print volumes
print times
