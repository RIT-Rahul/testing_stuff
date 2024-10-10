
# fill in the information for the file docstring
# i think this file should be called "pixart" ngl

# the way sir asked use for color_string and its uses for functions, its soo retarded bruv
# okay so, i defined PIXEL_SIZE = 30 again under draw_grid because im not sure if we can use global variables/constants for functions, i did that for activity 1 and sir got ptsd
#   technically, we have to put these things under main() and pass it to the functions but the thing is, sir didnt mention that we are allowed to accept this argument as a parameter
#   although the easier way is to use global variables/constants, meaning these variables/constants are defined outside of all the functions
#   ok... fuck it... i will just use the global variables/constants method
#   but then again, do we even have a main??????????? oki, i just saw part 3 and although he didnt mention a main, im guessing this is just a single file so yes we put main
 

"""
File DocString
________________________________


"""

PIXEL_SIZE = 30
NUMBER_OF_COLUMNS = 20
NUMBER_OF_ROWS = 20

# added a function docstring
# renamed "parameter" as "character"
# added spaces between the "==" sign
# changed the integers like 0, 1, 2, 3 to string using ""

# should i add a "try except" block ???? not sure...
# changed the strings starting with ' to "" because it just looks better...
#   there is another technical reason but it doesnt apply to python... but still yk...
# add comments to the code :)
# fill in the information for function docstring

def get_color(character):
    """
    Function DocString
    ________________________________


    """

    if character == "0":
        return "black"
    elif character == "1":
        return "white"
    elif character == "2":
        return "red"
    elif character == "3":
        return "yellow"
    elif character == "4":
        return "orange"
    elif character == "5":
        return "green"
    elif character == "6":
        return "yellowgreen"
    elif character == "7":
        return "sienna"
    elif character == "8":
        return "tan"
    elif character == "9":
        return "gray"
    elif character == "A":
        return "darkgray"
    else:
        return None
    


# swapped position of color_string and turta cause thats what the question asked for
# added space after "color_string," for the parameter
# added function docstring
# added turta.pendown() just incase, u never know ykykykykyk
# renamed turta.fd() to turta.forward() cause that easier to understand :C
# added turta.penup() just incase, u never know ykykykyk


# add comments to the code :)
# fill in the information for function docstring

def draw_color_pixel(color_string, turta):
    """
    Function DocString
    ________________________________


    """

    turta.pendown()
    turta.begin_fill()
    turta.fillcolor(color_string)

    for i in range(4):
        turta.fd(PIXEL_SIZE)
        turta.right(90)

    turta.forward(PIXEL_SIZE)

    turta.end_fill()
    turta.penup()



# added function docstring
# swapped position of color_number and turta cause thats what the question asked for
# renamed color_number to color_string because thats what the question asked for

# add comments to the code :)
# fill in the information for function docstring

def draw_pixel(color_string, turta):
    """
    Function DocString
    ________________________________


    """

    color = get_color(color_string)
    draw_color_pixel(color, turta)



# defined the function
# added function docstring
# used a for loop, the logic is simple and im lazy to explain it here
# edited this code for part 2, the new code is from line 147 to 153, basically moving turta to the next starting for row

# add comments to the code :)
# fill in the information for function docstring


def draw_line_from_string(color_string, turta):
    """
    Function DocString
    ________________________________


    """

    for character in color_string:
        if get_color(character) != None:
            draw_pixel(character, turta)
        else:
            return False
        
    current_x = turta.xcor()
    current_y = turta.ycor()

    row_starting_x = current_x - (PIXEL_SIZE * NUMBER_OF_ROWS)
    row_starting_y = current_y - PIXEL_SIZE

    turta.goto(row_starting_x, row_starting_y)

    return True



# defined the function
# added function docstring
# by default, empty strings return a False value
#   in order for the if statement to work, it needs a True value, therefore by using "not", it converts the False to True

# add comments to the code :)
# fill in the information for function docstring

def draw_shape_from_string(turta):
    """
    Function DocString
    ________________________________


    """

    while True:

        color_string = input("Enter a color string: ")

        if not color_string:
            break
        elif draw_line_from_string(color_string, turta) == False:
            break
        else:
            draw_color_pixel(color_string, turta)



# defined the function
# added function docstring
# renamed new_x and new_y to starting_x and starting_y

# add comments to the code :)
# fill in the information for function docstring


def draw_grid(turta):
    """
    Function DocString
    ________________________________


    """

    turta.penup()
    grid_starting_x = -PIXEL_SIZE * NUMBER_OF_COLUMNS // 2
    grid_starting_y = PIXEL_SIZE * NUMBER_OF_ROWS // 2
    turta.goto(grid_starting_x, grid_starting_y)
    turta.pendown()

    COLOR_STRING_SET_ONE = "02020202020202020202"
    COLOR_STRING_SET_TWO = "20202020202020202020" 

    ITERATION_COUNT = NUMBER_OF_ROWS // 2

    for i in range(ITERATION_COUNT):
        draw_line_from_string(COLOR_STRING_SET_ONE, turta)
        draw_line_from_string(COLOR_STRING_SET_TWO, turta)
    
    turta.penup()
    grid_ending_x = grid_starting_x
    grid_ending_y = grid_starting_y - (PIXEL_SIZE * NUMBER_OF_ROWS)
    turta.goto(grid_ending_x, grid_ending_y)



# defined the function
# added function docstring

# add comments to the code :)
# fill in the information for function docstring

def main():
    """
    Function DocString
    ________________________________


    """

    from turtle import Screen, Turtle

    screen = Screen()
    turta = Turtle()

    turta.speed(0)

    draw_grid(turta)


    screen.exitonclick()

if __name__ == "__main__":
    main()
