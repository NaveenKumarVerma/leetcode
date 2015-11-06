from sys import argv
script , usr_nm = argv
prompt = '>'

print "hi %s i am %s script" % (usr_nm,script)
print "i'd like to ask some ques"
print "do u like me %s ?" % usr_nm
likes = raw_input(prompt)

print"Where do you live %s?" % usr_nm
lives = raw_input(prompt)

print"What kinmd of computer do you have?"
computer = raw_input(prompt)

print"ok,so u said %r anty liking me.you live in %r and have a %r computer" %(likes,lives,computer)