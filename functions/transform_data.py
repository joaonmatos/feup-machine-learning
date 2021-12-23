def data_transformation_train(standardized_dataset, pre_processed_dataframe):
    amount_mean = standardized_dataset.groupby('loan_id')['amount'].mean()
    amount_max = standardized_dataset.groupby('loan_id')['amount'].max()
    amount_min = standardized_dataset.groupby('loan_id')['amount'].min()

    balance_mean = standardized_dataset.groupby('loan_id')['balance'].mean()
    balance_max = standardized_dataset.groupby('loan_id')['balance'].max()
    balance_min = standardized_dataset.groupby('loan_id')['balance'].min()

    credit_median = standardized_dataset.groupby('loan_id')['is_type_credit'].median()
    withdrawal_median = standardized_dataset.groupby('loan_id')['is_type_withdrawal'].median()
    withdrawal_in_cash_median = standardized_dataset.groupby('loan_id')['is_type_withdrawal in cash'].median()
    household_median = standardized_dataset.groupby('loan_id')['is_k_symbol_household'].median()
    insurrance_payment_median = standardized_dataset.groupby('loan_id')['is_k_symbol_insurrance payment'].median()
    interest_credited_median = standardized_dataset.groupby('loan_id')['is_k_symbol_interest credited'].median()
    payment_for_statement_median = standardized_dataset.groupby('loan_id')['is_k_symbol_payment for statement'].median()
    sanction_interest_if_negative_balance_median = standardized_dataset.groupby('loan_id')['is_k_symbol_sanction interest if negative balance'].median()
    collection_from_another_bank_median = standardized_dataset.groupby('loan_id')['is_operation_collection from another bank'].median()
    credit_card_withdrawal_median = standardized_dataset.groupby('loan_id')['is_operation_credit card withdrawal'].median()
    credit_in_cash_median = standardized_dataset.groupby('loan_id')['is_operation_credit in cash'].median()
    remittance_to_another_bank_median = standardized_dataset.groupby('loan_id')['is_operation_remittance to another bank'].median()
    op_withdrawal_in_cash_median = standardized_dataset.groupby('loan_id')['is_operation_withdrawal in cash'].median()

    features_to_copy = ["loan_date", "loan_amount", "loan_payments", "account_creation", "ratio_urban_inhabitants", "avg_salary", "unemployment", "crimes", "loan_id", "loan_status", "is_loan_duration_12", "is_loan_duration_24", "is_loan_duration_36", "is_loan_duration_48", "is_loan_duration_60"]
    processed_df = pre_processed_dataframe[features_to_copy]

    processed_df = processed_df.drop_duplicates()
    processed_df = processed_df.reset_index()
    processed_df = processed_df.drop(['index'], axis=1)
    processed_df = processed_df.set_index('loan_id')
    processed_df['amount_mean'] = amount_mean
    processed_df['amount_max'] = amount_max
    processed_df['amount_min'] = amount_min
    processed_df['balance_mean'] = balance_mean
    processed_df['balance_max'] = balance_max
    processed_df['balance_min'] = balance_min
    processed_df['credit_median'] = credit_median
    processed_df['withdrawal_median'] = withdrawal_median
    processed_df['withdrawal_in_cash_median'] = withdrawal_in_cash_median
    processed_df['household_median'] = household_median
    processed_df['insurrance_payment_median'] = insurrance_payment_median
    processed_df['interest_credited_median'] = interest_credited_median
    processed_df['payment_for_statement_median'] = payment_for_statement_median
    processed_df['sanction_interest_if_negative_balance_median'] = sanction_interest_if_negative_balance_median
    processed_df['collection_from_another_bank_median'] = collection_from_another_bank_median
    processed_df['credit_card_withdrawal_median'] = credit_card_withdrawal_median
    processed_df['credit_in_cash_median'] = credit_in_cash_median
    processed_df['remittance_to_another_bank_median'] = remittance_to_another_bank_median
    processed_df['op_withdrawal_in_cash_median'] = op_withdrawal_in_cash_median
    
    return processed_df


def data_transformation_test(pre_processed_test_dataframe):
    amount_mean = pre_processed_test_dataframe.groupby('loan_id')['amount'].mean()
    amount_max = pre_processed_test_dataframe.groupby('loan_id')['amount'].max()
    amount_min = pre_processed_test_dataframe.groupby('loan_id')['amount'].min()

    balance_mean = pre_processed_test_dataframe.groupby('loan_id')['balance'].mean()
    balance_max = pre_processed_test_dataframe.groupby('loan_id')['balance'].max()
    balance_min = pre_processed_test_dataframe.groupby('loan_id')['balance'].min()

    credit_median = pre_processed_test_dataframe.groupby('loan_id')['is_type_credit'].median()
    withdrawal_median = pre_processed_test_dataframe.groupby('loan_id')['is_type_withdrawal'].median()
    withdrawal_in_cash_median = pre_processed_test_dataframe.groupby('loan_id')['is_type_withdrawal in cash'].median()
    household_median = pre_processed_test_dataframe.groupby('loan_id')['is_k_symbol_household'].median()
    insurrance_payment_median = pre_processed_test_dataframe.groupby('loan_id')['is_k_symbol_insurrance payment'].median()
    interest_credited_median = pre_processed_test_dataframe.groupby('loan_id')['is_k_symbol_interest credited'].median()
    payment_for_statement_median = pre_processed_test_dataframe.groupby('loan_id')['is_k_symbol_payment for statement'].median()
    sanction_interest_if_negative_balance_median = pre_processed_test_dataframe.groupby('loan_id')['is_k_symbol_sanction interest if negative balance'].median()
    collection_from_another_bank_median = pre_processed_test_dataframe.groupby('loan_id')['is_operation_collection from another bank'].median()
    credit_card_withdrawal_median = pre_processed_test_dataframe.groupby('loan_id')['is_operation_credit card withdrawal'].median()
    credit_in_cash_median = pre_processed_test_dataframe.groupby('loan_id')['is_operation_credit in cash'].median()
    remittance_to_another_bank_median = pre_processed_test_dataframe.groupby('loan_id')['is_operation_remittance to another bank'].median()
    op_withdrawal_in_cash_median = pre_processed_test_dataframe.groupby('loan_id')['is_operation_withdrawal in cash'].median()

    features_to_copy = ["loan_date", "loan_amount", "loan_payments", "account_creation", "ratio_urban_inhabitants", "avg_salary", "unemployment", "crimes", "loan_id", "is_loan_duration_12", "is_loan_duration_24", "is_loan_duration_36", "is_loan_duration_48", "is_loan_duration_60"]
    processed_test_df = pre_processed_test_dataframe[features_to_copy]

    processed_test_df = processed_test_df.drop_duplicates()
    processed_test_df = processed_test_df.reset_index()
    processed_test_df = processed_test_df.drop(['index'], axis=1)
    processed_test_df = processed_test_df.set_index('loan_id')
    processed_test_df['amount_mean'] = amount_mean
    processed_test_df['amount_max'] = amount_max
    processed_test_df['amount_min'] = amount_min
    processed_test_df['balance_mean'] = balance_mean
    processed_test_df['balance_max'] = balance_max
    processed_test_df['balance_min'] = balance_min
    processed_test_df['credit_median'] = credit_median
    processed_test_df['withdrawal_median'] = withdrawal_median
    processed_test_df['withdrawal_in_cash_median'] = withdrawal_in_cash_median
    processed_test_df['household_median'] = household_median
    processed_test_df['insurrance_payment_median'] = insurrance_payment_median
    processed_test_df['interest_credited_median'] = interest_credited_median
    processed_test_df['payment_for_statement_median'] = payment_for_statement_median
    processed_test_df['sanction_interest_if_negative_balance_median'] = sanction_interest_if_negative_balance_median
    processed_test_df['collection_from_another_bank_median'] = collection_from_another_bank_median
    processed_test_df['credit_card_withdrawal_median'] = credit_card_withdrawal_median
    processed_test_df['credit_in_cash_median'] = credit_in_cash_median
    processed_test_df['remittance_to_another_bank_median'] = remittance_to_another_bank_median
    processed_test_df['op_withdrawal_in_cash_median'] = op_withdrawal_in_cash_median

    return processed_test_df