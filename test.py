from collections import Counter, OrderedDict
from math import inf
import heapq
from typing import List
from t100.linked_list.mock_listnode import ListNode, print_listnode


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

print( 2 ** 2)

dd = OrderedDict()
dd['q'] = 's'
dd['qq'] = 'ss'
print(dd)
dd.move_to_end('q')
print(dd)

tt = (('(', ')'), ('[', ']'), ('{', '}'))
print(('(',')') in tt)
print('ss'*2)
print("s"[1:])

qq = [1,2,3,4,4,2]
print(Counter(qq))