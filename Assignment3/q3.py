import math

def is_perfect_square(x):
    s = int(math.sqrt(x))
    return s * s == x

def is_fibonacci(n):
    if is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4):
        return "IsFibo"
    else:
        return "IsNotFibo"

def main():
    t = int(input("Enter the number of test cases: "))
    results = []
    for _ in range(t):
        n = int(input("Enter the number you want to check: "))
        results.append(is_fibonacci(n))

    print("\n".join(results))

if __name__ == '__main__':
    main()
