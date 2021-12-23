from sklearn.feature_selection import SequentialFeatureSelector

def sequencial_feature_selector(pre_processed_features, pre_processed_labels, unfit_classifier, n_features, direction):
    feature_names = pre_processed_features.columns

    sfs = SequentialFeatureSelector(
        unfit_classifier, n_features_to_select=n_features, direction=direction
    ).fit(pre_processed_features, pre_processed_labels)

    return feature_names[sfs.get_support()]
