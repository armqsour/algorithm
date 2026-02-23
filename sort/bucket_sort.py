class BucketSort():
    """ 桶排序 """

    @staticmethod
    def sort(arr, bucket_size = 10):
        if not len(arr):
            return arr

        min_val = min(arr)
        max_val = max(arr)

        bucket_count = (max_val - min_val) // bucket_size + 1
        buckets = [[] for _ in range(bucket_count)]

        for n in arr:
            index = int(( n - min_val) // bucket_size)
            buckets[index].append(n)
       
        sorted_arr = []
        for bucket in buckets:
            sorted_arr.extend(sorted(bucket))
       
        return sorted_arr

def main():
    arr = [ -1, -2, -3, 4, 2, 7, 4, 3]
    print(BucketSort.sort(arr, 10))

if __name__ == "__main__":
    main()

