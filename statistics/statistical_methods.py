# %%
import pandas as pd
from pandas.core.frame import DataFrame

# %% Tables
client = pd.read_csv("../clean-data/client.csv")
account = pd.read_csv("../clean-data/account.csv")
disposition = pd.read_csv("../clean-data/disposition.csv")
card = pd.read_csv("../clean-data/card_train.csv")
loan = pd.read_csv("../clean-data/loan_train.csv")
transaction = pd.read_csv("../clean-data/transaction_train.csv")
card_test = pd.read_csv("../clean-data/card_test.csv")
loan_test = pd.read_csv("../clean-data/loan_test.csv")
transaction_test = pd.read_csv("../clean-data/transaction_test.csv")

# # %% Gender per Client
gender_stats = pd.crosstab(index=client['gender'], columns='count')
gender_stats["relative"] = round(gender_stats/gender_stats.sum() * 100, 4)
gender_stats.to_csv("client_gender.csv")

# %% District per Client
district_client_stats = pd.crosstab(index=client['district_id'], columns='count')
district_client_stats["relative"] = round(district_client_stats/district_client_stats.sum() * 100, 4)
district_client_stats.to_csv("client_district.csv")

# %% District per Account
district_account_stats = pd.crosstab(index=account['district_id'], columns='count')
district_account_stats["relative"] = round(district_account_stats/district_account_stats.sum() * 100, 4)
district_account_stats.to_csv("account_district.csv")

# %% Frequency per Account
frequency_account_stats = pd.crosstab(index=account['frequency'], columns='count')
frequency_account_stats["relative"] = round(frequency_account_stats/frequency_account_stats.sum() * 100, 4)
frequency_account_stats.to_csv("account_frequency.csv")

# %% User type per Disposition

type_disposition_stats = pd.crosstab(index=disposition['type'], columns='count')
type_disposition_stats["relative"] = round(type_disposition_stats/type_disposition_stats.sum() * 100, 4)
type_disposition_stats.to_csv("type_disposition.csv")

# %% Type per Card (Train)

type_card_stats = pd.crosstab(index=card['type'], columns='count')
type_card_stats["relative"] = round(type_card_stats/type_card_stats.sum() * 100, 4)
type_card_stats.to_csv("type_card.csv")

# %% Duration per Loan (Train)

duration_loan_stats = pd.crosstab(index=loan['duration'], columns='count')
duration_loan_stats["relative"] = round(duration_loan_stats/duration_loan_stats.sum() * 100, 4)
duration_loan_stats.to_csv("duration_loan.csv")

# %% Status per Loan (Train)

status_loan_stats = pd.crosstab(index=loan['status'], columns='count')
status_loan_stats["relative"] = round(status_loan_stats/status_loan_stats.sum() * 100, 4)
status_loan_stats.to_csv("status_loan.csv")

# %% Type per Transaction (Train)

type_transaction_stats = pd.crosstab(index=transaction['type'], columns='count')
type_transaction_stats["relative"] = round(type_transaction_stats/type_transaction_stats.sum() * 100, 4)
type_transaction_stats.to_csv("type_transaction.csv")

# %% Operation per Transaction (Train)

operation_transaction_stats = pd.crosstab(index=transaction['operation'], columns='count')
operation_transaction_stats["relative"] = round(operation_transaction_stats/operation_transaction_stats.sum() * 100, 4)
operation_transaction_stats.to_csv("operation_transaction.csv")

# %% K_symbol per Transaction (Train)

k_symbol_transaction_stats = pd.crosstab(index=transaction['k_symbol'], columns='count')
k_symbol_transaction_stats["relative"] = round(k_symbol_transaction_stats/k_symbol_transaction_stats.sum() * 100, 4)
k_symbol_transaction_stats.to_csv("k_symbol_transaction.csv")

# %% Bank per Transaction (Train)

bank_transaction_stats = pd.crosstab(index=transaction['bank'], columns='count')
bank_transaction_stats["relative"] = round(bank_transaction_stats/bank_transaction_stats.sum() * 100, 4)
bank_transaction_stats.to_csv("bank_transaction.csv")

# %% Type per Card (Test)

type_card_test_stats = pd.crosstab(index=card_test['type'], columns='count')
type_card_test_stats["relative"] = round(type_card_test_stats/type_card_test_stats.sum() * 100, 4)
type_card_test_stats.to_csv("type_card_test.csv")

# %% Duration per Loan (Test)

duration_loan_test_stats = pd.crosstab(index=loan_test['duration'], columns='count')
duration_loan_test_stats["relative"] = round(duration_loan_test_stats/duration_loan_test_stats.sum() * 100, 4)
duration_loan_test_stats.to_csv("duration_loan_test.csv")

# %% Type per Transaction (Test)

type_transaction_test_stats = pd.crosstab(index=transaction_test['type'], columns='count')
type_transaction_test_stats["relative"] = round(type_transaction_test_stats/type_transaction_test_stats.sum() * 100, 4)
type_transaction_test_stats.to_csv("type_transaction_test.csv")

# %% Operation per Transaction (Test)

operation_transaction_test_stats = pd.crosstab(index=transaction_test['operation'], columns='count')
operation_transaction_test_stats["relative"] = round(operation_transaction_test_stats/operation_transaction_test_stats.sum() * 100, 4)
operation_transaction_test_stats.to_csv("operation_transaction_test.csv")

# %% K_symbol per Transaction (Test)

k_symbol_transaction_test_stats = pd.crosstab(index=transaction_test['k_symbol'], columns='count')
k_symbol_transaction_test_stats["relative"] = round(k_symbol_transaction_test_stats/k_symbol_transaction_test_stats.sum() * 100, 4)
k_symbol_transaction_test_stats.to_csv("k_symbol_transaction_test.csv")

# %% Bank per Transaction (Test)

bank_transaction_test_stats = pd.crosstab(index=transaction_test['bank'], columns='count')
bank_transaction_test_stats["relative"] = round(bank_transaction_test_stats/bank_transaction_test_stats.sum() * 100, 4)
bank_transaction_test_stats.to_csv("bank_transaction_test.csv")