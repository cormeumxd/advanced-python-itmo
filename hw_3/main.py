import numpy as np
from matrix import Matrix

### 3.1 ###
np.random.seed(0)

a = np.random.randint(0, 10, (10, 10))
b = np.random.randint(0, 10, (10, 10))

a_matrix = Matrix(a)
b_matrix = Matrix(b)

for op in ['+', '*', '@']:
    with open(f"hw_3/artifacts/matrix{op}.txt", "w") as f:
        f.write(str(eval(f"a_matrix {op} b_matrix")))

### 3.2 ###
from mixins import NumericArray

a_matrix = NumericArray(a)
b_matrix = NumericArray(b)

for op in ['+', '*', '@']:
    eval(f"a_matrix {op} b_matrix").save_to_file(f"hw_3/artifacts/mixin{op}.txt")

### 3.3 ###
def find_collision():
    # Будем перебирать небольшие матрицы 2x2
    from itertools import product
    
    for a11, a12, a21, a22 in product(range(1, 5), repeat=4):
        A = Matrix([[a11, a12], [a21, a22]])
        for c11, c12, c21, c22 in product(range(1, 5), repeat=4):
            C = Matrix([[c11, c12], [c21, c22]])
            if hash(A) == hash(C) and A != C:
                for b11, b12, b21, b22 in product(range(1, 5), repeat=4):
                    B = Matrix([[b11, b12], [b21, b22]])
                    D = B
                    AB = A @ B
                    Matrix._shared_cache.clear() # if don't clear, AB != CD will never happen, because hash of A @ B == hash of C @ D
                    CD = C @ D
                    if AB != CD:
                        return A, B, C, D, AB, CD
    return None

A, B, C, D, AB, CD = find_collision()

for artifacts in ['A', 'B', 'C', 'D', 'AB', 'CD', 'hash']:
    with open(f"hw_3/artifacts/{artifacts}.txt", "w") as f:
        if artifacts == 'hash':
            f.write(f"AB:{hash(AB)}\nCD:{hash(CD)}")
            continue
        f.write(str(eval(artifacts)))