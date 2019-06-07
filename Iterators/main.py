import json
import hashlib
from config import file_with_data, output_file


class ListIterator:  # итератор по списку.
    def __init__(self, list_iter):
        self.start = 0
        self.end = len(list_iter)
        self.list_iter = list_iter

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            self.item_iter = self.list_iter[self.start]
            self.start += 1
        else:
            raise StopIteration
        return self.item_iter


def hash_gen(file_path):
    with open(file_path, encoding='utf-8') as file_for_hash:
        x = 0
        while x < count_str():
            one_str = file_for_hash.readline()
            hash_str = hashlib.sha1(one_str.encode()).hexdigest()
            # print(one_str)
            yield hash_str
            x += 1


def read_write():
    """file_with_data в json_data , запись в output_file пар: страна - вики-ссылка используя ListIterator"""
    with open(file_with_data, encoding='utf-8') as data_file:
        json_data = json.load(data_file)
        with open(output_file, 'w', encoding='utf-8') as write_file:
            for item in ListIterator(json_data):
                country_name = str(item['name']['common']).replace(' ', '_')
                countries_list = f'{country_name} - https://en.wikipedia.org/wiki/{country_name}\n'
                write_file.write(countries_list)


def count_str():
    """ считает кол-во строк, return counter"""
    counter = sum(1 for _ in open(output_file, 'r'))
    return counter


if __name__ == '__main__':
    read_write()
    var_x = hash_gen(output_file)
    for item in var_x:
        print(item)
