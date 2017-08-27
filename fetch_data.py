import numpy
import matplotlib
import json
import sys
import time
import requests
import datetime
import pickle

def update():
    global interval
    global volumes
    global times

    data = json.loads(requests.get('https://bittrex.com/api/v1.1/public/getmarketsummaries').text)
    timestamp = str(datetime.datetime.now())

    del volumes
    volumes = {}
    del times
    times = []

    for i in data['result']:
        volumes[i['MarketName']] = [i['BaseVolume']]
    
    times.append(int(time.time()))

    for i in range(144):
        time.sleep(interval)
        data = json.loads(requests.get('https://bittrex.com/api/v1.1/public/getmarketsummaries').text)
        for j in data['result']:
            volumes[j['MarketName']].append(j['BaseVolume'])    
            open('/home/kazi/CryptoNotify/data/%s'%(timestamp), 'w').close()
            outputVol = open('/home/kazi/CryptoNotify/data/%s'%(timestamp),'w')
            pickle.dump(volumes,outputVol)
            #outputVol.write(volumes)
            #outputTime.write(times)
            outputVol.close()
        
        times.append(int(time.time())) 
        open('/home/kazi/CryptoNotify/data/%s_times'%(timestamp), 'w').close()
        outputTime = open('/home/kazi/CryptoNotify/data/%s_times'%(timestamp),'w')
        pickle.dump(times,outputTime)
        outputTime.close()

        print "finished with iteration %i"%(i)
        
    

    update()

volumes = {}
times = []

interval = 600 #in seconds

update()
