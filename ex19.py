def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man, that's enough for a party!"
    print "Get a blanket.\n"


print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def colin(weight, height, goal):
    print "Colin is overweight. He currently weighs %dlbs, which is a lot for someone who's only %s tall." % (weight, height)
    print "He's working on it though, dieting his way to %dlbs." % goal
    difference = weight - goal
    percent = 100 * (difference / weight)
    print "It won't be easy though, since the %dlbs he has to lose is %d percent of his body weight." % (difference, percent)


colin(183.0, "6'0\"", 174.0)
