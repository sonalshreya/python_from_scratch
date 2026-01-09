
#basic functions
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits)
fruits.append('grape')
print(fruits)
fruits.count('apple')
print(fruits)
fruits.insert(1,'strawberry')
print(fruits)
fruits.remove('apple')
print(fruits)
fruits.pop()
print(fruits)
fruits.reverse()
print(fruits)
fruits.sort()

#Using lists as Stack
print("***********STACK******")
stack=['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
stack.append('grapes')
print(stack)
stack.pop()
print(stack)

#using lists as queue- not efficient instead use collections.deque

print("******Queue*****")

from collections import deque
queue=deque(fruits)

queue.append('grapes')
print(queue)
queue.popleft()
print(queue)


##List compressions

print("****list compressiond*****")

#create a list of squares
squares = [x**2 for x in range(10)]
print(squares)

vec=[-4,-2,0,2,4]
result=[x*2 for x in vec]
print(result)

##if you would not have written like this and would have wriiten like full boilpolate code first for would have come then if , similary here
resultneg=[x for x in vec if x>0]
print(resultneg)

##Nested list compression


##del
print("**del")
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
del a[2:4]
print(a)

##tuples
#Though tuples may seem similar to lists, 
# they are often used in different situations and for different purposes. 
# Tuples are immutable, and usually contain a heterogeneous sequence of elements 
# that are accessed via unpacking (see later in this section) or indexing (or even by attribute in the case of namedtuples). Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list.


##Sets
#either use set() 
##or basket={'apple','orange'}
# a-b, 
# a |b (letters in a or b or both), 
# a & b, 
# a ^b(letters in a or b but not in both)



##Dictionaries