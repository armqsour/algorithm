from collections import OrderedDict
from math import inf
import heapq
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