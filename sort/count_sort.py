class CountSort():
    """ 计数排序 """

    @staticmethod
    def sort(arr):
        max_val = max(arr)
        bucket = [0] * (max_val + 1)

        for i in arr:
            bucket[i] += 1
       
        sort_index = 0
        for index in range(len(bucket)):
            while bucket[index] > 0:
                arr[sort_index] = index
                sort_index += 1
                bucket[index] -= 1
        return arr

def counting_sort_with_negatives(arr):
    if not arr:
        return arr
 
    min_val = min(arr)
    max_val = max(arr)
    offset = -min_val  # 偏移量
    range_size = max_val - min_val + 1
    count = [0] * range_size
 
    # 统计频次（偏移后）
    for num in arr:
        count[num + offset] += 1
 
    # 重构结果
    result = []
    for value in range(range_size):
        freq = count[value]
        original_value = value - offset
        result.extend([original_value] * freq)
 
    return result

def main():
    arr = [ -1, -2, -3, 4, 2, 7, 4, 3]
    # print(CountSort.sort(arr))
    print(counting_sort_with_negatives(arr))

if __name__ == "__main__":
    main()

