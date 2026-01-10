##An Iterator is an object that lets you access items in a sequence one at a time. 
# It does not load the entire data at once, instead it gives one value when asked. 
# This saves memoryand follow lazy evaluation

l=iter(['Geeks', 'For', 'Geeks'])
print(next(l))
print(next(l))
print(next(l))

#iter() converts list into an iterator
#next() fetches the next value from the iterator
#it remembers its position and does not restart automatically


#Generators
#it is another way of creating iterators, but in a simpler and more readable manner. Instead of storing all values, generators produce values on the fly using the yield keyword.

def sq_numbers(n):
    for i in range(1,n+1):
        yield(i*i)
        
a=sq_numbers(4)

print(next(a))
print(next(a))
print(next(a))
print(next(a))

#yield sends one value at a time without ending the function
# Each next() call resumes the function from where it stopped
# Values are produced only when needed