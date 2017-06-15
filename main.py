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
    for i in range(len(old['result'])):
        for j in range(len(old['result'])):
            if(old['result'][i]['MarketName'] == new['result'][i]['MarketName']):
                try:
                    change[old['result'][i]['MarketName']] = {'Name':old['result'][i]['MarketName'].encode('ASCII'),'Percent Change':((new['result'][i]['Last'] - old['result'][i]['Last'])/(old['result'][i]['Last'])) * 100,'Volume': new['result'][i]['BaseVolume'],'Price': new['result'][i]['Last'],'Time':str(datetime.datetime.now())}
                except:
                    #print 'Exception ' + str(old['result'][i]['MarketName'])
                    continue

def evaluate():
    for i in change:
        if((change[i]['Percent Change'] <= -5 and change[i]['Volume'] >= 200 and change[i]['Name'][0] != 'E')):
            notify(change[i])
      
def notify(coin):
    msg = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (fromaddr, ", ".join(toaddr), coin['Name'] + ' at ' + coin['Time'], coin)

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    print 'Sending... ' + coin['Name'] + ' at ' + coin['Time']
    server.login(username,password)
    server.sendmail(fromaddr,toaddr,msg)
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
fromaddr = login.readline().replace("\n", "")
toaddr = [login.readline().replace("\n", "")]

calculateChange()
evaluate()
print "Finished with interval " + str(datetime.datetime.now())
update()
