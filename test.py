from math import inf
import heapq


m = [[1,2,3], [4,5,6], [7,8,9]]
for i in m:
    for j in i:
        print(j, end=" ")
    print("\n")
m = [list(row) for row in zip(*m)][::-1]
for i in m:
    for j in i:
        print(j, end=" ")
    print("\n")
stack = []
print(stack[-1])