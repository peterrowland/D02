#!/usr/bin/env python
# HW02_ch03_ex03

# This exercise can be done using only the statements and other features we
# have learned so far.

# (1) Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +


# Hint: to print more than one value on a line, you can print a
# comma-separated sequence of values:

# print('+', '-')

# By default, print advances to the next line, but you can
# override that behavior and put a space at the end, like this:

# print('+', end=' ')
# print('-')

# The output of these statements is '+ -'.

# A print statement with no argument ends the current line and
# goes to the next line.



# (2) Write a function that draws a similar grid with four rows and four columns.
################################################################################
# Write your functions below:
# Body

def border():
    print('+','- ' * 4, end='')

def pane():
    print('|','  ' * 4, end='')

def end(char):
    print(char)

def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def pattern_x2():
    do_twice(border)
    end('+')
    do_twice(pane)
    end('|')
    do_twice(pane)
    end('|')
    do_twice(pane)
    end('|')

def pattern_x4():
    do_four(border)
    end('+')
    do_four(pane)
    end('|')
    do_four(pane)
    end('|')
    do_four(pane)
    end('|')

def two_by_two():
    do_twice(pattern_x2)
    do_twice(border)
    end('+')

def four_by_four():
    do_four(pattern_x4)
    do_four(border)
    end('+')

# Too much code! This was my original attempt:

# def two_by_two():
#     i = 0
#     while i < 11:
#         if i % 5 == 0:
#             print('+','-','-','-','-','+','-','-','-','-','+')
#             #print('+', (4 * '- '),'+',4 * '- ','+')
#         else:
#             print('|',' ',' ',' ',' ','|',' ',' ',' ',' ','|')
#         i = i + 1




# Write your functions above:
################################################################################
def main():
    """Call your functions within this function.
    When complete have two function calls in this function:
    two_by_two()
    four_by_four()
    """
    two_by_two()

    four_by_four()

    print("Hello World!")




if __name__ == "__main__":
    main()
