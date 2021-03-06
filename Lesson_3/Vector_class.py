import math as mth

class Vector:
    def __init__(self,elements=[]):
        self.elements= elements
        self.length =  len(elements)
    def dot_prod(self,vect_arg):
        if len(vect_arg.elements)!= self.length:
            print('Error. Vectors must be of the same length')
        else:
            output_val=0
            for k in range(0,self.length):
                output_val+=vect_arg.elements[k]*self.elements[k]
        return output_val  # alternatively return Vector([output_val])

    def norm(self):
        output_val=0
        for k in range(0,self.length):
            output_val+=self.elements[k]*self.elements[k]
        return mth.sqrt(output_val)

    def norm_2(self):
        return mth.sqrt(self.dot_prod(Vector(self.elements)))
