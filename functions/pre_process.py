import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Binarizer
from sklearn.preprocessing import OneHotEncoder

def standardize(dataset, features_to_standardize):
    # Standarization
    train_dataset_to_scale = dataset[features_to_standardize]

    # Scaler
    scaler = StandardScaler()
    scaled_train_dataset = pd.DataFrame(scaler.fit_transform(train_dataset_to_scale), columns = train_dataset_to_scale.columns)

    return scaled_train_dataset.join(dataset['loan_id'])


def remove_outliers(standardized_dataset, dataset): 
    # Remove outliers from scaled_train_dataset

    lines_to_drop = set([])
    for column in standardized_dataset.columns.difference(['loan_id']):
        for line_number in range(len(standardized_dataset[column])):
            value = standardized_dataset[column][line_number]
            if value > 3.0 or value < -3.0:
                lines_to_drop.add(line_number)


    no_outliers_train_dataset = standardized_dataset.drop(list(lines_to_drop).copy(), axis=0)
    no_outliers_cleaned_interpolated = dataset.drop(list(lines_to_drop).copy(), axis=0)

    no_outliers_train_dataset = no_outliers_train_dataset.reset_index()
    no_outliers_train_dataset = no_outliers_train_dataset.drop(['index'], axis=1)

    return no_outliers_train_dataset, no_outliers_cleaned_interpolated


def binarize(dataset, features_to_binarize):
    # Binarization
    train_dataset_to_binarize = dataset[features_to_binarize]

    # 0 <==> loan_status = -1
    # 1 <==> loan_status = 1
    binarizer = Binarizer()
    return pd.DataFrame(binarizer.fit_transform(train_dataset_to_binarize), columns = train_dataset_to_binarize.columns)


def one_hot_encode(dataset, features_to_encode):
    train_dataset_to_hotencode = dataset[features_to_encode]

    encoder = OneHotEncoder(sparse=False)
    res = encoder.fit(train_dataset_to_hotencode)

    columns = []
    for index, column_name in enumerate(features_to_encode):
        columns = columns + [f"is_{column_name}_{val}" for val in res.categories_[index]]

    return pd.DataFrame(res.transform(train_dataset_to_hotencode), columns = columns)


def re_create_dataframe(standardized_dataset, encoded_dataset, binarized_dataset):
    pre_processed_dataframe = standardized_dataset

    pre_processed_dataframe["loan_status"] = binarized_dataset.values

    for column_name in encoded_dataset.columns:
        pre_processed_dataframe[column_name] = encoded_dataset[column_name]

    return pre_processed_dataframe