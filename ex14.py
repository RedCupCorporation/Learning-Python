from sys import argv

script, user_name, roommate = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "I see you live with a roommate, %s" % roommate
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Does %s like me?" % roommate
rl = raw_input(prompt)

print "Where do you and %s live?" % roommate
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said '%s' about liking me, and %s said '%s' about liking me.
You and %s live in %s.  Not sure where that is.
And you have a %s computer.  Nice.
""" % (likes, roommate, rl, roommate, lives, computer)
