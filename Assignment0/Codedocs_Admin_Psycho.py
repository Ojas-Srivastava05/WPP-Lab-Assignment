def minimum_swaps(array):
    n = len(array)
    sorted_array = array[:]
    original_positions = list(range(n))

    # Sort the array manually and adjust indices
    for i in range(n - 1):
        for j in range(n - i - 1):
            if sorted_array[j] > sorted_array[j + 1]:
                sorted_array[j], sorted_array[j + 1] = sorted_array[j + 1], sorted_array[j]
                original_positions[j], original_positions[j + 1] = original_positions[j + 1], original_positions[j]

    visited = [False] * n
    swaps = 0

    for i in range(n):
        if visited[i] or original_positions[i] == i:
            continue

        cycle_size = 0
        current = i

        while not visited[current]:
            visited[current] = True
            current = original_positions[current]
            cycle_size += 1

        if cycle_size > 1:
            swaps += cycle_size - 1

    return swaps

array = [4, 3, 2, 1]
print("Minimum swaps required:", minimum_swaps(array))
