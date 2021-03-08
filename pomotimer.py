import threading
import time

class pomotimer(threading.Timer):
    def __init__(self, timeout, callback):
        self.timer = threading.Timer(timeout, callback)

        self.start_time = None
        self.pause_time = None

        # Used for creating a new timer upon renewal
        self.timeout = timeout
        self.callback = callback
    
    def start(self):
        self.start_time = time.time()
        self.timer.start()
        
    def pause(self):
        self.pause_time = time.time()
        self.timer.cancel()
        return self.remaining()
        
    def resume(self):
        self.timeout = self.remaining()
        self.timer = threading.Timer(self.timeout, self.callback)
        self.start_time = time.time()
        self.timer.start()
        return self.remaining() 
    
    def remaining(self):
        if self.pause_time is None or self.pause_time < self.start_time:
            return self.timeout - (time.time() - self.start_time)
        return self.timeout - (self.pause_time - self.start_time)
    
    def cancel(self):
        self.timer.cancel()
