print "Which file would you like to open?"
file = raw_input("> ")
print "Behold, %s, truncated!" % file

txt = open(file)
print txt.readline()
txt.close()
