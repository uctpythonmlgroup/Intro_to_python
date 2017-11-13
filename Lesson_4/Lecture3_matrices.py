##Lecture 3 - 2017-11-11

# starting with redefining class

class dog:
    def __init__(self,name,age,gender,colour): ## the first argument is always class
        self.name = name
        self.age = age
        self.gender= gender
        self.colour = colour
        print('You\'ve created a dog')
    
    def bark(self,n=1):
        print('{} is about to bark:' . format(self.name))## methods
        for k in range (0,n):
            print('Woof! ',end ='')
        print('')
    
    def jump(self, height=1): ## methods
        print('I just jumped {} metres' .format(height))
        
    
    def jump_and_bark(self,n=1, height=1): ## methods
        self.bark(n)
        self.jump(height)
        
##creating the matrix module 
class Matrix:
    def __init__(self,elements):
        self.n_rows = len(elements)
        self.n_cols = len(elements[0])
        self.elements = elements 
        self.dims = (self.n_rows, self.n_cols)
        
        for k in range(0,self.n_rows):
            if len(self.elements[k])!= self.n_cols:
                raise IndexError('Sorry, you can\'t create a matrix. Dimensions must agree')
        print('Congratulations,you\'ve created a matrix')
        
    
    def trace(self):
        s= 0
        for k in range(0, self.n_rows):
            s+= self.elements[k][k]
            
        return s 
    
    def is_square(self):
        return(self.n_rows == self.n_cols)


def add(A,B):
    if A.dims != B.dims :
        raise IndexError('Sorry.Dimensions are not equal')
    
    new_elements = []
    for k in range(0, A.n_rows):
        row = []
        for j in range (0, A.n_cols):
            new_ele = A.elements[k][j]+B.elements[k][j]
            row.append(new_ele)
        new_elements.append(row)
    
    C = Matrix(new_elements)
    
    return C
        
   #using created classes and methods in the next section 
   from lecture3 import Matrix, add

A = Matrix([[1,2],[3,4]])
B = Matrix([[5,6],[6,8]])
        
#print(A.n_rows,A.n_cols)    
#print(A.is_square())
#print(A.trace())

C = add(A,B)
print (C.elements) 

import numpy as np 
x = np.array([1,2,3])
y = np.array([2,3,5])

z = x+y
M = np.array ([[1,2],[3,4]])
print(np.shape(M))







   
   
   
   
   
        
        
            
