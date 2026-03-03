from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        # from collections import OrderedDict
        # OrderedDict = dict + 双向链表
        self.cache = OrderedDict()  # key -> value

    def get(self, key: int) -> int:
        if key not in self.cache:  # 没有这本书
            return -1
        # 有这本书，把这本书抽出来，放到最上面（last=False 表示移到链表头）
        self.cache.move_to_end(key, last=False)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value  # 添加 key value 或者更新 value
        # 把这本书抽出来，放到最上面（last=False 表示移到链表头）
        self.cache.move_to_end(key, last=False)
        if len(self.cache) > self.capacity:  # 书太多了
            self.cache.popitem()  # 去掉最后一本书