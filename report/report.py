import datetime
import argparse
import sys


def data_from_file(file_path):
    file_elements = {}
    with open(file_path) as file:
        for line in file:
            info = line.rstrip()
            driver = info[:3]
            date_time = datetime.datetime.strptime(info[3:], '%Y-%m-%d_%H:%M:%S.%f')
            file_elements.update({driver: date_time})
    return file_elements


def get_abbreviations(folder_path):
    abbreviations = {}

    with open(f'{folder_path}/abbreviations.txt', encoding='utf-8') as f:
        for line in f:
            abbreviations.update({line[:3]: line[4:].rstrip('\n').split('_')})
    return abbreviations


def build_report(folder_path):
    start = data_from_file(f'{folder_path}/start.log')
    end = data_from_file(f'{folder_path}/end.log')
    res_dict = {}
    for start_info in start:
        for end_info in end:
            if start_info == end_info:
                result_time = abs(end[end_info] - start[start_info])
                res_dict.update({start_info: result_time})
    result = sorted(res_dict.items(), key=lambda i: i[1])
    res_list = []
    abbreviations = get_abbreviations(folder_path)
    for racer, time in result:
        for abbr in abbreviations:
            if racer == abbr:
                res_list.append('{:<17} |{:<25}| {}'.format(
                    abbreviations[abbr][0], abbreviations[abbr][1], time))
    return res_list


def print_report(folder_path):
    res_list = build_report(folder_path)
    next_stage = 15
    for place, driver in enumerate(res_list, 1):
        print(place, driver)
        if place == next_stage:
            print("-" * 65)


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--files', required=True, type=str, help='Folder path')
    parser.add_argument('--driver', type=str, help='Driver\'s name')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--asc', action='store_true')
    group.add_argument('--desc', action='store_true')
    return parser.parse_args(args)


def main(command_line_args):
    args = parse_args(command_line_args)

    if args.files is not None:
        if args.driver:
            results = build_report(args.files)
            for driver in results:
                if args.driver in driver:
                    print(driver)

        elif args.desc:
            results = build_report(args.files)
            next_stage = 16
            for place, driver in reversed(list(enumerate(results, 1))):
                print(place, driver)
                if place == next_stage:
                    print("-" * 65)

        elif args.files:
            print_report(args.files)


if __name__ == "__main__":
    main(sys.argv[1:])
