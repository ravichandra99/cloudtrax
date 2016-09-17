#NCompass-Cloudtrax

#Description

node_mac 	MAC address of the Access Point reporting the presence data. 

mac 	MAC address of the end client device for which presence data is being reported.

count 	Number of times the specific end client device was seen by the AP, within the time period specified by the “First seen” and “Last seen” timestamps.

min_signal	Lowest RSSI reading on the AP for the specific client within the time period specified by the “First seen” and “Last seen” timestamps.

max_signal	Highest RSSI reading on the AP for the specific client within the time period specified by the “First seen” and “Last seen” timestamps. 

avg_signal 	Average RSSI reading on the AP for the specific client within the time period specified by the “First seen” and “Last seen” timestamps. 

first_seen	Timestamp of the first time this client was seen, during the reporting period

last_seen	Timestamp of the last time this client was seen, during the reporting period

associated	Indication of whether the client is associated to the AP or not.

CloudTrax Presence Reporting Documentation:
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
