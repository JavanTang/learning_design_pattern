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

class FactoryStrategy:

    def get_strategy(self, strate):
        if strate == 'Insightface':
            return Insightface()
        elif strate == 'Dlib':
            return Dlib()
        else:
            return None
        

if __name__ == '__main__':

    factory_strategy = FactoryStrategy()

    camera = Camera(factory_strategy.get_strategy('Insightface'))
    camera.execute()
    camera.set_strategy(factory_strategy.get_strategy('Dlib'))
    camera.execute()
