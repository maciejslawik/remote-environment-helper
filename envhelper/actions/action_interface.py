from abc import abstractmethod


class ActionInterface:

    @abstractmethod
    def run(self):
        pass
