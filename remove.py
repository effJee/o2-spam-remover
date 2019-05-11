import imapclient
import pprint
import email
import re
from os import environ

print("something")
# s = imapclient.SocketTimeout(connect=500, read=500)
imapObj = imapclient.IMAPClient('poczta.o2.pl', ssl=True, timeout=5)
print("after")
imapObj.login(environ.get('USERNAME_KEY'), environ.get('PASSWORD_KEY'))
#
# # pprint.pprint(imapObj.list_folders())
# imapObj.select_folder('INBOX', readonly=False)
# # UIDs = imapObj.search(['ALL'])
# # print(UIDs)
#
# messages = imapObj.search('UNSEEN')
# adresReg = re.compile(r"(<o2@o2.pl>|<no-response@o2.pl>)")
#
# for uid, message_data in imapObj.fetch(messages, 'RFC822').items():
#     email_message = email.message_from_bytes(message_data[b'RFC822'])
#     if re.search(adresReg, email_message.get('From')) is not None:
#         imapObj.delete_messages(uid)
#
# imapObj.logout()
