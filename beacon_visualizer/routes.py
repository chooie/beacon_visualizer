from flask import request, render_template
from beacon_visualizer import app
from beacon_visualizer.beacons import beacons

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', beacons=beacons.beacons)
    elif request.method == 'POST':
        return 'Log Beacon!'
