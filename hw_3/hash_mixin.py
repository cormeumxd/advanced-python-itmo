from typing import Iterable
class HashMixin:
    def __hash__(self):
        "Остаток от деления на 228 суммы всех элементов"
        hash_func = lambda x: sum(map(hash_func, x)) if isinstance(x, Iterable) else x
        return int(hash_func(self.matrix)) % 228