import datetime
import argparse
import sys
import operator


class Driver:
    def __init__(self, name, team):
        self.name = name
        self.team = team

    def __str__(self):
        return f'{self.name}, {self.team}'


def data_from_file(file_path):
    file_elements = {}
    with open(file_path) as file:
        for line in file:
            info = line.rstrip()
            driver = info[:3]
            date_time = datetime.datetime.strptime(info[3:], '%Y-%m-%d_%H:%M:%S.%f')
            file_elements[driver] = date_time
    return file_elements


def get_abbreviations(folder_path):
    abbreviations = {}

    with open(f'{folder_path}/abbreviations.txt', encoding='utf-8') as f:
        for line in f:
            abbr, name, team = line.rstrip('\n').split('_')
            abbreviations[abbr] = str(Driver(name=name, team=team))
        return abbreviations


def build_report(folder_path, *order):
    start = data_from_file(f'{folder_path}/start.log')
    end = data_from_file(f'{folder_path}/end.log')
    res_dict = {}
    for abbr, time in end.items():
        result_time = abs(time - start[abbr])
        res_dict.update({abbr: result_time})
    result_list = []
    abbreviations = get_abbreviations(folder_path)
    if order == ():
        result = sorted(res_dict.items(), key=operator.itemgetter(1))
        for abbr, time in result:
            name, team = abbreviations[abbr].split(',')
            result_list.append('{:<17} |{:<27}| {}'.format(
                name, team, time))
    else:
        result = sorted(res_dict.items(), key=operator.itemgetter(1), reverse=True)
        for abbr, time in result:
            name, team = abbreviations[abbr].split(',')
            result_list.append('{:<17}|{:<27}| {}'.format(
                name, team, time))
    return result_list


def print_report(folder_path, *desc):
    report = build_report(folder_path)
    next_stage = 15
    if desc == ():
        for place, driver in enumerate(report, 1):
            print(place, driver)
            if place == next_stage:
                print("-" * 65)
    else:
        for place, driver in reversed(list(enumerate(report, 1))):
            print(place, driver)
            if place == next_stage + 1:
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
            print_report(args.files, args.desc)

        elif args.files:
            print_report(args.files)


if __name__ == "__main__":
    main(sys.argv[1:])
