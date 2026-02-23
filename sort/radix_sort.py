class RadixSort():
    """ 基数排序 """

    @staticmethod
    def count_sort(arr, exp):
        n = len(arr)
        output = [0] * n
        count = [0] * 10

        for num in arr:
            index = (num // exp) % 10
            count[index] += 1
       
        for i in range(1, 10):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            index = (arr[i] // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1
            i -= 1

        for i in range(n):
             arr[i] = output[i]

    @staticmethod
    def sort(arr):
        max_num = max(arr)
        exp = 1
        while max_num // exp > 0:
            RadixSort.count_sort(arr, exp)
            exp *= 10
        return arr

def main():
    arr = [4, 2, 7, 4, 3]
    print(RadixSort.sort(arr))

if __name__ == "__main__":
    main()

