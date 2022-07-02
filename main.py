# Алгоритмы и структуры данных.
# 5 семестр ВМЗ-19
# Задание 1 Алгоритмы сортировки

from pprint import pprint
import time
import json
import csv
import lab1


def write_to_json_file(filename, results):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        print(f'Congratulations! The results are saved to {filename}\n')
    except OSError as other:
        print(f'There were problems opening the file {filename}: \n\t{other}\n')
        print('Sorry, the results are not saved to a json file...')


def write_to_csv_file(filename, results):
    try:
        with open(filename, 'w', newline="", encoding='utf-8') as f:
            data_writer = csv.DictWriter(f, fieldnames=results[0].keys(), delimiter=',')
            data_writer.writeheader()
            data_writer.writerows(results)
        print(f'The results are saved to {filename}\n')
    except OSError as other:
        print(f'There were problems opening the file {filename}: \n\t{other}\n')
        print('Sorry, the results are not saved to a csv file...')


def write_to_log_file(filename, results):
    try:
        with open(filename, 'a', encoding='utf-8') as f:
            f.write('\n')
            f.write(str(time.time()) + ':\n')
            for data in results:
                f.write(data + '\n')
        print(f'The results are saved to {filename}')
    except OSError as other:
        print(f'There were problems opening the file {filename}: \n\t{other}\n')
        print('Sorry, the results are not saved to a log file...')


if __name__ == '__main__':
    # Лабораторная работа №1
    #
    header = ['array size', 'Odd-Even Sort time', 'Heap Sort time']
    list_resultsLab1 = []
    log_resultsLab1 = []
    header_line = '{:>10} {:>18} {:>18}'.format(header[0], header[1], header[2])
    log_resultsLab1.append(header_line)
    print(header_line)

    for size in range(50, 1001, 50):
        dict_ = {header[0]: size,
                 header[1]: lab1.algorithm_OddEvenSort(size),
                 header[2]: lab1.algorithm_maxHeapSort(size)}
        list_resultsLab1.append(dict_)
        result = '{:>10} {:>18f} {:>18f}'.format(
            dict_[header[0]], dict_[header[1]], dict_[header[2]])
        log_resultsLab1.append(result)
        print(result)

    write_to_log_file('Lab1_algorithms.log', log_resultsLab1)
    write_to_csv_file('Lab1_algorithms.csv', list_resultsLab1)
    if input('Do you want to save the results to json file? (Y/N) >>'
             ) in ['y', 'Y', 'н', 'Н']:
        write_to_json_file('Lab1_algorithms.json', list_resultsLab1)
