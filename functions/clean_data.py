def clean_data(dataset):
    # Convert empty k_symbol to None
    for index in range(len(dataset.k_symbol)):
        if dataset.k_symbol[index] == " ":
            dataset.k_symbol[index] = None

    # Interpolate missing values
    interpolated = dataset.interpolate(method ='pad')

    # Search for None Operations
    lines_to_drop = set([])
    for index in range(len(interpolated.operation)):
        if interpolated.operation[index] == None:
            lines_to_drop.add(index)

    cleaned_interpolated = interpolated.drop(list(lines_to_drop).copy(), axis=0)
    cleaned_interpolated = cleaned_interpolated.reset_index()
    cleaned_interpolated = cleaned_interpolated.drop(['index'], axis=1)
    return cleaned_interpolated