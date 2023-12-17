from modules import SpecialBucket


EMPTY_BUCKET = SpecialBucket.SpecialBucket(SpecialBucket.EMPTY)
DUMMY_BUCKET = SpecialBucket.SpecialBucket(SpecialBucket.DUMMY)
INIT_TABLE_SIZE = 4 # MUST BE A POWER OF 2


class QuadraticHashTable:
    def __init__(self, max_load_factor: float = 0.65) -> None:
        if not 0 < max_load_factor < 1:
            raise ValueError("Incorrect load factor") 

        self._max_load_factor = max_load_factor
        self._amount = 0
        self._size = INIT_TABLE_SIZE
        self._table = [EMPTY_BUCKET] * self._size

    def insert(self, key: int, value) -> None:
        if self._amount / self._size > self._max_load_factor:
            self._rehash()
        i = 0
        index = self.__hash(key, i)
        
        while self._table[index] not in (EMPTY_BUCKET, DUMMY_BUCKET):
            if self._table[index][0] == key:
                self._table[index][1] = value
                return
            i += 1
            index = self.__hash(key, i)

        self._table[index] = [key, value]
        self._amount += 1

    def remove(self, key: int) -> None:
        i = 0
        index = self.__hash(key, i)
        while self._table[index] != EMPTY_BUCKET and i != self._size:
            if self._table[index] != DUMMY_BUCKET and self._table[index][0] == key:
                self._amount -= 1
                self._table[index] = DUMMY_BUCKET
                break
            i += 1
            index = self.__hash(key, i)

    def search(self, key: int, return_value=None):
        i = 0
        index = self.__hash(key, i)
        while self._table[index] != EMPTY_BUCKET and i != self._size:
            if self._table[index] != DUMMY_BUCKET and self._table[index][0] == key:
                return self._table[index][1]
            i += 1
            index = self.__hash(key, i)
        
        if return_value is None:
            raise LookupError(f'No element with key: {key}')
        return return_value

    def _rehash(self) -> None:
        old_table = self._table
        self._size *= 2
        self._table = [EMPTY_BUCKET] * self._size
        self._amount = 0

        for bucket in old_table:
            if bucket not in (EMPTY_BUCKET, DUMMY_BUCKET):
                self.insert(bucket[0], bucket[1])

    def __hash(self, key: int, i: int) -> int:
        if not isinstance(key, int):
            raise TypeError("Key must be an integer")
        return (key + (i ** 2 + i) // 2) % self._size
    
    def __str__(self) -> str:
        table = '\n'.join([f'{i}:\t{str(bucket)}' for i, bucket in enumerate(self._table)])
        return f'TABLE{"-" * 45}\n{table}\n{"-" * 50}'

    @property
    def size(self) -> int:
        return self._size
    
    @property
    def amount(self) -> int:
        return self._amount

    @property
    def table(self) -> list:
        return self._table[:]
