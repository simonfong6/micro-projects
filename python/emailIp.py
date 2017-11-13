#emailIp.py

import netifaces
import time
text = open("text.txt", "w+")
text.write("IPPPP")
text.close()


interfaces = netifaces.interfaces()
for i in interfaces:
    if i == 'lo':
        continue
    iface = netifaces.ifaddresses(i).get(netifaces.AF_INET)
    if iface != None:
        for j in iface:
            msg = j['addr']
            print msg

import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("simonfong6@gmail.com", "!1BeerCoke")

server.sendmail("simonfong@gmail.com", "scf001@ucsd.edu", msg)
server.quit()
