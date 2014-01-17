Suckfish
========

Suckfish connects to a Gmail account and extracts a list of unique email addresses
sent to a particular domain name.

Requirements
============
You'll need the following:

* [Python 2.7.3](http://www.python.org/)

Usage
=====
```bash
    # Clone the repo
    git clone git@github.com:taeram/suckfish.git
    cd ./suckfish

    # Start the application, prefixing with the required environment variables
    IMAP_USERNAME="user@gmail.com" IMAP_PASSWORD="secret" DOMAIN_NAME="example.com" python app.py
```

The script will output a unique list of email addresses matching the specified domain name:
```bash
joe@example.com
bob@example.com
jim@example.com
```
