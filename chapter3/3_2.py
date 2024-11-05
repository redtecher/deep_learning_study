import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    return np.array(x>0,dtype=np.int_)

if __name__=='__main__':
    # x=np.array([-1.0,1.0,2.0])
    # print(x)
    # y = x>0
    # print(y)
    # y = y.astype(np.int_)
    # print(y)
    x= np.arange(-5.0,5.0,0.1)
    # print(x)
    y= step_function(x)
    plt.plot(x,y)
    plt.ylim(-0.1,1.1)
    plt.show()

