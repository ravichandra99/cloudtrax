from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import json

# initialize flask as app, sqlalchemy as db & marshmallow as ma
# also set database URI
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)

# sqlalchemy model
class ProbeRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    network_id = db.Column(db.String(120))
    node_mac = db.Column(db.String(120))
    mac = db.Column(db.String(120))
    count = db.Column(db.String(120))
    min_signal = db.Column(db.String(120))
    max_signal = db.Column(db.String(120))
    avg_signal = db.Column(db.String(120))
    first_seen = db.Column(db.String(120))
    last_seen = db.Column(db.String(120))
    associated = db.Column(db.String(120))

    def __init__(self, network_id, node_mac, mac, count, min_signal, max_signal, 
                    avg_signal, first_seen, last_seen, associated):
        self.network_id = network_id
        self.node_mac = node_mac
        self.mac = mac
        self.count = count
        self.min_signal = min_signal
        self.max_signal = max_signal
        self.avg_signal = avg_signal
        self.first_seen = first_seen
        self.last_seen = last_seen
        self.associated = associated

    def __repr__(self):
        return '<Mac %r>' % self.mac

# marshmallow schema
class ProbeRequestSchema(ma.ModelSchema):
    class Meta:
        model = ProbeRequest

# flask routes

# show stored ProbeRequests
@app.route("/")
def show():
    # retrieve all ProbeRequests
    probes = ProbeRequest.query.all()
    return render_template('show.html', probes=probes)

# store ProbeRequests from Cloudtrax
@app.route('/recieve', methods=['POST'])
def recieve():
    # get json that cloudtrax HTTP POST'd to this URL
    json_string = request.get_json(silent=True)
    parsed_json = json.loads(json_string)

    # loop through probe_requests
    for request in parsed_json['probe_requests']:
        # create new ProbeRequest row
        probe = ProbeRequest(parsed_json['network_id'], parsed_json['node_mac'], request['mac'], request['count'], request['min_signal'], request['max_signal'], request['avg_signal'], request['first_seen'], request['last_seen'], request['associated'])
        db.session.add(probe)
        
    # commit db changes
    db.session.commit()

    return render_template('recieve.html', data="success!")

# store sample ProbeRequests
@app.route('/test', methods=['GET', 'POST'])
def test():
    # sample json string
    json_string = '{"network_id":179283,"node_mac":"AC:86:74:61:4F:C0","version":1,"probe_requests": [{"mac":"14:2d:27:29:16:f7","count":26,"min_signal":-74,"max_signal":-64,"avg_signal":-68,"first_seen":1455845796,"last_seen":1455845819,"associated":false},{"mac":"48:5a:3f:37:de:f7","count":10,"min_signal":-37,"max_signal":-26,"avg_signal":-30,"first_seen":1455845791,"last_seen":1455845811,"associated":true},{"mac":"4e:20:5d:18:d0:ab","count":1,"min_signal":-90,"max_signal":-90,"avg_signal":-90,"first_seen":1455845809,"last_seen":1455845809,"associated":false},{"mac":"68:96:7b:c8:8b:e9","count":4,"min_signal":-54,"max_signal":-5,"avg_signal":-27,"first_seen":1455845817,"last_seen":1455845817,"associated":false},{"mac":"80:19:34:b8:bc:1c","count":2,"min_signal":-65,"max_signal":-61,"avg_signal":-63,"first_seen":1455845819,"last_seen":1455845820,"associated":false}]}'
    parsed_json = json.loads(json_string)

    # loop through probe_requests
    for request in parsed_json['probe_requests']:
        # create new ProbeRequest row
        probe = ProbeRequest(parsed_json['network_id'], parsed_json['node_mac'], request['mac'], request['count'], request['min_signal'], request['max_signal'], request['avg_signal'], request['first_seen'], request['last_seen'], request['associated'])

        db.session.add(probe)
    # commit db changes
    db.session.commit()

    #return success
    return render_template('recieve.html', data="success!")

# this code only executes if file is run directly
if __name__ == "__main__":
    # creates database with models
    db.create_all()
    # start flask server
    app.run()
