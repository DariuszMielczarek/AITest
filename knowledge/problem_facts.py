import inspect
from abc import ABC, abstractmethod


class ProblemFacts(ABC):
    @abstractmethod
    def get_data(self):
        pass

    def list_constructor_attributes(self):
        init_method = self.__init__
        source_code = inspect.getsource(init_method)

        attributes = []
        for line in source_code.split('\n'):
            line = line.strip()
            if line.startswith('self.') and '=' in line:
                attr_name = line.split('=')[0].strip()[5:]
                attributes.append(attr_name)

        return attributes

    def exclude(self, other):
        attrs = self.list_constructor_attributes()
        equal_count = 0
        not_equal_count = 0
        for attr in attrs:
            if self.__getattribute__(attr) is not None and other.__getattribute__(attr) is not None and self.__getattribute__(attr) != other.__getattribute__(attr):
                if equal_count > 0:
                    return True
                not_equal_count += 1
            elif self.__getattribute__(attr) == other.__getattribute__(attr) and self.__getattribute__(attr):
                if not_equal_count > 0:
                    return True
                equal_count += 1
        return False
