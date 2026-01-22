"""
异或计算 满足交换律和结合律
a ^ b = b ^ a
a ^ b ^ c = a ^ c ^ b
0 ^ 1 = 1
0 ^ 0 = 0

在 C / C++ / 汇编：

整数是原始类型

XOR 是 CPU 指令

在 Python里

整数是对象

XOR 是函数调用
"""

a = 1
b = 2

a = a ^ b
b = a ^ b
a = a ^ b

print(a, b)

xorarr = [1, 1, 2, 2, 2, 3, 4, 4, 3]
xor = 0
for i in xorarr:
    xor ^= i
print(xor)

xorarr = [1, 1, 2, 2, 2, 3, 4, 4, 3]
from functools import reduce
from operator import xor
print(reduce(xor, xorarr))

xorarr = [1, 1, 2, 2, 2, 3, 4, 4, 3]
from collections import Counter
for k, v in Counter(xorarr).items():
    if v % 2 == 1:
        print(k)
