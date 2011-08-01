i = 0
numbers = []

def while_loop(loop, increment):
    global i
    while i < loop:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + increment
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

def for_loop(num):
    global i
    for number in range(num):
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

#var = int(raw_input("How many loops? "))
#inc = int(raw_input("By what increment? "))
#while_loop(var, inc)

num = int(raw_input("How many loops - for? "))
for_loop(num)

print "The numbers: "

for num in numbers:
    print num
