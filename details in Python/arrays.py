'''
Consider the two approaches below for initializing an array and
the arrays that will result.
'''

# initializing an Array first method
x = [[1, 2, 3, 4]] *4
print(x)
# [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]

# initializing an Array second method

y = [[1, 2, 3, 4] for i in range(4)]
print(y)
# [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]

'''
Even though both methods seam to produce the same outcome there is an extreme
significant difference between the given methods.
'''
 # MODIFYING THE x ARRAY FROM THE PRIOR CODE:
x[0][0]= 123
print(x)
# [[123, 2, 3, 4], [123, 2, 3, 4], [123, 2, 3, 4], [123, 2, 3, 4]]

'''
this is going to happen because all the elemens fo the array refer
to the same object
'''

'''
this can be avoided with method2 which create an array of 4 elements,
each of which is itself indipendent
'''
y[0][0] = 123
print(y)
# [[123, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
