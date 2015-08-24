from fileManager import FileManager
from painter import Painter

class Calendar(object):
    def __init__(self, filename):
        self.filename = filename
    
    def __enter__(self):
        self.fManager = FileManager(self.filename)
        self.events = self.fManager.readEvents()
        self.painter = Painter()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fManager.rewriteEvents(self.events)
        
    def draw(self):
        self.painter.draw(self.events)
        