#Mad libz
# 
import re 

adjregex = re.compile(r'ADJECTIVE')

nounregex = re.compile(r'(NOUN?)')

verbregex = re.compile(r'VERB')

noun2regex = re.compile


text = 'The ADJECTIVE panda walked to the NOUN and then VERB.'
madlib = ''

print('')
print(text)
print(' ')

print('Enter an adjective, please.')
entry1 = input()

adjregex.findall(text)
text = adjregex.sub(entry1, text)
madlib = text 

print('Please enter a noun.')
entry2 = input()

nounregex.findall(text)
madlib = nounregex.sub(entry2, text)

print('Please enter a verb.')
entry3 = input()

verbregex.findall(madlib)
madlib = verbregex.sub(entry3, madlib)

print(madlib)

pandalibs = open('pandalibs.txt', 'w')
pandalibs.write(madlib)
pandalibs.close()