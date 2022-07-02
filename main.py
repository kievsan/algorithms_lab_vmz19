# Алгоритмы и структуры данных.
# 5 семестр ВМЗ-19
# Задание 1 Алгоритмы сортировки

from pprint import pprint
import time
import json
import lab1


def write_to_json_file(filename, results):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        print(f'Congratulations! The results are saved to {filename}\n')
    except OSError as other:
        print(f'There were problems opening the file {filename}: \n\t{other}\n')
        print('Sorry, the results are not saved to a json file...')


def write_to_log_file(filename, results):
    try:
        with open(filename, 'a', encoding='utf-8') as f:
            f.write('\n')
            f.write(str(time.time()) + ':\n')
            for data in results:
                f.write(data + '\n')
        print(f'The results are saved to {filename}\n')
    except OSError as other:
        print(f'There were problems opening the file {filename}: \n\t{other}\n')
        print('Sorry, the results are not saved to a log file...')


if __name__ == '__main__':
    # Лабораторная работа №1
    #
    log_resultsLab1 = []
    list_resultsLab1 = []
    header = ['item', 'array size', 'Odd-Even Sort time', 'Heap Sort time']
    header_line = '{:>10} {:>18} {:>18}'.format(header[1], header[2], header[3])
    log_resultsLab1.append(header_line)
    print(header_line)

    for size in range(5000, 100001, 5000):
        record = {header[1]: size,
                  header[2]: lab1.algorithm_OddEvenSort(size),
                  header[3]: lab1.algorithm_maxHeapSort(size)}
        list_resultsLab1.append(record)
        result = '{:>10} {:>18f} {:>18f}'.format(
            record[header[1]], record[header[2]], record[header[3]])
        log_resultsLab1.append(result)
        print(result)

    write_to_log_file('Lab1_algorithms.log', log_resultsLab1)
    if input('Do you want to save the results to json file? (Y/N) >>'
             ) in ['y', 'Y', 'н', 'Н']:
        write_to_json_file('Lab1_algorithms.json', list_resultsLab1)


