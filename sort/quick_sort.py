class QuickSort():
    """ 快速排序 """

    @staticmethod
    def sort(arr, left, right):
        if left < right:
            partition_index = QuickSort.partition(arr, left, right)
            QuickSort.sort(arr, left, partition_index - 1)
            QuickSort.sort(arr, partition_index + 1, right)
        return arr
   
    @staticmethod
    def partition(arr, left, right):
        pivot = left
        index = pivot + 1
        i = index
        while i <= right:
            if arr[i] < arr[pivot]:
                arr[i], arr[index] = arr[index], arr[i]
                index += 1
            i += 1
        arr[pivot], arr[index - 1] = arr[index - 1], arr[pivot]
        return index - 1


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    # 选择基准元素（这里选择最后一个元素）
    pivot = arr[-1]
    # 分区：小于基准的元素放在左侧，大于基准的元素放在右侧
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    # 递归排序并合并
    return quick_sort(left) + [pivot] + quick_sort(right)


def main():
    arr = [ -1, -2, -3, 4, 2, 7, 4, 3]
    print(quick_sort(arr))
    # print(QuickSort.sort(arr, 0, len(arr) - 1))

if __name__ == "__main__":
    main()

