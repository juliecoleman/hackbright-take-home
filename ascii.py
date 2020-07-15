# def add_shape(shape):
#     if shape == rectangle:

#         start_x = input("Choose a number between 1 and 7 for the starting x axis?")
#         start_y = input("Choose a number between 1 and 7 for the starting y axis?")
#         end_x = input("Choose a number less than or equal to 8 but greater than your starting x axis?")
#         end_y = input("Choose a number less than or equal to 8 but greater than your starting y axis?")
#         fill_char = input("What character should be used to draw your rectangle?")
#         create_rectangle(start_x, start_y, end_x, end_y, fill_char)

def create_rectangle(start_x, start_y, end_x, end_y, fill_char):

    line = '#' + (' '*(start_x - 1)) + (fill_char*(end_x - start_x)) + fill_char + (' '*(8 - end_x)) + '#'
    num_lines = end_y - start_y
    for i in range(num_lines + 1):
        print(line)

# def change_fill_char(char):

# def translate(axis, num):



def canvas():
    pound_sign = '#'*(10)
    blank_line = "#"+(' '*(8))+'#'
    # grid_line = "#"+(' '*N)+('*'*N)+(' '*N)+"#"
    print('{}{}{}'.format(pound_sign+'\n',\
                    (blank_line+'\n')*8,\
                    # (grid_line+'\n')*N,\
                    # (blank_line+'\n')*int(N/2),\
                    pound_sign))

# def clear_canvas():

if __name__ == '__main__':
    create_rectangle(2,2,4,8,'p')