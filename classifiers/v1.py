from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import csv

train_dataset = pd.read_csv("features/v1/learn.csv")
train_features = train_dataset.drop("loan_status", axis=1)
train_labels = train_dataset.loan_status

target_dataset = pd.read_csv("features/v1/test.csv")
target_features = target_dataset.drop("loan_status", axis=1).drop("loan_id", axis=1)
target_ids = target_dataset.loan_id

rf = RandomForestClassifier(n_estimators= 1000, random_state = 19)
rf.fit(train_features, train_labels)
rf.classes_

probabilities = rf.predict_proba(target_features)
positive_probabilities = [row[1] for row in probabilities]

with open("predictions/v1/random_forest.csv", "w") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["Id", "Predicted"])
    writer.writerows(zip(target_ids, positive_probabilities))
