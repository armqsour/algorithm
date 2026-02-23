class ShellSort():
    """ 希尔排序 """

    @staticmethod
    def sort(arr:list):
        if not arr or len(arr) < 2:
            return arr

        gap = len(arr) // 2
        while gap:
            for i in range(gap, len(arr)):
                pivot = arr[i]
                j = i

                while j >= gap and arr[j-gap] > pivot:
                    arr[j] = arr[j-gap]
                    j -= gap
                arr[j] = pivot
           
            gap //= 2


def main():
    arr = [ -1, -2, -3, 4, 2, 7, 4, 3]
    ShellSort.sort(arr)
    print(arr)

if __name__ == "__main__":
    main()
