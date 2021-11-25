# %%
import pandas as pd

# %% Tables
client = pd.read_csv("../clean-data/client.csv")
account = pd.read_csv("../clean-data/account.csv")
disposition = pd.read_csv("../clean-data/disposition.csv")

# # %% Gender per Client
gender_stats = pd.crosstab(index=client['gender'], columns='count')
gender_stats.to_csv("client_gender.csv")

# %% District per Client
district_client_stats = pd.crosstab(index=client['district_id'], columns='count')
district_client_stats.to_csv("client_district.csv")

# %% District per Account
district_account_stats = pd.crosstab(index=account['district_id'], columns='count')
district_account_stats.to_csv("account_district.csv")

# %% Frequency per Account
frequency_account_stats = pd.crosstab(index=account['frequency'], columns='count')
frequency_account_stats.to_csv("account_frequency.csv")

# %% User type per Disposition
type_disposition_stats = pd.crosstab(index=disposition['type'], columns='count')
type_disposition_stats.to_csv("type_disposition.csv")