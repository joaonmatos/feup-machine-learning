import csv


def no_questions(cell):
    return "" if cell == "?" else cell


with open("data/account.csv", newline="") as account:
    reader = csv.reader(account, delimiter=";", quotechar="\"")
    clean = open("clean-data/account.csv", mode="w", newline="")
    writer = csv.writer(clean, dialect="excel")
    writer.writerows(reader)

with open("data/district.csv", newline="") as district:
    reader = csv.reader(district, delimiter=";",
                        quotechar="\"", skipinitialspace=True)
    clean = open("clean-data/district.csv", mode="w", newline="")
    writer = csv.writer(clean, dialect="excel")
    for row in reader:
        writer.writerow([no_questions(elem.strip().casefold())
                        for elem in row])

with open("data/client.csv", newline="") as client:
    reader = csv.reader(client, delimiter=";",
                        quotechar="\"", skipinitialspace=True)
    rows = [row for row in reader]
    head = rows[0]
    head.append("gender")
    clean = open("clean-data/client.csv", mode="w", newline="")
    writer = csv.writer(clean, dialect="excel")
    writer.writerow([elem.strip().casefold() for elem in head])
    for row in rows[1:]:
        clean_strings = [elem.strip().casefold() for elem in row]
        birth_number = int(clean_strings[1])
        if (birth_number // 100) % 100 > 12:
            clean_strings[1] = str(birth_number - 5000)
            clean_strings.append("woman")
        else:
            clean_strings.append("man")
        writer.writerow(clean_strings)

with open("data/disp.csv", newline="") as disposition:
    reader = csv.reader(disposition, delimiter=";", quotechar="\"")
    clean = open("clean-data/disposition.csv", mode="w", newline="")
    writer = csv.writer(clean, dialect="excel")
    writer.writerows(reader)

with open("data/card_train.csv", newline="") as card:
    reader = csv.reader(card, delimiter=";", quotechar="\"")
    clean = open("clean-data/card_train.csv", mode="w", newline="")
    writer = csv.writer(clean, dialect="excel")
    writer.writerows(reader)

with open("data/card_test.csv", newline="") as card:
    reader = csv.reader(card, delimiter=";", quotechar="\"")
    clean = open("clean-data/card_test.csv", mode="w", newline="")
    writer = csv.writer(clean, dialect="excel")
    writer.writerows(reader)

with open("data/trans_test.csv", newline="") as transaction:
    reader = csv.reader(transaction, delimiter=";", quotechar="\"")
    clean = open("clean-data/transaction_test.csv", mode="w", newline="")
    writer = csv.writer(clean, dialect="excel")
    writer.writerows(reader)

with open("data/trans_train.csv", newline="") as transaction:
    reader = csv.reader(transaction, delimiter=";", quotechar="\"")
    clean = open("clean-data/transaction_train.csv", mode="w", newline="")
    writer = csv.writer(clean, dialect="excel")
    writer.writerows(reader)

with open("data/loan_train.csv", newline="") as loan:
    reader = csv.reader(loan, delimiter=";", quotechar="\"")
    clean = open("clean-data/loan_train.csv", mode="w", newline="")
    writer = csv.writer(clean, dialect="excel")
    writer.writerows(reader)

with open("data/loan_test.csv", newline="") as loan:
    reader = csv.reader(loan, delimiter=";", quotechar="\"")
    clean = open("clean-data/loan_test.csv", mode="w", newline="")
    writer = csv.writer(clean, dialect="excel")
    writer.writerows(reader)
