import imapclient
import config
import pprint
import email
import re

imapObj = imapclient.IMAPClient('poczta.o2.pl', ssl=True)
imapObj.login(config.username, config.password)

# pprint.pprint(imapObj.list_folders())
imapObj.select_folder('INBOX', readonly=True)
# UIDs = imapObj.search(['ALL'])
# print(UIDs)

messages = imapObj.search('UNSEEN')

for uid, message_data in imapObj.fetch(messages, 'RFC822').items():
    email_message = email.message_from_bytes(message_data[b'RFC822'])

    print(email_message.get('From'))
