# %%
import pandas as pd
import csv
from pandas.io.parsers import read_csv

# %% Tables
client = pd.read_csv("clean-data/client.csv", dtype={"gender": "string", "district_id": int})
account = pd.read_csv("clean-data/account.csv", dtype={"district_id": int, "frequency": "string"})
disposition = pd.read_csv("clean-data/disposition.csv", dtype={"type": "string"})
district = pd.read_csv("clean-data/district.csv")
card = pd.read_csv("clean-data/card_train.csv", dtype={"type": "string"})
card_test = pd.read_csv("clean-data/card_test.csv", dtype={"type": "string"})
loan = pd.read_csv("clean-data/loan_train.csv", dtype={"amount": int, "duration": int, "status": int})
loan_test = pd.read_csv("clean-data/loan_test.csv", dtype={"amount": int, "duration": int})
transaction = pd.read_csv("clean-data/transaction_train.csv", dtype={"type": "string", "operation": "string", "k_symbol": "string", "bank": "string"})
transaction_test = pd.read_csv("clean-data/transaction_test.csv", dtype={"type": "string", "operation": "string", "k_symbol": "string", "bank": "string"})


# # %% Account
# # District

# account_district_stats = pd.crosstab(index=account['district_id'], columns='count')
# account_district_stats["relative"] = round(account_district_stats/account_district_stats.sum() * 100, 4)
# account_district_stats.to_csv("statistics/frequencies/account_district.csv")

# with open("statistics/numbers/account_district.csv", "w", newline='') as outfile:
#     writer = csv.writer(outfile)
#     writer.writerow(["Mean", account['district_id'].mean()])
#     writer.writerow(["Mode", account['district_id'].mode()[0]])
#     writer.writerow(["Median", account['district_id'].median()])
#     writer.writerow(["1st Quarter", account['district_id'].quantile(0.25)])
#     writer.writerow(["3rd Quarter", account['district_id'].quantile(0.75)])
#     writer.writerow(["Standard deviation", account['district_id'].std()])
#     writer.writerow(["Variance", account['district_id'].var()])

# # Frequency
# account_frequency_stats = pd.crosstab(index=account['frequency'], columns='count')
# account_frequency_stats["relative"] = round(account_frequency_stats/account_frequency_stats.sum() * 100, 4)
# account_frequency_stats.to_csv("statistics/frequencies/account_frequency.csv")

# with open("statistics/numbers/account_frequency.csv", "w", newline='') as outfile:
#     writer = csv.writer(outfile)
#     writer.writerow(["Mode", account['frequency'].mode()[0]])


# # %% Client
# # Gender
# client_gender_stats = pd.crosstab(index=client['gender'], columns='count')
# client_gender_stats["relative"] = round(client_gender_stats/client_gender_stats.sum() * 100, 4)
# client_gender_stats.to_csv("statistics/frequencies/client_gender.csv")

# with open("statistics/numbers/client_gender.csv", "w", newline='') as outfile:
#     writer = csv.writer(outfile)
#     writer.writerow(["Mode", client['gender'].mode()[0]])

# # District
# client_district_stats = pd.crosstab(index=client['district_id'], columns='count')
# client_district_stats["relative"] = round(client_district_stats/client_district_stats.sum() * 100, 4)
# client_district_stats.to_csv("statistics/frequencies/client_district.csv")

# with open("statistics/numbers/client_district.csv", "w", newline='') as outfile:
#     writer = csv.writer(outfile)
#     writer.writerow(["Mean", client['district_id'].mean()])
#     writer.writerow(["Mode", client['district_id'].mode()[0]])
#     writer.writerow(["Median", client['district_id'].median()])
#     writer.writerow(["1st Quarter", client['district_id'].quantile(0.25)])
#     writer.writerow(["3rd Quarter", client['district_id'].quantile(0.75)])
#     writer.writerow(["Standard deviation", client['district_id'].std()])
#     writer.writerow(["Variance", client['district_id'].var()])


# # %% Disposition
# # Type
# disposition_type_stats = pd.crosstab(index=disposition['type'], columns='count')
# disposition_type_stats["relative"] = round(disposition_type_stats/disposition_type_stats.sum() * 100, 4)
# disposition_type_stats.to_csv("statistics/frequencies/disposition_type.csv")

# with open("statistics/numbers/disposition_type.csv", "w", newline='') as outfile:
#     writer = csv.writer(outfile)
#     writer.writerow(["Mode", disposition['type'].mode()[0]])


# # %% Card
# # Type (Train)
# card_type_stats = pd.crosstab(index=card['type'], columns='count')
# card_type_stats["relative"] = round(card_type_stats/card_type_stats.sum() * 100, 4)
# card_type_stats.to_csv("statistics/frequencies/card_type.csv")

# with open("statistics/numbers/card_type.csv", "w", newline='') as outfile:
#     writer = csv.writer(outfile)
#     writer.writerow(["Mode", card['type'].mode()[0]])

# # Type (Test)
# card_type_test_stats = pd.crosstab(index=card_test['type'], columns='count')
# card_type_test_stats["relative"] = round(card_type_test_stats/card_type_test_stats.sum() * 100, 4)
# card_type_test_stats.to_csv("statistics/frequencies/card_type_test.csv")

# with open("statistics/numbers/card_test_type.csv", "w", newline='') as outfile:
#     writer = csv.writer(outfile)
#     writer.writerow(["Mode", card_test['type'].mode()[0]])


# %% Loan
# Duration (Train)
loan_duration_stats = pd.crosstab(index=loan['duration'], columns='count')
loan_duration_stats["relative"] = round(loan_duration_stats/loan_duration_stats.sum() * 100, 4)
loan_duration_stats.to_csv("statistics/frequencies/loan_duration.csv")

with open("statistics/numbers/loan_duration.csv", "w", newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["Mean", loan['duration'].mean()])
    writer.writerow(["Mode", loan['duration'].mode()[0]])
    writer.writerow(["Median", loan['duration'].median()])
    writer.writerow(["1st Quarter", loan['duration'].quantile(0.25)])
    writer.writerow(["3rd Quarter", loan['duration'].quantile(0.75)])
    writer.writerow(["Standard deviation", loan['duration'].std()])
    writer.writerow(["Variance", loan['duration'].var()])

# Status (Train)
loan_status_stats = pd.crosstab(index=loan['status'], columns='count')
loan_status_stats["relative"] = round(loan_status_stats/loan_status_stats.sum() * 100, 4)
loan_status_stats.to_csv("statistics/frequencies/loan_status.csv")

with open("statistics/numbers/loan_status.csv", "w", newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["Mode", loan['status'].mode()[0]])

# Duration (Test)
loan_duration_test_stats = pd.crosstab(index=loan_test['duration'], columns='count')
loan_duration_test_stats["relative"] = round(loan_duration_test_stats/loan_duration_test_stats.sum() * 100, 4)
loan_duration_test_stats.to_csv("statistics/frequencies/loan_duration_test.csv")

with open("statistics/numbers/loan_duration_test.csv", "w", newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["Mean", loan_test['duration'].mean()])
    writer.writerow(["Mode", loan_test['duration'].mode()[0]])
    writer.writerow(["Median", loan_test['duration'].median()])
    writer.writerow(["1st Quarter", loan_test['duration'].quantile(0.25)])
    writer.writerow(["3rd Quarter", loan_test['duration'].quantile(0.75)])
    writer.writerow(["Standard deviation", loan_test['duration'].std()])
    writer.writerow(["Variance", loan_test['duration'].var()])

# # %% Transaction
# # Type (Train)
# type_transaction_stats = pd.crosstab(index=transaction['type'], columns='count')
# type_transaction_stats["relative"] = round(type_transaction_stats/type_transaction_stats.sum() * 100, 4)
# type_transaction_stats.to_csv("type_transaction.csv")

# # Operation (Train)
# operation_transaction_stats = pd.crosstab(index=transaction['operation'], columns='count')
# operation_transaction_stats["relative"] = round(operation_transaction_stats/operation_transaction_stats.sum() * 100, 4)
# operation_transaction_stats.to_csv("operation_transaction.csv")

# # K_symbol (Train)
# k_symbol_transaction_stats = pd.crosstab(index=transaction['k_symbol'], columns='count')
# k_symbol_transaction_stats["relative"] = round(k_symbol_transaction_stats/k_symbol_transaction_stats.sum() * 100, 4)
# k_symbol_transaction_stats.to_csv("k_symbol_transaction.csv")

# # Bank (Train)
# bank_transaction_stats = pd.crosstab(index=transaction['bank'], columns='count')
# bank_transaction_stats["relative"] = round(bank_transaction_stats/bank_transaction_stats.sum() * 100, 4)
# bank_transaction_stats.to_csv("bank_transaction.csv")

# # Type (Test)
# type_transaction_test_stats = pd.crosstab(index=transaction_test['type'], columns='count')
# type_transaction_test_stats["relative"] = round(type_transaction_test_stats/type_transaction_test_stats.sum() * 100, 4)
# type_transaction_test_stats.to_csv("type_transaction_test.csv")

# # Operation (Test)
# operation_transaction_test_stats = pd.crosstab(index=transaction_test['operation'], columns='count')
# operation_transaction_test_stats["relative"] = round(operation_transaction_test_stats/operation_transaction_test_stats.sum() * 100, 4)
# operation_transaction_test_stats.to_csv("operation_transaction_test.csv")

# # K_symbol (Test)
# k_symbol_transaction_test_stats = pd.crosstab(index=transaction_test['k_symbol'], columns='count')
# k_symbol_transaction_test_stats["relative"] = round(k_symbol_transaction_test_stats/k_symbol_transaction_test_stats.sum() * 100, 4)
# k_symbol_transaction_test_stats.to_csv("k_symbol_transaction_test.csv")

# # Bank (Test)
# bank_transaction_test_stats = pd.crosstab(index=transaction_test['bank'], columns='count')
# bank_transaction_test_stats["relative"] = round(bank_transaction_test_stats/bank_transaction_test_stats.sum() * 100, 4)
# bank_transaction_test_stats.to_csv("bank_transaction_test.csv")