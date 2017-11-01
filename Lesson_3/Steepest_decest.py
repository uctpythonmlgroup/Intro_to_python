def grad_desc(func,grad_func,x_0,lr=0.2,tol=1e-7):
    x_n=x_0
    
    while(abs(grad_func(x_n)>tol)):
    # could've used  abs(x_n-x_0)>tol
    # However abs(grad_func)>tol works better since we could have abs(x_n-x_0)<tol while abs(grad_func) is large
        
        # Update rule
        x_n -= lr*grad_func(x_n)
    return (x_n,func(x_n),grad_func(x_n))


#Example function
def f(x):
    return x**2
#Gradient/Derivative of f
def f_prime(x):
    return 2*x


#Call Gradient Function
print(grad_desc(f,f_prime,10))
