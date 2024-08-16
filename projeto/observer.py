from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, mensagem: str):
        pass

class Subject(ABC):
    def __init__(self):
        self._observers = []
    
    def add_observer(self, observer: Observer):
        self._observers.append(observer)
    
    def remove_observer(self, observer: Observer):
        self._observers.remove(observer)
    
    def notify_observers(self, mensagem: str):
        for observer in self._observers:
            observer.update(mensagem)

