print "You're faced with a critical decision. Do you 1) study for law school or 2) bow to the peer pressure of monday night dinner with your lame friends in Santa Monica?"

choice = int(raw_input("> "))

if choice == 1:
    print "Your friends play the 'But you studied for law school last week!' card"
    print "1. Succumb."
    print "2. Study."

    final = int(raw_input("> "))

    if final == 1:
        print "You get good grades anyway."
    elif final == 2:
        print "You get good grades."
    else:
        print "Ah, secret option %d eh? Good choice: you study, do well in class, and make some new friends who aren't idiots." % final

elif choice == 2:
    print "You should really get some new friends."
    print "1. But other girls just don't get me like they do!."
    print "2. But I suck at change!."
    print "3. You make a good point Colin. You know, I don't tell you this enough, but you're always right."

    friends = int(raw_input("> "))

    if friends == 1 or friends == 2:
        print "Due to a dearth of options, Megan Stegner will be a bridesmaid at your sad, lonely wedding."
    else:
        print "I am always right aren't I? In the words of Grandma Saracen, \"Matt, you need to get a new friend.\""

else:
    print "Ah, secret option %d eh? Good choice: you study, do well in class, and make some new friends who aren't idiots." % choice
