def print_field(field_to_print: list):
    print(" ------------- ")
    for i in range(13):
        print('|' + field_to_print[i] + '|')

    print(" ------------- ")


print("Hello, World!")
print("Time for Petanque!")

field = [' ' * 13] * 13
print_field(field)