#bigger is greater
def next_permutation(w):
    def all_permutations(s, step=0, result=set()):
        if step == len(s):
            result.add("".join(s))
        for i in range(step, len(s)):
            s[step], s[i] = s[i], s[step]
            all_permutations(s[:], step + 1, result)
            s[step], s[i] = s[i], s[step]
        return sorted(result)
    
    perms = all_permutations(list(w))
    for perm in perms:
        if perm > w:
            return perm
    return "no answer"

def main():
    t = int(input().strip())
    results = []
    for _ in range(t):
        w = input().strip()
        results.append(next_permutation(w))
    print("\n".join(results))

if __name__ == "__main__":
    main()