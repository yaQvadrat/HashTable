from modules import HashTable
from random import randint


def random_ht(ht) -> dict:
    dct = {}
    for _ in range(randint(10, 100000)):
        key = randint(-10000, 10000)
        value = randint(0, 100)
        ht.insert(key, value)
        dct[key] = value
    
    return dct


class TestHashTable:
    def test_insert(self):
        ht = HashTable.QuadraticHashTable()
        dct = random_ht(ht)
        table = [tuple(bucket) for bucket in ht.table if bucket not in (HashTable.EMPTY_BUCKET, HashTable.DUMMY_BUCKET)]
        dct_items = dct.items()

        assert all(map(lambda bucket: bucket in dct_items, table))

    def test_search(self):
        ht = HashTable.QuadraticHashTable()
        dct = random_ht(ht)
        keys = list(dct.keys())
        random_key = keys[randint(0, len(keys))]

        assert dct[random_key] == ht.search(random_key)

    def test_remove(self):
        ht = HashTable.QuadraticHashTable()
        dct = random_ht(ht)
        keys = list(dct.keys())
        random_key = keys[randint(0, len(keys))]
        del dct[random_key]
        ht.remove(random_key)
        table = [tuple(bucket) for bucket in ht.table if bucket not in (HashTable.EMPTY_BUCKET, HashTable.DUMMY_BUCKET)]
        dct_items = dct.items()

        assert all(map(lambda bucket: bucket in dct_items, table))
