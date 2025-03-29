import numpy as np
import json

class ArithmeticMixin:
    def __add__(self, other):
        return self.__class__(self.value + other.value)

    def __sub__(self, other):
        return self.__class__(self.value - other.value)

    def __mul__(self, other):
        return self.__class__(self.value * other.value)

    def __matmul__(self, other):
        return self.__class__(self.value @ other.value)

class FileMixin:
    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            file.write(str(self))

class DisplayMixin:
    def __str__(self):
        return "\n".join(" ".join(str(x) for x in row) for row in self.value)

class PropertyMixin:
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = np.array(new_value)

class NumericArray(ArithmeticMixin, FileMixin, DisplayMixin, PropertyMixin):
    def __init__(self, value):
        self.value = value
