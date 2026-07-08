import poplib
from email.message import EmailMessage


server = "192.168.188.128"
user = "ubuntu"
password = "T123456789"

server = poplib.POP3(server)
server.user(user)
server.pass_(password)

msgNum = len(server.list()[1])

for i in range(msgNum):
    for msg in server.retr(i+1)[1]:
        print(msg.decode())