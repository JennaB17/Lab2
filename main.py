# task 1
# accept user's input
binary = int(input("Enter a binary number to convert to decimal: "))
counter = 0   #intialize the counter to equal 0
decimal = 0   #initialize decimalbinary to equal 0
remainderbinary = 0   #initialize remainderbinary to equal 0 because the reaminder is always 1 or 0

# While binary is greater than zero
while binary > 0:
  divisionbinary = binary // 10   #has to divide by 10 because 10 is the decimal sign
  remainderbinary = binary % 10  #get the remainder of the input
  decimal = decimal + remainderbinary * 2 ** counter   #needs to multiply the remainder by 2 because it is the binary sign. 
  counter = counter + 1   # And to the exponent of the counter because it counts how many times the binary number goes through the loop intil it reaches the division of 0.
  binary = divisionbinary  #initialize the input to equal the decimal binary which finds the answer. 
print("The decimal equivalent is: ", decimal)   # print the input's decimal equivalent



# task 2
# accept user's input
s = input()

print(s.replace('?', ' ')) # replace the question mark with a space

x = s.replace("?", ' ')

# count the number of words in the new string
count = x.split() 
n = len(count)

#print the number of words
print("There are",n, "words in this string.")

# if there are no questinon marks found, prompt the user to input a string with question marks
if s.find('?') <= 0:
  print('Enter a string with question marks.')