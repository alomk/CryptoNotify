import requests
from notifications import notify
import time
import json
import sys
import datetime

def update():
    global old
    global new
    old = copy.deepcopy(new)
    time.sleep(delay)
    new = json.loads(requests.get('https://bittrex.com/api/v1.1/public/getorderbook?market=%s&type=buy'%(coin)))
    calculateChange()
    evaluate()
    print "Finished with interval " + str(datetime.datetime.now())
    update()
    

def calculateChange():
    return None

def evaluate():
    return None

delay = 30
coin = sys.argv[1]
old = json.loads(requests.get('https://bittrex.com/api/v1.1/public/getorderbook?market=%s&type=buy'%(coin)))
time.sleep(delay)
new = json.loads(requests.get('https://bittrex.com/api/v1.1/public/getorderbook?market=%s&type=buy'%(coin)))

calculateChange()
evaluate()
print "Finished with interval " + str(datetime.datetime.now())
update()
