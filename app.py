import time, threading, functools

from flask import Flask, request, render_template
from flask_script import Manager, Server

app = Flask(__name__)

beacons = ["beacon1", "beacon2", "beacon3","beacon4"]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', beacons=beacons)
    elif request.method == 'POST':
        return 'Log Beacon!'

def clear_beacons():
    print 'Clearing beacons!'
    # Todo: Clear Beacons

def call_after_delay(func, time_delay_in_seconds):
    threading.Timer(time_delay_in_seconds, func).start()

def call_repeatedly(func, time_interval_in_seconds):
    call_after_delay(clear_beacons, time_interval_in_seconds)
    call_after_delay(functools.partial(call_repeatedly, func,
                                       time_interval_in_seconds),
                     time_interval_in_seconds)

def _run_on_start():
    call_repeatedly(clear_beacons, 1)

class CustomServer(Server):
    def __call__(self, app, *args, **kwargs):
        _run_on_start()
        #Hint: Here you could manipulate app
        return Server.__call__(self, app, *args, **kwargs)

manager = Manager(app)

# Remeber to add the command to your Manager instance
manager.add_command('runserver', CustomServer())

if __name__ == "__main__":
    manager.run()
