#!/usr/bin/env python
import imaplib
import os
import email
import re

username=os.getenv('IMAP_USERNAME')
password=os.getenv('IMAP_PASSWORD')
domain_name=os.getenv('DOMAIN_NAME')

# Login
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(username, password)

# Select the All Mail folder
mail.select("[Gmail]/All Mail")

# List all emails to domain_name addresses
result, search_results = mail.uid('search', None, '(HEADER To "@%s")' % domain_name)

whitelist = []
regex = re.compile("([a-z0-9\-\+\.]+?@%s)" % domain_name, re.IGNORECASE|re.MULTILINE)

for line in search_results:
    uids = line.split(" ")
    for uid in uids:
        result, data = mail.uid('fetch', uid, '(RFC822)')
        raw_email = data[0][1]

        message = email.message_from_string(raw_email)
        address = message['To']

        try:
            r = regex.search(address)
        except:
            print "- Could not parse raw address %s" % address
            continue

        if r and r.groups():
            address = r.group(1).lower()
        else:
            print "- Could not parse To: %s" % address
            continue

        if address not in whitelist:
            print address
            whitelist.append(address)
