import inspect
from abc import ABC, abstractmethod


class ProblemFacts(ABC):
    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def check_if_are_exactly_the_same(self, other):
        pass

    @staticmethod
    @abstractmethod
    def get_attr_count():
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


class Person(ProblemFacts):
    def __init__(self, nationality: str | None = None, age: int | None = None, house: str | None = None,
                 data: list = None):
        self.nationality = data[0] if data else nationality
        self.age = data[1] if data else age
        self.house = data[2] if data else house

    def get_data(self):
        return self.nationality, self.age, self.house

    @staticmethod
    def get_attr_count():
        return 3

    def check_if_are_exactly_the_same(self, other):
        return self.nationality == other.nationality and self.age == other.age and self.house == other.house

    def __str__(self):
        return f'Person({self.nationality}, {self.age}, {self.house})'

    def __eq__(self, other):
        return ((self.nationality == other.nationality if (self.nationality and other.nationality) else True)
                and (self.age == other.age if (self.age and other.age) else True)
                and (self.house == other.house if (self.house and other.house) else True))
