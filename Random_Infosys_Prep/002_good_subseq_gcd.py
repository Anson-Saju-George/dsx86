from math import gcd

def get_ans(a, p, queries):
    yes_count = 0

    for idx, val in queries:
        # update array (1-based index)
        a[idx - 1] = val

        g = 0
        count_div = 0

        # compute gcd of elements divisible by p
        for x in a:
            if x % p == 0:
                g = x if g == 0 else gcd(g, x)
                count_div += 1
                # print(f"Current element: {x}, Current GCD: {g}")

        # check condition
        if count_div >= 1 and g == p:
            yes_count += 1
    print("NO:",len(queries) - yes_count)
    return yes_count


# Example usage:
n = 5
a = [2, 3, 4, 5, 6]
p = 3
q = 3
queries = [(1, 8), (2, 10), (3, 14), (4, 2), (5, 20)]
print("YES:",get_ans(a, p, queries))  # Output: number of "YES" responses after queries
print("YES:",get_ans(a, 2, queries))  # Output: number of "YES" responses after queries