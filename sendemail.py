import smtplib

from_addr = 'amc12vidal@gmail.com'
to_addr  = 'david@someemail.com'
from_name = 'Andre Vidal'
to_name = 'david'
subject = ''
message = """
From: {} <{}>
To: {} <{}>
Subject: {}

{}
"""
message_to_send = message.format(from_name, from_addr, to_name, to_addr, subject, message)
# Credentials (if needed)
username = ''
password = ''

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.sendmail(from_addr, to_addr, message_to_send)
server.quit()
