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
    return random.randint(LOWER_BOUND, UPPER_BOUND), random.randint(LOWER_BOUND, UPPER_BOUND)

def create_initial_array():
    return [["0" for i in range(UPPER_BOUND)] for j in range(UPPER_BOUND)]

def throw(input_x, input_y, player):
    force = random.randint(0, 5)
    orthogonal = random.randint(0,1)

    #check what the edge is
    if input_x == LOWER_BOUND:
        temp_y = input_y - 1
        if target_y != input_y:
            if target_y > input_y:
                temp_y += orthogonal
            else:
                temp_y -= orthogonal
        arr[input_x - 1 + force][temp_y] = player
    elif input_x == UPPER_BOUND:
        arr[input_x - 1 - force][input_y - 1 - orthogonal] = player
    elif input_y == LOWER_BOUND:
        arr[input_x - 1 + orthogonal][input_y - 1 + force] = player
    elif input_y == UPPER_BOUND:
        arr[input_x - 1 - orthogonal][input_y - 1 - force] = player
    print("Threw with force {} and orthogonal {}".format(force, orthogonal))

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