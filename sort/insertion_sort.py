class InsertionSort():
    """ 选择排序 """

    @staticmethod
    def sort(arr:list):
        if not arr or len(arr) < 2:
            return arr

        for i in range(1, len(arr)):
            pivot = arr[i]
            j = i
            while(j >= 1 and arr[j - 1] > pivot):
                arr[j] = arr[j - 1]
                j -= 1
            arr[j] = pivot

def main():
    arr = [ -1, -2, -3, 4, 2, 7, 4, 3]
    InsertionSort.sort(arr)
    print(arr)

if __name__ == "__main__":
    main()
