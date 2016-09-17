#NCompass-Cloudtrax

#Description

Recieves HTTP POST requests from the CloudTrax Presence Reporting API, with JSON data.

Parses JSON, stores each ProbeRequest as a row in a SQLite database (example.db) with these columns: node mac address, client mac address, count , max/min/average signal, first seen, and last seen

Displays all ProbeRequests

CloudTrax Presence Reporting API Documentation:
https://help.cloudtrax.com/hc/en-us/articles/207985916-CloudTrax-Presence-Reporting-API

#Install
```
  clone repository
  cd repository
  virtualenv env
  source env/bin/activate
  pip install -r requirements.txt
  python app.py
```
#Usage

```
  /
```

Shows table of ProbeRequests

```
  /receive
```

Receives HTTP Post request from Cloudtrax

```
  /test
```

Adds sample ProbeRequests to the database
