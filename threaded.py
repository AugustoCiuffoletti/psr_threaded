#!/usr/bin/python 
import socket 
import thread

port = raw_input('Su quale porta apri il servizio?\n> ') 
queuelen = 5 
buflen = 80
# Una funzione definisce il servizio
def servizio(client):
    data = client.recv(buflen) 
    if data: 
        client.send(data)
    print ('Stringa scambiata: '+data)
    client.close()
    print ('Servizio concluso')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind(('',int(port))) 
s.listen(queuelen)
try:
    while 1:
        (client, (remhost, remport))=s.accept()
        print ('Servizio attivo con '+remhost)
        thread.start_new_thread(servizio,(client,))
except KeyboardInterrupt:
    print('\n*** Interruzione!')
