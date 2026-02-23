import copy
import random
import time

from selection_sort import SelectionSort


class GenerateRandomArray():
    """ 生成随机整型数组 """

    @staticmethod
    def generate(min = -1_000_000, max = 1_000_000, length = 1_000) -> list:
        return [random.randint(0, length) for _ in range(length)]


def main():
    arr = GenerateRandomArray.generate(min=-1_000_000, max=1_000_000, length=1_000)
    counter_arr = copy.deepcopy(arr)

    s_time = time.time()
    SelectionSort.sort(arr)
    e1_time = time.time()
    counter_arr.sort()
    e2_time = time.time()

    print(f"selection_sort cost {e1_time - s_time:.4f}\n")
    print(f"tim_sort cost {e2_time - e1_time:.4f}\n")


    print(arr == counter_arr)

if __name__ == "__main__":
    main()