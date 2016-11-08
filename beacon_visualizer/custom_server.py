from flask_script import Server
from beacon_visualizer.start_up_tasks import _run_on_start

class CustomServer(Server):
    def __call__(self, app, *args, **kwargs):
        _run_on_start()
        # Hint: Here you could manipulate app
        return Server.__call__(self, app, *args, **kwargs)
