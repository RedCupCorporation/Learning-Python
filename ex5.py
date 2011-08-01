name = 'Colin Regan'
age = 25 # not a lie
height = 74 # inches
weight = 186 # lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

height_centimeters = height * 2.54
weight_kilos = weight * .4536

print "Let's talk about %s." % name
print "He's %e centimeters tall." % height_centimeters
print "He's %e kilos heavy." % weight_kilos
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
