import smtplib

def notify(coin, eventCase):
    
    if eventCase==0:
        event = ' decreasing'
    elif eventCase==1:
        event = ' increasing'
    elif eventCase==2:
        event = ' volume decreasing'
    elif eventCase==3:
        event = ' volume increasing'
    else:
        event = ' decreasing'
    
    msg = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (username.replace("\n",""), ", ".join([username.replace("\n","")]), coin['Name'] + event +  ' at ' + coin['Time'], coin)

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    print 'Sending... ' + coin['Name'] + ' at ' + coin['Time']
    server.login(username,password)
    server.sendmail(username,username,msg)
    server.quit
    print 'Sent!'

#def sendImage(img, msg):
    #todo



login = open('login.conf','r')
username = login.readline()
password = login.readline()
