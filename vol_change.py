import requests
import json
import sys
import time
import datetime
import smtplib
import copy

def update():
    global old
    global new
    old = copy.deepcopy(new)
    time.sleep(delay)
    new = json.loads(requests.get('https://bittrex.com/api/v1.1/public/getmarketsummaries').text)
    calculateChange()
    evaluate()
    print "Finished with interval " + str(datetime.datetime.now())
    update()

def calculateChange():
    global change
    del change
    change = {}
    for i in range(len(new['result'])):
        for j in range(len(new['result'])):
            try:
                if(old['result'][i]['MarketName'] == new['result'][i]['MarketName']):
                    try:
                        change[old['result'][i]['MarketName']] = {'Name':old['result'][i]['MarketName'].encode('ASCII'),'Change':((new['result'][i]['BaseVolume'] - old['result'][i]['BaseVolume'])),'Volume': new['result'][i]['BaseVolume'],'Price': new['result'][i]['Last'],'Time':str(datetime.datetime.now())}
                    except:
                        #print 'Exception ' + str(old['result'][i]['MarketName'])
                        continue
            except:
                print str(len(new['result'])) + ' is new length'
                print str(len(old['result'])) + ' is old length'
                print "Caught index out of bounds"
                return


def evaluate():
    for i in change:
        if((change[i]['Change'] >= 30 and change[i]['Name'][0] == 'B' and change[i]['Volume'] >= 100)):
            notifyIncrease(change[i])
        elif(change[i]['Change'] <= -30 and change[i]['Name'][0] == 'B' and change[i]['Volume'] >= 100):
            notifyDecrease(change[i])
      
def notifyIncrease(coin):
    msg = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (username.replace("\n",""), ", ".join([username.replace("\n","")]), coin['Name'] + ' increasing volume at ' + coin['Time'], coin)

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    print 'Sending... ' + coin['Name'] + ' at ' + coin['Time']
    server.login(username,password)
    server.sendmail(username,username,msg)
    server.quit
    print 'Sent!'


def notifyDecrease(coin):
    msg = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (username.replace("\n",""), ", ".join([username.replace("\n","")]), coin['Name'] + ' decreasing volume at ' + coin['Time'], coin)

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    print 'Sending... ' + coin['Name'] + ' at ' + coin['Time']
    server.login(username,password)
    server.sendmail(username,username,msg)
    server.quit
    print 'Sent!'


delay = 900
change = {}
old = json.loads(requests.get('https://bittrex.com/api/v1.1/public/getmarketsummaries').text)
time.sleep(delay)
new = json.loads(requests.get('https://bittrex.com/api/v1.1/public/getmarketsummaries').text)

login = open('login.conf','r')
username = login.readline()
password = login.readline()


calculateChange()
evaluate()
print "Finished with interval " + str(datetime.datetime.now())
update()
