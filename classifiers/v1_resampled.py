# %%
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import csv
from imblearn.combine import SMOTETomek

# %%
train_dataset = pd.read_csv("features/v1/learn.csv")
train_features = train_dataset.drop("loan_status", axis=1)
train_labels = train_dataset.loan_status
train_dataset.value_counts(subset=["loan_status"])

# %%
smt = SMOTETomek(random_state=19, sampling_strategy="auto")
feaures_res, labels_res = smt.fit_resample(train_features, train_labels)
pd.DataFrame(labels_res).value_counts(subset=["loan_status"])

# %%
rf = RandomForestClassifier(n_estimators= 30, random_state = 19)
rf.fit(feaures_res, labels_res)

# %%
target_dataset = pd.read_csv("features/v1/test.csv")
target_features = target_dataset.drop("loan_status", axis=1).drop("loan_id", axis=1)
target_ids = target_dataset.loan_id

# %%
probabilities = rf.predict_proba(target_features)
positive_probabilities = [row[1] for row in probabilities]

# %%
with open("predictions/v1/random_forest_resampled.csv", "w") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["Id", "Predicted"])
    writer.writerows(zip(target_ids, positive_probabilities))



