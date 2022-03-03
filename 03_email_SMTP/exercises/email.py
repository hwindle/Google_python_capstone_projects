#!/usr/bin/env python3

from email.message import EmailMessage

message = EmailMessage()
print(message)
message['From'] = sender
message['To'] = recipient
print(message)
#From: me@example.com
#To: you@example.com
body = """Hey there!
...
... I'm learning to send emails using Python!"""
message.set_content(body)

 import os.path
attachment_path = "/tmp/example.png"
attachment_filename = os.path.basename(attachment_path)
import mimetypes
mime_type, _ = mimetypes.guess_type(attachment_path)
print(mime_type)
#image/png
mime_type, mime_subtype = mime_type.split('/', 1)
print(mime_type)
#image
print(mime_subtype)
#png
with open(attachment_path, 'rb') as ap:
    message.add_attachment(ap.read(),
    maintype=mime_type,
    subtype=mime_subtype,
    filename=os.path.basename(attachment_path))
print(message)


import smtplib
mail_server = smtplib.SMTP('localhost')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  (...We deleted a bunch of lines here...)
ConnectionRefusedError: [Errno 61] Connection refused

# Correct way of connecting to an SMTP personal gmail server
mail_server = smtplib.SMTP_SSL('smtp.example.com')
mail_server.set_debuglevel(1)
import getpass
mail_pass = getpass.getpass('Password? ')
#Password?
mail_server.login(sender, mail_pass)
mail_server.send_message(message)
mail_server.quit()
