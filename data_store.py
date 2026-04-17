from abc import ABC, abstractmethod
class data_store(ABC):
    @abstractmethod
    def get_user_data(self, username):
        pass
    