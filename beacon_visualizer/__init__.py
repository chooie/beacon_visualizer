from flask import Flask
from flask_script import Manager
from beacon_visualizer.custom_server import CustomServer

app = Flask(__name__)

import beacon_visualizer.routes

manager = Manager(app)
manager.add_command('runserver', CustomServer())
