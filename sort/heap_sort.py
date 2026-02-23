class HeapSort():
    """ 堆排序 """

    @staticmethod
    def sort(arr):
        n = len(arr)
        for i in range( n // 2 - 1, -1, -1):
            HeapSort.heapify(arr, n, i)
       
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            HeapSort.heapify(arr, i, 0)
       
        return arr
   
    @staticmethod
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
       
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            HeapSort.heapify(arr, n, largest)


def main():
    arr = [ -1, -2, -3, 4, 2, 7, 4, 3]
    print(HeapSort.sort(arr))

if __name__ == "__main__":
    main()

