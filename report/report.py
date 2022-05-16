import datetime


def data_from_file(file_path):
    file_elements = []
    with open(file_path) as file:
        for line in file:
            info = line.rstrip('\n')
            driver = info[:3]
            date_time = datetime.datetime.strptime(info[3:].replace('_', ' '), '%Y-%m-%d %H:%M:%S.%f')
            file_elements.append((driver, date_time))
    return file_elements


def get_abbreviations():
    abbreviation_list = []

    with open('D:/python/task-6-report-monaco-f1/data_files/abbreviations.txt', encoding='utf-8') as f:
        for line in f:
            abbreviation_list.append(line.rstrip('\n').split('_'))
    return abbreviation_list


def build_report(file_path):
    res_list = []
    start = data_from_file('D:/python/task-6-report-monaco-f1/data_files/start.log')
    end = data_from_file('D:/python/task-6-report-monaco-f1/data_files/end.log')
    print()
    for item in start:
        for elem in end:
            if item[0] == elem[0]:
                res_time = elem[1] - item[1]
                res_list.append([item[0], abs(res_time)])
                res_list.sort(key=lambda i: i[1])
    with open(file_path, 'w') as file:
        for line in res_list:
            file.writelines('%s\n' % line)
    return res_list


def print_report(file_path):
    result = build_report(file_path)
    abbreviations = get_abbreviations()
    place = 1
    for item in result:
        for elem in abbreviations:
            if item[0] == elem[0]:
                print(str(place) + '.' + elem[1], '|', elem[2], '|', item[1])
                place += 1
                if place == 16:
                    print("-" * 80)


def main():
    print_report('D:/python/task-6-report-monaco-f1/data_files/result.txt')


if __name__ == "__main__":
    main()
