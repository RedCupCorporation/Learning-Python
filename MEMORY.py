from random import randint
from sys import exit
from prize import winner

def print_dashes(quantity):
    print "-" * quantity

def print_lines(quantity):
    for i in range(quantity):
        print


print_lines(3)
print_dashes(60)
print "\t\t\tWelcome to MEMORY"
print "\t  The game where you have to remember stuff\n"
print "Here's how it works: COMPUTER will give you one of four colors"
print "You type in each color in order until you can't remember them anymore"
print "Answer 10 in a row correctly and you win a prize"
print "Fun right?"
print_dashes(60)
print_lines(5)

colors = ['red', 'blue', 'green', 'yellow']
memory = []
user = []

def next_color():
    global current
    current = colors[randint(0, 3)]
    return current

def add_to_list(color):
    memory.append(color)

for i in range(10):
    if user == memory:
        next_color()
        add_to_list(current)
        print "Color #%d: %s" % (i + 1, current)
        user = raw_input("> ").split(' ')
        print_lines(25)
        if "win" in user:
            winner("A's")
    
    else:
        print "You lose... at least you got %d right though" % (i - 1)
        print "The answer we were looking for was", memory
        exit(0)

winner("A's")
