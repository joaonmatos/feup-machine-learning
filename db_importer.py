import csv
import sys

args = sys.argv
mode = args[1] if len(args) > 1 else None
if mode not in ["train", "test"]:
    mode = "train"


def parse_int(data):
    if data == "":
        return None
    else:
        return int(data)


def parse_float(data):
    if data == "":
        return None
    else:
        return float(data)


def parse_string(data):
    if data == "":
        return None
    else:
        return data


def parse_row(types, row):
    return [op(item) for op, item in zip(types, row)]


def parse_district(data):
    types = [
        parse_int,
        parse_string,
        parse_string,
        parse_int,
        parse_int,
        parse_int,
        parse_int,
        parse_int,
        parse_int,
        parse_float,
        parse_int,
        parse_float,
        parse_float,
        parse_float,
        parse_int,
        parse_int
    ]
    return [parse_row(types, row) for row in data]

def parse_account(data):
    types = [
        parse_int,
        parse_int,
        parse_string,
        parse_string
    ]
    return [parse_row(types, row) for row in data]

def parse_loan(data):
    types = [
        parse_int,
        parse_int,
        parse_string,
        parse_int,
        parse_int,
        parse_int,
        parse_int
    ]
    return [parse_row(types, row) for row in data]

with open("clean-data/district.csv", newline="") as district:
    reader = csv.reader(district)
    data = [rows for rows in reader]
    parsed_data = parse_district(data[1:])
    # print(parsed_data[0])

with open("clean-data/account.csv", newline="") as account:
    reader = csv.reader(account)
    data = [rows for rows in reader]
    parsed_data = parse_account(data[1:])
    # print(parsed_data)

with open("clean-data/loan_"+ mode +".csv", newline="") as loan:
    reader = csv.reader(loan)
    data = [rows for rows in reader]
    parsed_data = parse_loan(data[1:])
    print(parsed_data)
