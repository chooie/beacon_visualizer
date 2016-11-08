from flask import request, render_template
from beacon_visualizer import app

beacons = ["beacon1", "beacon2", "beacon3","beacon4"]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', beacons=beacons)
    elif request.method == 'POST':
        return 'Log Beacon!'
