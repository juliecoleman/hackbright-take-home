print('Welcome to drawing a rectangle on a canvas in your command line!')


def add_shape(shape):
    if shape == 'rectangle':
        start_x = int(input("Choose a number between 1 and 10 for the starting x axis?"))
        start_y = int(input("Choose a number between 1 and 10 for the starting y axis?"))
        end_x = int(input("Choose a number greater than your starting x axis but less than or equal to 10?"))
        end_y = int(input("Choose a number greater than your starting y axis but less than or equal to 10??"))
        canvas(start_x, start_y, end_x, end_y)


def create_rectangle_on_canvas(start_x, start_y, end_x, end_y, fill_char):
    canvas_top_bottom = '#'*(12)
    blank_line = "#"+(' '*(10))+'#'
    num_top_blank_lines = 9 - end_y
    num_bottom_blank_lines = start_y - 2

    print(canvas_top_bottom)
    for i in range(num_top_blank_lines + 1):
        print(blank_line)

    line = '#' + (' '*(start_x - 1)) + (fill_char*(end_x - start_x)) + fill_char + (' '*(10 - end_x)) + '#'
    num_lines = end_y - start_y
    for i in range(num_lines + 1):
        print(line)

    for i in range(num_bottom_blank_lines + 1):
        print(blank_line)
    print(canvas_top_bottom)


def change_fill_char():
    fill_char = input("What character should be used to draw your rectangle?")
    return fill_char


def translate():
    axis = input('Which axis would you like to move? Please type x or y')
    num = int(input('How far would you like to move it? Make sure you do not move it off the canvas! Negative numbers will move left/down and positive numbers will move right/up'))

    return [axis, num]


def clear_canvas():
    canvas_top_bottom = '#'*(12)
    blank_line = "#"+(' '*(10))+'#'
    print(canvas_top_bottom)
    for i in range(1, 11):
        print(blank_line)
    print(canvas_top_bottom)


def canvas(start_x, start_y, end_x, end_y):

    fill_char = change_fill_char()

    create_rectangle_on_canvas(start_x, start_y, end_x, end_y, fill_char)


    change_fill = input('Would you like to change the fill character? Please type yes or no.')
    if change_fill == 'yes' or change_fill == 'Yes':
        fill_char = change_fill_char()
        print('Ok redrawing')
        create_rectangle_on_canvas(start_x, start_y, end_x, end_y, fill_char)
    elif change_fill == 'no' or change_fill == 'No':
        print('ok great')
    else:
        print('Incorrect answer.')


    move = input('Would you like to move the rectangle? Please type yes or no.')
    if move == 'yes' or move == 'Yes':
        translate_list = translate()
        if translate_list[0] == 'x':
            start_x = start_x + translate_list[1]
            end_x = end_x + translate_list[1]
        elif translate_list[0] == 'y':
            print(translate_list[1])
            start_y = start_y + translate_list[1]
            print(start_y)
            end_y = end_y + translate_list[1]
            print(end_y)
            num_top_blank_lines = 9 - end_y
            num_bottom_blank_lines = start_y - 2
        create_rectangle_on_canvas(start_x, start_y, end_x, end_y, fill_char)
    elif move == 'no' or move == 'No':
        print('ok great')
    else:
        print('Incorrect answer')


    clear = input('Would you like to clear your canvas? Please type yes or no.')
    if clear == 'yes' or clear == 'Yes':
        clear_canvas()


    start_again = input('Would you like to add a new rectangle? Please type yes or no.')
    if start_again == 'yes' or start_again == 'Yes':
        add_shape('rectangle')
    else: print('Goodbye')


if __name__ == '__main__':
    add_shape('rectangle')