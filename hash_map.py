from typing import Any


class HashMap:

    def resize(self) -> None:
        length = len(self.hashmap)

        if length == 0:
            self.hashmap = [None]
            return
        current_load = self.current_load()

        if current_load < 0.05:
            return
        else:
            temp = self.hashmap
            
            self.hashmap =  [None for _ in range(length * 10)] 
            
            for item in temp:
                if item is not None:
                    key, value = item
                    self.insert(key, value)



    def current_load(self) -> float:
        if len(self.hashmap) == 0:
            return 1
        
        else:
            filled_buckets = 0
            for key in self.hashmap:
                if key is not None:
                    filled_buckets += 1

            return filled_buckets/len(self.hashmap)

    def get(self, key: str) -> Any:
        index = self.key_to_index(key)
        
        if self.hashmap[index] is not None:
            return self.hashmap[index][1]
        else:
            raise Exception("sorry, key not found")

    def insert(self, key: str, value: Any) -> None:
        self.resize()

        index = self.key_to_index(key)

        self.hashmap[index] = (key, value)

    def key_to_index(self, key: str) -> int:
        key_sum = sum(ord(k) for k in key)

        return key_sum % len(self.hashmap)

    # don't touch below this line

    def __init__(self, size: int) -> None:
        self.hashmap = [None for i in range(size)]

    def __repr__(self) -> str:
        buckets = []
        for v in self.hashmap:
            if v != None:
                buckets.append(v)
        return str(buckets)
