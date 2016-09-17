#NCompass-Cloudtrax

#Description

Receives HTTP POST requests from the [CloudTrax Presence Reporting API](https://help.cloudtrax.com/hc/en-us/articles/207985916-CloudTrax-Presence-Reporting-API
) containing JSON data containing ProbeRequests.

Parses JSON and stores each item in ProbeRequests as a row in example.db (SQLite). 

Displays all ProbeRequests received from CloudTrax

CloudTrax usually sends requests every 30 seconds, but there is an option to change the rate.
#Install
```
  git clone https://github.com/f00-/ncompass-cloudtrax.git
  cd ncompass-cloudtrax
  virtualenv env
  source env/bin/activate
  pip install -r requirements.txt
  python app.py
```

  Go to http://127.0.0.1:5000/test to add sample ProbeRequests and go to http://127.0.0.1:5000/ to view them
  
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

#Dependency Documentation

[CloudTrax Presence Reporting API Documentation](https://help.cloudtrax.com/hc/en-us/articles/207985916-CloudTrax-Presence-Reporting-API
)

[Flask Documentation](http://flask.pocoo.org/)

[Flask-SQLAlchemy Documentation](http://flask-sqlalchemy.pocoo.org/2.1/)

[Marshmallow-SQLAlchemy Documentation](https://marshmallow-sqlalchemy.readthedocs.io/en/latest/)

[Heroku Procfile](https://devcenter.heroku.com/articles/procfile)

[Virtualenv Documentation](https://virtualenv.pypa.io/en/stable/)

[pip and requirements.txt](https://pip.readthedocs.io/en/1.1/requirements.html)
