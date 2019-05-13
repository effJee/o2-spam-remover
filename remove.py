from os import environ
import imapclient
import pprint
import socket
import email
import re

connected = False
timeouts = 1

while not connected:
    try:
        print("Connecting...")
        imapObj = imapclient.IMAPClient('poczta.o2.pl',port=993, ssl=True, timeout=60)
        print("Connected")
        imapObj.login(environ.get('USERNAME_KEY'), environ.get('PASSWORD_KEY'))
        print("Logged in")
        connected = True
    except socket.timeout:
        print("{}. Timed out".format(timeouts))

# pprint.pprint(imapObj.list_folders())
imapObj.select_folder('INBOX', readonly=False)
# UIDs = imapObj.search(['ALL'])
# print(UIDs)

messages = imapObj.search('UNSEEN')
adresReg = re.compile(r"(<o2@o2.pl>|<no-response@o2.pl>)")

for uid, message_data in imapObj.fetch(messages, 'RFC822').items():
    email_message = email.message_from_bytes(message_data[b'RFC822'])
    if re.search(adresReg, email_message.get('From')) is not None:
        imapObj.delete_messages(uid)
        print("Deleted")

imapObj.logout()
print("Logged out")
