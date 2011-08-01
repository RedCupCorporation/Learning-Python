def hypotenuse(a, b):
    return (a * a + b * b)**.5

print "Let's find the length of the hypotenuse, given the lengths of the two adjacent sides of the right triangle"
first = int(raw_input("First side: "))
second = int(raw_input("Second side: "))

print hypotenuse(first, second)
