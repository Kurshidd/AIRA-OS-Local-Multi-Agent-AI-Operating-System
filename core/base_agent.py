from abc import ABC, abstractmethod


class BaseAgent(ABC):

    def __init__(self, name, model):
        self.name = name
        self.model = model

    @abstractmethod
    def run(self, task, context=None):
        """
        Every agent must implement this.
        """
        pass

    def __str__(self):
        return self.name