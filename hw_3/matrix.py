from abc import ABC, abstractmethod
from typing import Iterable
from numbers import Number
from functools import lru_cache
from hash_mixin import HashMixin

class Matrix(HashMixin):
    _shared_cache = {} # for 3.3

    def __init__(self, matrix: Iterable[Iterable[Number]]):
        self.matrix = matrix

        if not all(len(row) == len(self.matrix[0]) for row in self.matrix):
            raise ValueError("Matrix must be same size")
        
        if not all(isinstance(item, Number) for row in self.matrix for item in row):
            raise ValueError("Matrix must contain only numbers")
        
    def __add__(self, other: 'Matrix') -> 'Matrix':
        if not isinstance(other, Matrix):
            raise TypeError("Can only add matrices")
        
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Matrices must be same size")

        return Matrix([[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))])

    def __mul__(self, other: 'Matrix') -> 'Matrix':
        if not isinstance(other, Matrix):
            raise TypeError("Can only multiply matrices")
        
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Matrices must be same size")
        
        return Matrix([[self.matrix[i][j] * other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))])

    def __matmul__(self, other: 'Matrix') -> 'Matrix':
        if not isinstance(other, Matrix):
            raise TypeError("Can only multiply matrices")
        
        if len(self.matrix[0]) != len(other.matrix):
            raise ValueError("Can't multiply matrices")
        
        cache_key = (hash(self), hash(other))
        if cache_key in Matrix._shared_cache:
            return Matrix._shared_cache[cache_key]

        result = Matrix([[sum(self.matrix[i][j] * other.matrix[j][k] for j in range(len(self.matrix[0]))) for k in range(len(other.matrix[0]))] for i in range(len(self.matrix))])
        Matrix._shared_cache[cache_key] = result

        return result
        
    def __eq__(self, other: 'Matrix') -> bool:
        if not isinstance(other, Matrix):
            raise TypeError("Can only compare matrices")
        
        if len(self.matrix[0]) != len(other.matrix[0]) or len(self.matrix) != len(other.matrix):
            return False
        
        return all(self.matrix[i][j] == other.matrix[i][j] for i in range(len(self.matrix)) for j in range(len(self.matrix[0])))
    
    def __hash__(self):
        return super().__hash__()

    def __str__(self):
        return "\n".join(" ".join(str(x) for x in row) for row in self.matrix)
