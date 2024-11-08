# 数值微分
# 导数
import numpy as np
import matplotlib.pylab as plt

def f(x):
    return x*x

# f1 = 0.01x²+0.1x
def function1(x):
    return 0.01*x**2+0.1*x

# x =[x0,x1]
def function2(x):
    return x[0]**2 + x[1]**2

def numerical_diff(f, x):
    h = 1e-4 
    return (f(x+h) - f(x)) / h

if __name__=='__main__':
    x = np.arange(0.0,20.0,0.1)
    y = function1(x)
    # plt.xlabel('x')
    # plt.ylabel('f(x)')
    # plt.plot(x,y)
    # plt.show()
    print(numerical_diff(function1,5))
    print(numerical_diff(function1,10))

    # x0 = np.arange(-3,+3,0.1)
    # x1 = np.arange(-3,+3,0.1)
    # y = function2([x0,x1])
    # plt.xlabel('x0')
    # plt.ylabel('x1')

    # plt.plot(x,y)
    # plt.show()
    
