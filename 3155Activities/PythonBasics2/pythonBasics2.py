# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code. Make sure to add what is going to be returned.


# Part A. count_threes
# Define a function count_threes(n) that takes an int and
# returns the number of multiples of 3 in the range from 0
# to n (including n).

def count_threes(n):
  return int(n/3) #divides n by a multiple of 3


# Part B. longest_consecutive_repeating_char
# Define a function longest_consecutive_repeating_char(s) that takes
# a string s and returns the character that has the longest consecutive repeat.
def longest_consecutive_repeating_char(s):
  n=len(s)
  count=1 #set counter to 1
  max=1 #set max to 1
  char = s[0]
  for i in range(0,n-1): #for i in range, 0 to n-1
    if s[i] ==s[i+1]: #sets s array i to s arr i+1
      count += 1 

    else:
        if count > max: #if char greater than max then set max to count, set char to s arr i and count to 1
          max = count
          char = s[i] 
          count = 1
    if count > max: #runs in for loop instead of else, sets max to count and char to s arr
      max = count
      char = s[i]
  return char


# Part C. is_palindrome
# Define a function is_palindrome(s) that takes a string s
# and returns whether or not that string is a palindrome.
# A palindrome is a string that reads the same backwards and
# forwards. Treat capital letters the same as lowercase ones
# and ignore spaces (i.e. case insensitive).
def is_palindrome(s): #s is for string
  i = 0 #set i to 0
  j = len(s)-1 #using j as a secondary i
  while i <= j: #while loop i less than or equal to j
        if s[i] == ' ': #checks if blank space for i
            i += 1 #increment
            continue #continues operation
        if s[j] == ' ': #checks if blank space for j
            j -= 1 #decrement
            continue #continues operation
        if s[i].lower() != s[j].lower(): #if string array i not equal to string array j 
            return False 
        i += 1 #increment
        j -= 1 #decrement
  return True
