from abc import abstractmethod


class AccessDataReaderInterface:

    @abstractmethod
    def read_access_data(self):
        pass
