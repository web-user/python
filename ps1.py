def reverse_name(first_name,last_name):
    if first_name and last_name:
        reversed_name = ' '.join([last_name, first_name])
    else:
        reversed_name = 'Error'
    return reversed_name

first_name = raw_input('What is first name? ')
last_name = raw_input('What is last namee? ')
print(reverse_name(first_name, last_name))