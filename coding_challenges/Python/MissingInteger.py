# Task
# Given an array A of N integers, returns the smallest positive integer 
# (greater than 0) that does not occur in A.


def solution1(A):
    a = 1

    while a in A:
        a = a + 1
    
    return a




# Solution 2 is less pythonic, doesn't use the 'in' operator in the 
# while loop
def is_in(a, A):

    for i in range(0,len(A)):
        if a == A[i]:
            return True
    
    return False

def solution2(A):
    a = 1
    while is_in(a, A) == True:
        a = a + 1
    
    return a



A = [1,2,3,-4,-10,4,5,6,8,9]

print (solution2(A))
