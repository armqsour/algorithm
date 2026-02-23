class BubbleSort():
    """ 冒泡排序 """

    @staticmethod
    def sort(arr:list):
        if not arr or len(arr) < 2:
            return arr
        n = len(arr)
        for i in range(n - 1):
            swapped = False
            for j in range(0, n - 1 - i):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
            if not swapped:
                break

def main():
    arr = [ -1, -2, -3, 4, 2, 7, 4, 3]
    BubbleSort.sort(arr)
    print(arr)

if __name__ == "__main__":
    main()

