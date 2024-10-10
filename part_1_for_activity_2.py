
# fill in the information for the file docstring
# i think this file should be called "pixart" ngl
# the way sir asked use for color_string and its uses for functions, its soo retarded bruv

"""
File DocString
________________________________


"""

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
# moved the "PIXEL_SIZE = 30" constant from global to inside the function
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

    PIXEL_SIZE = 30

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

