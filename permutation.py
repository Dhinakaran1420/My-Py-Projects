from itertools import permutations
a=str(input())
b=[''.join(i) for i in permutations(a)]
print(b)

