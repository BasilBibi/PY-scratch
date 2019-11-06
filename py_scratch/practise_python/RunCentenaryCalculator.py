from py_scratch.practise_python.Centenary import calculate_year_of_centenary

while True:
    name = input('Enter your name: ')

    if name == "QUIT":
        break

    current_age = int(input('Enter your current age in years: '))
    current_year = int(input('What is the current year?: '))

    centenary_year = calculate_year_of_centenary(current_age=current_age, current_year=current_year)
    print(f'{name} will be 100 years of age in the calendar year {centenary_year}')
