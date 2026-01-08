n = 29
# Method 1 — Python built-in
bin(n).count('1')

# Method 2 — Brian Kernighan (INTERVIEW GOLD)
# n       = 101100
# n - 1   = 101011
# n & n-1 = 101000
def count_ones(n):
    count = 0
    while n:
        n &= n - 1   # removes lowest set bit
        count += 1
    return count

# Method 3 — Using bit manipulation
def count_ones_bits(n):
    count = 0
    for i in range(32):  # assuming 32-bit integer
        if n & (1 << i):
            count += 1
    return count

print("Brian Kernighan:", count_ones(n))  # Output: 4
print(f"{n} has {bin(n).count('1')} ones and {bin(n).count('0')} zeros in its binary representation using Python built-in function.")
print("Bit Manipulation:", count_ones_bits(123418276))  # Output: 15
print()
print(f"Now let's print the binary representation of {0}: {bin(0)}")
print(f"Now let's print the binary representation of {1}: {bin(1)}")
print(f"Now let's print the binary representation of {2}: {bin(2)}")
print(5, "in 04b format is:", format(5, '04b'))
print(2, "in 04b format is:", format(2, '04b'))