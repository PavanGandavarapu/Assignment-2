def calculate_cases(string):
    upper_count = 0
    lower_count = 0

    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    print("No. of Upper-case characters:", upper_count)
    print("No. of Lower-case characters:", lower_count)

input_string = 'The quick Brow Fox'
calculate_cases(input_string)