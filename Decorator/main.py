from datetime import datetime
import json

data_rss = {}
i = 0
word_list = []


# ======= часть с декоратором ========
def my_decorator_with_attribute(path_to_log):
    start_time = datetime.now()
    path = path_to_log

    def main_decorator(old_function):
        def new_function(*args, **kwargs):
            arguments_used = [*args]
            something = old_function(*args, **kwargs)
            nonlocal start_time, path
            with open(path, 'w', encoding='utf-8') as write_file:
                write_file.write(f' дата и время вызова: {start_time: %d.%m.%Y %H:%M}\n'
                                 f' имя функции: {old_function.__name__}\n'
                                 f' аргументы с которыми вызывалась:  {arguments_used} \n'
                                 f' возвращает: {something}\n')
            return something, start_time

        return new_function

    return main_decorator

# ====== конец части с декоратором, начало части старого задания =====


with open('newsafr.json', encoding='utf-8') as datafile:
    json_data = json.load(datafile)
    data_rss = json_data['rss']

while i != len(data_rss['channel']['items']):
    # pprint(data_rss['channel']['items'][i]['description'])
    for word in data_rss['channel']['items'][i]['description'].split(' '):
        if len(word) > 6:
            word_list.append(word.lower())
    i += 1


@my_decorator_with_attribute('out_logfile.txt')  # декоратор для логов
def get_sort(string_list, top):
    seen = {}
    k = 0

    for find_word in string_list:
        if find_word not in seen:
            seen[find_word] = 1
        else:
            seen[find_word] += 1

    dcit_sort = sorted(seen.items(), key=lambda kv: kv[1])
    dcit_sort.reverse()
    for i_sort in dcit_sort:
        if k < top:
            print(i_sort[0], '-', i_sort[1], 'раз ввстречается')
            k += 1
        else:
            break

    return dcit_sort


get_sort(word_list, 10)
