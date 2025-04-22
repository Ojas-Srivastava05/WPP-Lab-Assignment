import numpy as np

def generate_magic_square(n):
    if n % 2 == 1:
        return generate_odd_magic_square(n)
    elif n % 4 == 0:
        return generate_doubly_even_magic_square(n)
    else:
        return generate_singly_even_magic_square(n)

def generate_odd_magic_square(n):
    magic_square = np.zeros((n, n), dtype=int)
    num = 1
    i, j = 0, n // 2

    while num <= n**2:
        magic_square[i, j] = num
        num += 1
        newi, newj = (i - 1) % n, (j + 1) % n
        if magic_square[newi, newj]:
            i += 1
        else:
            i, j = newi, newj
    return magic_square

def generate_doubly_even_magic_square(n):
    magic_square = np.arange(1, n * n + 1).reshape(n, n)
    indices = [(i, j) for i in range(n) for j in range(n)
               if (i % 4 == j % 4) or ((i + j) % 4 == 3)]
    for i, j in indices:
        magic_square[i, j] = n * n + 1 - magic_square[i, j]
    return magic_square

def generate_singly_even_magic_square(n):
    half_n = n // 2
    sub_square_size = half_n
    sub_square = generate_odd_magic_square(half_n)
    magic_square = np.zeros((n, n), dtype=int)

    # Create 4 sub-squares and fill them with sub_square values
    indices = [(0, 0), (0, 1), (1, 0), (1, 1)]
    add_vals = [0, 2, 3, 1]
    for (r, c), add in zip(indices, add_vals):
        magic_square[r * half_n:(r + 1) * half_n, c * half_n:(c + 1) * half_n] = \
            sub_square + add * half_n * half_n

    k = (n - 2) // 4
    for i in range(half_n):
        for j in range(n):
            if (j < k or j >= n - k or (j == k and i == k)):
                if j < half_n:
                    magic_square[i, j], magic_square[i + half_n, j] = \
                        magic_square[i + half_n, j], magic_square[i, j]

    return magic_square

if __name__ == "__main__":
    for n in [4, 5, 6, 7, 8]:
        print(f"\nMagic Square of size {n}:")
        print(generate_magic_square(n))
