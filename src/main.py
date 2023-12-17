from modules import HashTable


def main():
    ht = HashTable.QuadraticHashTable()
    action = input('Input action\n(insert <int-key> <val>, remove <int-key>): ')
    while action != 'quit':
        data = action.split()
        if data[0] == 'insert':
            ht.insert(int(data[1]), data[2])
        elif data[0] == 'remove':
            ht.remove(int(data[1]))
        print(ht)
        action = input('Input action: ')


if __name__ == '__main__':
    main()
