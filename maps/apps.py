#coding "utf-8"

from flask import Flask, render_template
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

app = Flask(__name__, template_folder=".")
GoogleMaps(app)

@app.route("/")
def mapview():
    sndmap = Map(
            identifier="sndmap",

            lat=0.2933469,
            lng=101.7068294,
            markers={'http://maps.google.com/mapfiles/ms/icons/green-dot.png':[(0.2933469, 101.7068294)],
                             'http://maps.google.com/mapfiles/ms/icons/blue-dot.png':[(0.2933469, 101.7068294)]},
            style="width:1350px;height:600px;"
            )
    return render_template('example.html', sndmap=sndmap)

if __name__ == "__main__":
    app.run(debug=True)
