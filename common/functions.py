import numpy as np

def softmax(a): 
    c = np.max(a)
    exp_a = np.exp(a - c) # 溢出对策 
    sum_exp_a = np.sum(exp_a) 
    y = exp_a / sum_exp_a
    return y 

def cross_entropy_error(y, t): 
    if y.ndim == 1: 
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
    batch_size = y.shape[0] 
    return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size