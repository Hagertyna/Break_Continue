# Python program to
# demonstrate break statement
 
s = 'Ethipia is Great country'

# Using for loop
for letter in s:
 
    print(letter)
    # break the loop as soon it sees 'e'
    # or 's'
    if letter == 'e' or letter == 's':
        break
 
print(& quot
       Out of for loop & quot
       )
print()
 
i = 0
 
# Using while loop
while True:
    print(s[i])
 
    # break the loop as soon it sees 'e'
    # or 's'
    if s[i] == 'e' or s[i] == 's':
        break
    i += 1
 
print(& quot
       Out of while loop & quot
       )
