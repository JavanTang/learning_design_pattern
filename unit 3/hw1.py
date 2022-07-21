import time

from abc import ABC, abstractmethod

class Strategy(ABC):

    @abstractmethod
    def execute(self):
        pass

class Insightface(Strategy):
    
    def execute(self):
        print("Insightface")
    

class Dlib(Strategy):

    def execute(self):
        print("Dlib")

class Camera:

    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def execute(self):
        for i in range(1):
            time.sleep(1)
            self.strategy.execute()

if __name__ == '__main__':
    camera = Camera(Insightface())
    camera.execute()
    camera.set_strategy(Dlib())
    camera.execute()
