'''
once the list argument has been initialized to an empty array,
subsequent calls to append without any argument specified will continue to use
the same array to which list was originally initialized.
'''

def append(list = []):
    list.append(len(list))
    return list

print(append(list = [1,2,3,4,5]))
# [1, 2, 3, 4, 5, 5]

'''
>>> append()  # first call with no arg uses default list value of []
[0]
>>> append()  # but then look what happens...
[0, 1]
>>> append()  # successive calls keep extending the same default list!
[0, 1, 2]
>>> append()  # and so on, and so on, and so on...
[0, 1, 2, 3]
'''
'''
the append method would be one of a number of ways to avoid the
undesirable behavior described in the answer to the previous question:
'''
def append(list=None):
    if list is None:
        list = []
    list.append(len(list))
    return list



print(append())
print(append())
# [0]
# [0]
