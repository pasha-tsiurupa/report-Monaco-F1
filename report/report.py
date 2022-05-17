import datetime
import argparse


def data_from_file(file_path):
    file_elements = []
    with open(file_path) as file:
        for line in file:
            info = line.rstrip()
            driver = info[:3]
            date_time = datetime.datetime.strptime('{0} {1}'.format(info[3:13], info[14:]), '%Y-%m-%d %H:%M:%S.%f')
            file_elements.append((driver, date_time))
    return file_elements


def get_abbreviations(folder_path):
    abbreviation_list = []

    with open(f'{folder_path}/abbreviations.txt', encoding='utf-8') as f:
        for line in f:
            abbreviation_list.append(line.rstrip('\n').split('_'))
    return abbreviation_list


def build_report(folder_path):
    res_list = []
    start = data_from_file(f'{folder_path}/start.log')
    end = data_from_file(f'{folder_path}/end.log')
    print()
    for item in start:
        for elem in end:
            if item[0] == elem[0]:
                res_time = elem[1] - item[1]
                res_list.append([item[0], abs(res_time)])
                res_list.sort(key=lambda i: i[1])
    return res_list


def print_report(folder_path):
    racers_rating = []
    result = build_report(folder_path)
    abbreviations = get_abbreviations(folder_path)
    place = 1
    next_stage = 15
    for item in result:
        for elem in abbreviations:
            if item[0] == elem[0]:
                racers_rating.append(f'{str(place)}.{elem[1]} |{elem[2]}| {item[1]}')
                place += 1
                if place == next_stage + 1:
                    racers_rating.append("-" * 65)
    return racers_rating


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--files', required=True, type=str, help='Folder path')
    parser.add_argument('--driver', type=str, help='Driver\'s name')
    args = parser.parse_args()
    rating = print_report(args.files)

    if args.driver:
        for driver in rating:
            if args.driver in driver:
                print(driver)

            print(driver)
    elif args.files:
        for racer in rating:
            print(racer)


if __name__ == "__main__":
    main()
