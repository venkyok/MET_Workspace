# dict  key should be string or number, float even bool and also tuple
# a set can have tuple , string, number, float, bool but not list or dict


fruits = [['apple', 'banana'],[ 'cherry', 'orange'],3]

# fruits1 = [['apple', 'banana'],{ 'cherry', 'orange'},3]

# prinnt(fruits1[1][0]) ❌ # ['apple', 'banana']

print(fruits[0][0]) # ['apple', 'banana']


# print(fruits[0]{1})  ❌ # ['apple', 'banana']


#1 . non empty string -True 
#2 non empty list -True
#3 non empty tuple -True
#4 non empty set -True
#5 non empty dict -True
#6 non zero int -True