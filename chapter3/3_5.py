# 输出层的设计
import numpy as np
import matplotlib.pylab as plt

def softmax_source(a): 
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a) 
    y = exp_a / sum_exp_a
    return y

def softmax(a): 
    c = np.max(a)
    exp_a = np.exp(a - c) # 溢出对策 
    sum_exp_a = np.sum(exp_a) 
    y = exp_a / sum_exp_a
    return y 

if __name__=='__main__':
    a = np.array([1010,1000,990])
    # print(np.exp(a)/np.sum(np.exp(a)))
    print(softmax(a))
    print(np.sum(softmax(a)))



