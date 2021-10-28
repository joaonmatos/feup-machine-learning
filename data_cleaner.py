import csv

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
        writer.writerow([elem.strip().casefold() for elem in row])

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
