import random

UPPER_BOUND = 13
LOWER_BOUND = 1

def print_field(field_to_print: list):
    border = "-------------------------------------------"
    print(border)
    for i in range(UPPER_BOUND):
        current = "|  "
        for ii in range(UPPER_BOUND):
            current += field_to_print[i][ii] + "  "
        current += "|"
        print(current)
    print(border)

def get_initial_coordinates():
    return random.randint(LOWER_BOUND - 1, UPPER_BOUND - 1), random.randint(LOWER_BOUND - 1, UPPER_BOUND - 1)

def create_initial_array():
    return [["0" for i in range(UPPER_BOUND)] for j in range(UPPER_BOUND)]

def add_orthogonal(target_coordinate, input_coordinate):
    orthogonal = 0

    print("target {}, input {}".format(target_coordinate, input_coordinate))
    if target_coordinate != input_coordinate:
        orthogonal = random.randint(0, 1)
        if target_coordinate < input_coordinate:
            orthogonal * -1

    if input_coordinate + orthogonal < LOWER_BOUND or input_coordinate + orthogonal > UPPER_BOUND:
        orthogonal = 0

    print("Threw with orthogonal {}".format(orthogonal))
    return orthogonal

def throw(input_x, input_y, player):
    force = random.randint(0, 5)
    #orthogonal = random.randint(0, 1)

    #go from 1-13 to 0-12 due to zero indexed arrays
    final_x, final_y = input_x - 1, input_y - 1

    #throwing from top to bottom
    if input_x == LOWER_BOUND:
        final_x += force
        final_y += add_orthogonal(target_y, input_y)

    #throwing from bottom to top
    elif input_x == UPPER_BOUND:
        final_x -= force
        final_y += add_orthogonal(target_y, input_y)

    #throwing from left to right
    elif input_y == LOWER_BOUND:
        final_x += add_orthogonal(target_x, input_x)
        final_y += force

    #throwing from right to left
    elif input_y == UPPER_BOUND:
        final_x += add_orthogonal(target_x, input_x)
        final_y -= force

    arr[final_x][final_y] = player

    print("Threw with force {}".format(force))

def get_coordinates_from_player():
    print("Use values between 1 and 13")
    print("Choose x:")
    input_x = int(input())
    print("Choose y:")
    input_y = int(input())
    return input_x, input_y

def validate_coordinates(input_x, input_y):
    valid = False
    if (input_x == LOWER_BOUND or input_x == UPPER_BOUND) and LOWER_BOUND <= input_y <= UPPER_BOUND:
        valid = True
    elif (input_y == LOWER_BOUND or input_y == UPPER_BOUND) and LOWER_BOUND <= input_x <= UPPER_BOUND:
        valid = True

    return valid

def get_current_player(round_count):
    if count % 2 == 0:
        player = "1"

    else:
        player = "2"
    return player

print("Time for Petanque!")

arr = create_initial_array()
target_x,target_y = get_initial_coordinates()
arr[target_x][target_y] = "X"
print_field(arr)

count = 0
while True:
    current_player = get_current_player(count)
    print("Turn player " + current_player + "!")

    player_x, player_y = get_coordinates_from_player()
    is_valid = validate_coordinates(player_x, player_y)

    if is_valid:
        throw(player_x, player_y, current_player)
        print_field(arr)
        count += 1
    else:
        print("Invalid coordinates!")
        continue