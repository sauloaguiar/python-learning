# Given a string, return a new string where the first and last chars have been exchanged. 

# front_back('code') → 'eodc'
# front_back('a') → 'a'
# front_back('ab') → 'ba'

def front_back(str):
  if ( len(str) <= 1 ):
   return str
  else:
   tam = len(str)
   return str[tam-1] + str[1:tam-1] + str[0]   return str[tam-1] + str[1:tam-1] + str[0]
