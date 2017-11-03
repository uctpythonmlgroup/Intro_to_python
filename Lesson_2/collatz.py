import random
def collatz_func(input_int):
    inital_input_int=input_int
 # its conjectured that for any positive intger >=1
 # this function will always termintate with input_int==1
 #i.e. for some deep reason this doesnt appear to have any cases resulting in
 # a infinite loop!
 #https://www.youtube.com/watch?v=5mFpVDpKX70
    N_rounds=0
    if input_int>=1:
        while input_int!=1:
            N_rounds=N_rounds+1
            if(input_int%2==1): #if the number is odd mulitply by 3 and add 1
                input_int=3*input_int+1
            else:input_int=input_int/2  #if even divide by 2
        print('For random input '+str(inital_input_int)+',the while condition fails '+ 'after '+str(N_rounds)+' interations')
        print('Current value for which while loop fails is '+str(input_int))
    else:print('The input argument must be greater than 0')

#generate 20 random numbers and evaluate collatz_func(random_int)
for random_int in random.sample(range(10000),20):
    collatz_func(random_int)
