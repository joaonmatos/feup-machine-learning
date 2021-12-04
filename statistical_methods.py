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


# %% Account
# District

account_district_stats = pd.crosstab(index=account['district_id'], columns='count')
account_district_stats["relative"] = round(account_district_stats/account_district_stats.sum() * 100, 4)
account_district_stats.to_csv("statistics/frequencies/account_district.csv")

with open("statistics/numbers/account_district.csv", "w", newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["Mean", account['district_id'].mean()])
    writer.writerow(["Mode", account['district_id'].mode()[0]])
    writer.writerow(["Median", account['district_id'].median()])
    writer.writerow(["1st Quarter", account['district_id'].quantile(0.25)])
    writer.writerow(["3rd Quarter", account['district_id'].quantile(0.75)])
    writer.writerow(["Standard deviation", account['district_id'].std()])
    writer.writerow(["Variance", account['district_id'].var()])

# Frequency
account_frequency_stats = pd.crosstab(index=account['frequency'], columns='count')
account_frequency_stats["relative"] = round(account_frequency_stats/account_frequency_stats.sum() * 100, 4)
account_frequency_stats.to_csv("statistics/frequencies/account_frequency.csv")

with open("statistics/numbers/account_frequency.csv", "w", newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["Mode", account['frequency'].mode()[0]])


# %% Client
# Gender
client_gender_stats = pd.crosstab(index=client['gender'], columns='count')
client_gender_stats["relative"] = round(client_gender_stats/client_gender_stats.sum() * 100, 4)
client_gender_stats.to_csv("statistics/frequencies/client_gender.csv")

with open("statistics/numbers/client_gender.csv", "w", newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["Mode", client['gender'].mode()[0]])

# District
client_district_stats = pd.crosstab(index=client['district_id'], columns='count')
client_district_stats["relative"] = round(client_district_stats/client_district_stats.sum() * 100, 4)
client_district_stats.to_csv("statistics/frequencies/client_district.csv")

with open("statistics/numbers/client_district.csv", "w", newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["Mean", client['district_id'].mean()])
    writer.writerow(["Mode", client['district_id'].mode()[0]])
    writer.writerow(["Median", client['district_id'].median()])
    writer.writerow(["1st Quarter", client['district_id'].quantile(0.25)])
    writer.writerow(["3rd Quarter", client['district_id'].quantile(0.75)])
    writer.writerow(["Standard deviation", client['district_id'].std()])
    writer.writerow(["Variance", client['district_id'].var()])


# %% Disposition
# Type
disposition_type_stats = pd.crosstab(index=disposition['type'], columns='count')
disposition_type_stats["relative"] = round(disposition_type_stats/disposition_type_stats.sum() * 100, 4)
disposition_type_stats.to_csv("statistics/frequencies/disposition_type.csv")

with open("statistics/numbers/disposition_type.csv", "w", newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["Mode", disposition['type'].mode()[0]])


# %% Card
# Type (Train)
card_type_stats = pd.crosstab(index=card['type'], columns='count')
card_type_stats["relative"] = round(card_type_stats/card_type_stats.sum() * 100, 4)
card_type_stats.to_csv("statistics/frequencies/card_type.csv")

with open("statistics/numbers/card_type.csv", "w", newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["Mode", card['type'].mode()[0]])

# Type (Test)
card_type_test_stats = pd.crosstab(index=card_test['type'], columns='count')
card_type_test_stats["relative"] = round(card_type_test_stats/card_type_test_stats.sum() * 100, 4)
card_type_test_stats.to_csv("statistics/frequencies/card_type_test.csv")

with open("statistics/numbers/card_test_type.csv", "w", newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["Mode", card_test['type'].mode()[0]])


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

# Amount (Train)
loan_amount_stats = pd.crosstab(index=loan['amount'], columns='count')
loan_amount_stats["relative"] = round(loan_amount_stats/loan_amount_stats.sum() * 100, 4)
loan_amount_stats.to_csv("statistics/frequencies/loan_amount.csv")

with open("statistics/numbers/loan_amount.csv", "w", newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["Mean", loan['amount'].mean()])
    writer.writerow(["Mode", loan['amount'].mode()[0]])
    writer.writerow(["Median", loan['amount'].median()])
    writer.writerow(["1st Quarter", loan['amount'].quantile(0.25)])
    writer.writerow(["3rd Quarter", loan['amount'].quantile(0.75)])
    writer.writerow(["Standard deviation", loan['amount'].std()])
    writer.writerow(["Variance", loan['amount'].var()])

# Payments (Train)
loan_payments_stats = pd.crosstab(index=loan['payments'], columns='count')
loan_payments_stats["relative"] = round(loan_payments_stats/loan_payments_stats.sum() * 100, 4)
loan_payments_stats.to_csv("statistics/frequencies/loan_payments.csv")

with open("statistics/numbers/loan_payments.csv", "w", newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["Mean", loan['payments'].mean()])
    writer.writerow(["Mode", loan['payments'].mode()[0]])
    writer.writerow(["Median", loan['payments'].median()])
    writer.writerow(["1st Quarter", loan['payments'].quantile(0.25)])
    writer.writerow(["3rd Quarter", loan['payments'].quantile(0.75)])
    writer.writerow(["Standard deviation", loan['payments'].std()])
    writer.writerow(["Variance", loan['payments'].var()])

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
    
# Amount (Test)
loan_amount_test_stats = pd.crosstab(index=loan_test['amount'], columns='count')
loan_amount_test_stats["relative"] = round(loan_amount_test_stats/loan_amount_test_stats.sum() * 100, 4)
loan_amount_test_stats.to_csv("statistics/frequencies/loan_amount_test.csv")

with open("statistics/numbers/loan_amount_test.csv", "w", newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["Mean", loan_test['amount'].mean()])
    writer.writerow(["Mode", loan_test['amount'].mode()[0]])
    writer.writerow(["Median", loan_test['amount'].median()])
    writer.writerow(["1st Quarter", loan_test['amount'].quantile(0.25)])
    writer.writerow(["3rd Quarter", loan_test['amount'].quantile(0.75)])
    writer.writerow(["Standard deviation", loan_test['amount'].std()])
    writer.writerow(["Variance", loan_test['amount'].var()])
    
# Payments (Test)
loan_payments_test_stats = pd.crosstab(index=loan_test['payments'], columns='count')
loan_payments_test_stats["relative"] = round(loan_payments_test_stats/loan_payments_test_stats.sum() * 100, 4)
loan_payments_test_stats.to_csv("statistics/frequencies/loan_payments_test.csv")

with open("statistics/numbers/loan_payments_test.csv", "w", newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["Mean", loan_test['payments'].mean()])
    writer.writerow(["Mode", loan_test['payments'].mode()[0]])
    writer.writerow(["Median", loan_test['payments'].median()])
    writer.writerow(["1st Quarter", loan_test['payments'].quantile(0.25)])
    writer.writerow(["3rd Quarter", loan_test['payments'].quantile(0.75)])
    writer.writerow(["Standard deviation", loan_test['payments'].std()])
    writer.writerow(["Variance", loan_test['payments'].var()])
    

# %% Transaction
# Type (Train)
transaction_type_stats = pd.crosstab(index=transaction['type'], columns='count')
transaction_type_stats["relative"] = round(transaction_type_stats/transaction_type_stats.sum() * 100, 4)
transaction_type_stats.to_csv("statistics/frequencies/transaction_type.csv")

with open("statistics/numbers/transaction_type.csv", "w", newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["Mode", transaction['type'].mode()[0]])

# Operation (Train)
transaction_operation_stats = pd.crosstab(index=transaction['operation'], columns='count')
transaction_operation_stats["relative"] = round(transaction_operation_stats/transaction_operation_stats.sum() * 100, 4)
transaction_operation_stats.to_csv("statistics/frequencies/transaction_operation.csv")

with open("statistics/numbers/transaction_operation.csv", "w", newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["Mode", transaction['operation'].mode()[0]])

# K_symbol (Train)
transaction_k_symbol_stats = pd.crosstab(index=transaction['k_symbol'], columns='count')
transaction_k_symbol_stats["relative"] = round(transaction_k_symbol_stats/transaction_k_symbol_stats.sum() * 100, 4)
transaction_k_symbol_stats.to_csv("statistics/frequencies/transaction_k_symbol.csv")

with open("statistics/numbers/transaction_k_symbol.csv", "w", newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["Mode", transaction['k_symbol'].mode()[0]])

# Bank (Train)
transaction_bank_stats = pd.crosstab(index=transaction['bank'], columns='count')
transaction_bank_stats["relative"] = round(transaction_bank_stats/transaction_bank_stats.sum() * 100, 4)
transaction_bank_stats.to_csv("statistics/frequencies/transaction_bank.csv")

with open("statistics/numbers/transaction_bank.csv", "w", newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["Mode", transaction['bank'].mode()[0]])
    
# Account-To (Train)
transaction_account_stats = pd.crosstab(index=transaction['account'], columns='count')
transaction_account_stats["relative"] = round(transaction_account_stats/transaction_account_stats.sum() * 100, 4)
transaction_account_stats.to_csv("statistics/frequencies/transaction_account.csv")

with open("statistics/numbers/transaction_account.csv", "w", newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["Mode", transaction['account'].mode()[0]])
    
# Amount (Train)
transaction_amount_stats = pd.crosstab(index=transaction['amount'], columns='count')
transaction_amount_stats["relative"] = round(transaction_amount_stats/transaction_amount_stats.sum() * 100, 4)
transaction_amount_stats.to_csv("statistics/frequencies/transaction_amount.csv")

with open("statistics/numbers/transaction_amount.csv", "w", newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["Mean", transaction['amount'].mean()])
    writer.writerow(["Mode", transaction['amount'].mode()[0]])
    writer.writerow(["Median", transaction['amount'].median()])
    writer.writerow(["1st Quarter", transaction['amount'].quantile(0.25)])
    writer.writerow(["3rd Quarter", transaction['amount'].quantile(0.75)])
    writer.writerow(["Standard deviation", transaction['amount'].std()])
    writer.writerow(["Variance", transaction['amount'].var()])
    
# Balance (Train)
transaction_balance_stats = pd.crosstab(index=transaction['balance'], columns='count')
transaction_balance_stats["relative"] = round(transaction_balance_stats/transaction_balance_stats.sum() * 100, 4)
transaction_balance_stats.to_csv("statistics/frequencies/transaction_balance.csv")

with open("statistics/numbers/transaction_balance.csv", "w", newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["Mean", transaction['balance'].mean()])
    writer.writerow(["Mode", transaction['balance'].mode()[0]])
    writer.writerow(["Median", transaction['balance'].median()])
    writer.writerow(["1st Quarter", transaction['balance'].quantile(0.25)])
    writer.writerow(["3rd Quarter", transaction['balance'].quantile(0.75)])
    writer.writerow(["Standard deviation", transaction['balance'].std()])
    writer.writerow(["Variance", transaction['balance'].var()])

# Type (Test)
transaction_type_test_stats = pd.crosstab(index=transaction_test['type'], columns='count')
transaction_type_test_stats["relative"] = round(transaction_type_test_stats/transaction_type_test_stats.sum() * 100, 4)
transaction_type_test_stats.to_csv("statistics/frequencies/transaction_type_test.csv")

with open("statistics/numbers/transaction_type_test.csv", "w", newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["Mode", transaction_test['type'].mode()[0]])

# Operation (Test)
transaction_operation_test_stats = pd.crosstab(index=transaction_test['operation'], columns='count')
transaction_operation_test_stats["relative"] = round(transaction_operation_test_stats/transaction_operation_test_stats.sum() * 100, 4)
transaction_operation_test_stats.to_csv("statistics/frequencies/transaction_operation_test.csv")

with open("statistics/numbers/transaction_operation_test.csv", "w", newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["Mode", transaction_test['operation'].mode()[0]])

# K_symbol (Test)
transaction_k_symbol_test_stats = pd.crosstab(index=transaction_test['k_symbol'], columns='count')
transaction_k_symbol_test_stats["relative"] = round(transaction_k_symbol_test_stats/transaction_k_symbol_test_stats.sum() * 100, 4)
transaction_k_symbol_test_stats.to_csv("statistics/frequencies/transaction_k_symbol_test.csv")

with open("statistics/numbers/transaction_k_symbol_test.csv", "w", newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["Mode", transaction_test['k_symbol'].mode()[0]])

# Bank (Test)
transaction_bank_test_stats = pd.crosstab(index=transaction_test['bank'], columns='count')
transaction_bank_test_stats["relative"] = round(transaction_bank_test_stats/transaction_bank_test_stats.sum() * 100, 4)
transaction_bank_test_stats.to_csv("statistics/frequencies/transaction_bank_test.csv")

with open("statistics/numbers/transaction_bank_test.csv", "w", newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["Mode", transaction_test['bank'].mode()[0]])
    
# Account-To (Test)
transaction_account_test_stats = pd.crosstab(index=transaction_test['account'], columns='count')
transaction_account_test_stats["relative"] = round(transaction_account_test_stats/transaction_account_test_stats.sum() * 100, 4)
transaction_account_test_stats.to_csv("statistics/frequencies/transaction_account_test.csv")

with open("statistics/numbers/transaction_account_test.csv", "w", newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["Mode", transaction_test['account'].mode()[0]])
    
# Amount (Test)
transaction_amount_test_stats = pd.crosstab(index=transaction_test['amount'], columns='count')
transaction_amount_test_stats["relative"] = round(transaction_amount_test_stats/transaction_amount_test_stats.sum() * 100, 4)
transaction_amount_test_stats.to_csv("statistics/frequencies/transaction_amount_test.csv")

with open("statistics/numbers/transaction_amount_test.csv", "w", newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["Mean", transaction_test['amount'].mean()])
    writer.writerow(["Mode", transaction_test['amount'].mode()[0]])
    writer.writerow(["Median", transaction_test['amount'].median()])
    writer.writerow(["1st Quarter", transaction_test['amount'].quantile(0.25)])
    writer.writerow(["3rd Quarter", transaction_test['amount'].quantile(0.75)])
    writer.writerow(["Standard deviation", transaction_test['amount'].std()])
    writer.writerow(["Variance", transaction_test['amount'].var()])
    
# Balance (Test)
transaction_balance_test_stats = pd.crosstab(index=transaction_test['balance'], columns='count')
transaction_balance_test_stats["relative"] = round(transaction_balance_test_stats/transaction_balance_test_stats.sum() * 100, 4)
transaction_balance_test_stats.to_csv("statistics/frequencies/transaction_balance_test.csv")

with open("statistics/numbers/transaction_balance_test.csv", "w", newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["Mean", transaction_test['balance'].mean()])
    writer.writerow(["Mode", transaction_test['balance'].mode()[0]])
    writer.writerow(["Median", transaction_test['balance'].median()])
    writer.writerow(["1st Quarter", transaction_test['balance'].quantile(0.25)])
    writer.writerow(["3rd Quarter", transaction_test['balance'].quantile(0.75)])
    writer.writerow(["Standard deviation", transaction_test['balance'].std()])
    writer.writerow(["Variance", transaction_test['balance'].var()])