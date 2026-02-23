class SelectionSort:
    """ 选择排序 """

    @staticmethod
    def sort(arr: list = None) -> list:
        # 元素个数小于2，自然有序
        if not arr or len(arr) < 2:
            return
        
        for idx in range(len(arr) - 1):
            min_indx = idx
            for i in range(idx + 1, len(arr)):
                if arr[min_indx] > arr[i]:
                    min_indx = i
            arr[min_indx], arr[idx] = arr[idx], arr[min_indx]