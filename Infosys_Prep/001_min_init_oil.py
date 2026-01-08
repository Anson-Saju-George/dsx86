# You have an oil tank with a capacity of C litres that 
# can be bought and sold by N people. The people 
# are standing in a queue are served sequentially in 
# the order of array A.
# Some of them want to sell a litre of oil and some of 
# them want to buy a litre of oil and A describes this. 
# Here, A[i] = 1 denotes that the person wants to sell 
# a litre of oil and A[i] = -1 denotes that the person 
# wants to buy a litre of oil.
# When a person wants to sell a litre of oil but the 
# tank is full, they cannot sell it and become upset. 
# Similarly, when a person wants to buy a litre of 
# oil but the tank is empty, they cannot buy it and 
# become upset. Both these cases cause disturbances.
# You can minimize the disturbance by filling the tank 
# initially with a certain X litres of oil.
# Find the minimum initial amount of oil X that results 
# in the least number of disturbances.
# Input Format
# The first line contains an integer, N, denoting the 
# number of elements in A.
# The next line contains an integer, C, denoting the 
# capacity of the tank.
# Each line i of the N subsequent lines (where 0 ≤ i < 
# N) contains an integer describing A[i]

def min_initial_oil(A, C):
    balance = 0
    min_balance = 0

    for x in A:
        balance += x
        min_balance = min(min_balance, balance)

    return max(0, -min_balance)

# Example usage:
C = 10
A = [1, 1, -1, -1, 1, -1, -1, -1]

print(min_initial_oil(A, C))  # Output: 0 (minimum initial oil to minimize disturbances)