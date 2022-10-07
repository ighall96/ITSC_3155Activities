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
  n = list(str(n)) #conv int to list 
  umap={} #dictionary
  #init all multiples of three as 0 in dict
  umap[3] = umap[6] = umap[9] = 0
  #loop iterates over list and counts multiples of three
  for i in n:
    j = int(i)
    if j%3 ==0 and j!=0:
      umap[j] = umap[j] + 1

  #find out digit with most frequency
  maxi = -1
  index = -1
  for x,y in umap.items():
    if y > maxi:
      maxi = y
      index = x

  return index


# Part B. longest_consecutive_repeating_char
# Define a function longest_consecutive_repeating_char(s) that takes
# a string s and returns the character that has the longest consecutive repeat.
def longest_consecutive_repeating_char(s):
  l=len(s)
  s=list(s)
  count=1 #set counter to 1
   #set max to -1
  umap = {}
  for i in range(0,l-1): #counts freq of chark
    if(s[i]!= s[+1]): 
      if((s[i] in umap)and umap[s[i]]>count): 
        continue
      else:
        umap[s[i]] =  count
        count = 1
    else:
      count = count +1
  umap[s[s-1]]=count
  #find max freq
  max=-1

  for z,y in umap.items():
    if y > max:
      max = y
  freqList=[]
  #add char to freqList
  for z,y in umap.items():
    if y==max:
      freqList.append(y)
   
  return freqList


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
