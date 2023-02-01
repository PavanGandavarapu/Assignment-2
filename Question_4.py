def get_unique(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

sample_list = [1, 2, 3, 3, 3, 3, 4, 5]
print(get_unique(sample_list))
