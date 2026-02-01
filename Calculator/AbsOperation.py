from abc import ABC, abstractmethod

class AbsOperation(ABC):
    @abstractmethod
    def operate(self):
        pass