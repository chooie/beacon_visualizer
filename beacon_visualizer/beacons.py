import threading

class Beacons():
    def __init__(self, beacons, lock):
        self.beacons = beacons
        self.lock = lock

    def get_beacons(self):
        return self.beacons;

    def add_beacon(self, beacon):
        with self.lock:
            self.beacons.append(beacon)

    def clear_beacons(self):
        with self.lock:
            self.beacons = []

beacons = Beacons(["beacon1", "beacon2", "beacon3","beacon4"],
                  threading.RLock())
